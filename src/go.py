#!/usr/bin/python3
import os
try:
	import settings
except (ModuleNotFoundError):
	from shutil import copyfile
	print("Creating new config file.")
	print("To change settings such as the destination folder edit settings.py.")
	copyfile("defaults.py", "settings.py")
	import settings

from state import state
from serve import serve
from display import display
import threading
import argparse

if __name__ == '__main__':

	parser = argparse.ArgumentParser(description="Multithreading youtube-dl helper")
	parser.add_argument("-nd","--no-display", help="Don't start curses display.", action="store_true")
	parser.add_argument("-v","--verbose", help="Log http activity to the console.", action="store_true")
	parser.add_argument("port", nargs="?", default=7777, type=int)
	args = parser.parse_args()

	settings.port = args.port

	if(args.no_display == False):
		display_thread = threading.Thread(target=display, args=())
		display_thread.start()
	else:
		settings.curses = False
		print("Non-curses interface. CTRL-C to quit.")

	state["verbose"] = args.verbose

	try:
		serve(port=args.port)
	except KeyboardInterrupt:
		print("Keyboard interrupt, quitting...")
