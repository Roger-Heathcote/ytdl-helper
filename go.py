import state
import settings
from serve import serve
from display import display
import threading

if __name__ == '__main__':

	from sys import argv

	display_thread = threading.Thread(target=display, args=())
	# # thread.daemon = True
	display_thread.start()
	print ("Starting curses display...")

	try:
		if len(argv) == 2:
			serve(port=int(argv[1]))
		else:
			serve()

	except KeyboardInterrupt:
		pass
