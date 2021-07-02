#!/usr/bin/python3
from state import state
import settings
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
		print("Non-curses interface. CTRL-C to quit.")

	state["verbose"] = args.verbose

	try:
		serve(port=args.port)
	except KeyboardInterrupt:
		print("Keyboard interrupt, quitting...")
