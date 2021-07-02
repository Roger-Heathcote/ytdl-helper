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

	with lock:
		state["job"][thread_id] = "Starting..."

	try:

		if not('data' in req):
			print ("Can't do much without data!")
			return
		url = req["data"]

		domain = urlparse(url).netloc
		if(domain == ''): return

		output_folder = settings["output folder"]
		outputTemplate = f"{output_folder}%(title)s.%(ext)s"

		download = subprocess.Popen(["youtube-dl", url, "-o", outputTemplate],
										universal_newlines=True,
										stdout = subprocess.PIPE,
										stderr=subprocess.STDOUT)
		for line in download.stdout:
			# Don't bother locking for output lines
			state["job"][thread_id] = line

		state["job"][thread_id] = "done."
		time.sleep(2)

	finally:
		with lock:
			state["job"].pop(thread_id, None)
		print ("done.")