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

---

If you need something to POST the URLs to this program then you can try my firefox plugin: [Utility Button](https://github.com/Roger-Heathcote/utility-button)

No great attention has been paid to security so far so only use it on LANs you can trust.
