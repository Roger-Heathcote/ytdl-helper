# ytdl-helper

Usage: ./go.py [optional: A PORT NUMBER]

*-v flag* enables verbose http request logging

*--nd flag* disables the curses display

Don't use both flags together, unless you thrive on chaos.

---

Settings...

Put this in a file called settings.py...

```python
settings = {}
settings['port'] = "undefined"
settings['output folder'] = "PATH TO THE FOLDER YOU WANT YOUR FILES SAVING IN/"
```

Do not forget the trailing slash when specifying a path name!