# strainy
Strainy is an application for Mac that sends a notification every 20 minutes. The notification reminds the user to take a break from looking at the computer screen.

# Build .app

```bash
python setup.py py2app --packages=rumps,time,datetime,_thread -A
```

# Thanks to

Rumps Library

https://github.com/jaredks/rumps

https://rumps.readthedocs.io/en/latest/index.html