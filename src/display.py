from threading import Timer
import _thread
from state import state
import curses
import datetime
from time import sleep
import re
import sys
import settings

def display_loop(*args):

    stdscr = curses.initscr()
    curses.noecho()
    curses.cbreak()
    stdscr.keypad(True)
    stdscr.nodelay(True)
    curses.curs_set(0)

    verbose = False

    try:

        while True:

            rows, cols = stdscr.getmaxyx()
            stdscr.clear()

            out = f"Serving on port: {settings.port} :: {len(state['job'])} jobs."
            stdscr.addstr(0, 0, out)

            now = datetime.datetime.now().strftime("%H:%M:%S")
            stdscr.addstr(0, cols-len(now), now)

            for idx, thread_id in enumerate(state["job"]):
                job_state = state["job"][thread_id]
                if verbose:
                    # Display domain?
                    out = str(thread_id)[-4:] + ": " + job_state 
                else:
                    percentage = re.search('[0-9\.]{1,5}%', job_state)
                    if(percentage):
                        out = str(thread_id)[-4:] + ": " + percentage.group()
                    else:
                        out = "Running."
                stdscr.addstr(idx+1, 0, out)

            if verbose:
                stdscr.addstr(rows-1, cols-4, "(v)")

            try:
                key = stdscr.getkey()
                stdscr.addstr(rows-1, 0, "processing")
                if key in "Qq":
                    return
                else:
                    verbose = not(verbose)
            except:
                try:
                    stdscr.addstr(rows-1, 0, f"[Q] - Quit")
                except curses.error: #addstr's fail when resizing
                    pass

            stdscr.refresh()
            sleep(0.5)

    except BaseException as error:
        print('An exception occurred: {}'.format(error))
        raise

    finally:
        curses.echo()
        curses.nocbreak()
        stdscr.keypad(False)
        curses.endwin()
        print("Quit at:", datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"))
        if sys.exc_info()[0] is not None:
            _thread.interrupt_main()
            raise
        return

def display():
    sleep(2) # So we have time to see any startup console messages/errors.
    curses.wrapper(display_loop)
    _thread.interrupt_main()
