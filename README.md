# Alarm
QT-based tray application for easily setting-up and monitoring alarms. 

# Valid formats
The program comprehends these inputs:
* Standard-clock format (0:00; 10:00)...
* Military-format (000; 1000)...
* Sun-clock format (N+0; D-2)...
* Relative-time (1h; 2m; 30s)...

The accepted letters and their meanings are:
* S for seconds; M for minutes; H for hours
* N for night (0:00); M for morning (6:00); D for day (12:00); E for evening (18:00)

# Installation
Execute the following commands:
~~~sh
git clone --recurse-submodules https://github.com/tukkek/alarm
cd alarm/
python3 -m venv .venv/
.venv/bin/pip install -r requirements.txt
~~~

After that, you can create a menu-item (such as with Menu Libre) to create a new alarm. Point it to `/path/to/alarm/.venv/bin/python /path/to/alarm/alarm.py`.

# Credits
* Bell (CC-BY Attribution 3.0 Unported) https://archive.org/details/Berklee44v11
* Icon (Creative Commons 4 Attribution, Non Commercial) https://iconscout.com/free-icon/alarm-395
