import os, pathlib
this_folder = str(pathlib.Path(__file__).parent.resolve())

settings = {}
settings['port'] = "undefined"
settings['curses'] = True
settings['output folder'] = this_folder + os.sep
#YTDL-ARGS=--no-playlist, --limit-rate 8M, --restrict-filenames --simulate --no-call-home