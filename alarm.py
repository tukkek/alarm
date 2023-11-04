#!/usr/bin/python3
import os,threading,sys,math,datetime

BELL='/usr/share/sounds/freedesktop/stereo/complete.oga'
MINUTE=60
HOUR=60*MINUTE
DURATIONS={'h':HOUR,'m':MINUTE,'s':1,}

message=' '.join(sys.argv[2:]) if len(sys.argv)>2 else 'Alarm'
alarm=datetime.datetime.now()
lastalert=False

def sound():
  if os.path.exists(BELL):
    os.system('paplay '+BELL)

def check():
  n=datetime.datetime.now()
  return 0 if n>=alarm else (alarm-n).seconds

def alert(force=False):
  global lastalert
  seconds=check()
  for d in DURATIONS:
    if seconds>DURATIONS[d]:
      left=round(math.ceil(seconds/DURATIONS[d]))
      if not force and left>10 and left%10!=0:
        break
      text=f'{message} in {left}{d}...'
      if lastalert!=text:
        notify(text)
      lastalert=text
      break

def notify(text,force=False):
  print(text)
  if check()>=MINUTE or force:
    os.system(f'notify-send Alarm "{text}"')

def tick():
  if check()>=1:
    alert()
    threading.Timer(1,tick).start()
    return
  notify(message,True)
  sound()

def parse(argument):
  argument=argument.lower()
  for d in DURATIONS:
    if d in argument:
      argument=argument.replace(d,'')
      return int(argument)*DURATIONS[d]
  argument=argument.split(':') if ':' in argument else [argument[0:2],argument[2:4]]
  argument=[int(a) for a in argument]
  now=datetime.datetime.now().time()
  then=datetime.time(argument[0],argument[1])
  seconds=(then.hour-now.hour)*HOUR+(then.minute-now.minute)*MINUTE
  if seconds<0:
    seconds+=24*HOUR
  return seconds

alarm+=datetime.timedelta(seconds=parse(sys.argv[1]))
message=message[0].upper()+message[1:]
alert(True)
tick()
