from threading import Timer
import _thread
from state import state
import curses
import datetime
from time import sleep
import re
import sys

stdscr = curses.initscr()
curses.noecho()
curses.cbreak()
stdscr.keypad(True)
stdscr.nodelay(True)
curses.curs_set(0)

def display_loop(*args):

    verbose = False

    try:

        while True:

            rows, cols = stdscr.getmaxyx()
            stdscr.clear()

            out = f"We have {len(state['job'])} jobs."
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

            try:
                key = stdscr.getkey()
                stdscr.addstr(rows-1, 0, f"Key pressed: {key}")
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
    curses.wrapper(display_loop)
    _thread.interrupt_main()
