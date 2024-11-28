# Alarm

QT-based tray application for easily setting up and monitoring alarms. Accepts inputs such as *10m* and *16:20*.

## Install

Execute the following commands:

```
git clone --recurse-submodules https://github.com/tukkek/alarm
cd alarm/
python3 -m venv .venv/
.venv/bin/pip install -r requirements.txt
```

After that, you can create a menu-item (such as with Menu Libre) to create a new alarm. Point it to `/path/to/alarm/.venv/bin/python /path/to/alarm/alarm.py`.

## Credits

* Bell (CC-BY Attribution 3.0 Unported) https://archive.org/details/Berklee44v11
* Icon (Creative Commons 4 Attribution, Non Commercial) https://iconscout.com/free-icon/alarm-395
