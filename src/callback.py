from urllib.parse import urlparse
import time
import subprocess
import threading
from settings import settings
from state import state
from threading import Lock
lock=Lock()

def callback(req):
	thread_id = threading.current_thread().ident

	try:

		if not settings['curses']:
			print ("Attempting download")

		if not('data' in req):
			print ("Can't do much without data!")
			return
		url = req["data"]

		domain = urlparse(url).netloc
		if(domain == ''): return

		# check domain and sleep in a loop if present
		all_clear = False
		while not all_clear:
			all_clear = True
			with lock:
				for job in state["job"]:
					if state["job"][job]["domain"] == domain:
						all_clear = False
			if not all_clear:
				msg = f"Already downloading from {domain}, sleeping for 5s"
				if settings['curses']:
					state["job"][thread_id] = {"domain": "", "display": msg}
				else:
					print (msg)
				time.sleep(5)

		with lock:
			state["job"][thread_id] = {"domain": domain, "display": "Starting..."}

		output_folder = settings["output folder"]
		outputTemplate = f"{output_folder}%(title)s.%(ext)s"

		download = subprocess.Popen(["youtube-dl", url, "-o", outputTemplate],
										universal_newlines=True,
										stdout = subprocess.PIPE,
										stderr=subprocess.STDOUT)
		for line in download.stdout:
			# Don't bother locking for output lines
			state["job"][thread_id]["display"] = line

		state["job"][thread_id]["display"] = "done."
		time.sleep(2)

	finally:
		with lock:
			state["job"].pop(thread_id, None)
		print ("done.")