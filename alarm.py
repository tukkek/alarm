#!/usr/bin/python3
import os,threading,sys,math

BELL='/usr/share/sounds/freedesktop/stereo/complete.oga'
MINUTE=60
DURATIONS={'h':60*MINUTE,'m':MINUTE,'s':1,}

message=sys.argv[2] if len(sys.argv)>2 else 'Alarm'
seconds=-1
lastalert=False

def sound():
  if os.path.exists(BELL):
    os.system('paplay '+BELL)

def alert():
  global lastalert
  for d in DURATIONS:
    if seconds>DURATIONS[d]:
      left=round(math.ceil(seconds/DURATIONS[d]))
      if left>10 and left%10!=0:
        break
      text=f'{message} in {left}{d}...'
      if lastalert!=text:
        notify(text)
      lastalert=text
      break

def notify(text,force=False):
  print(text)
  if seconds>=MINUTE or force:
    os.system(f'notify-send Alarm "{text}"')

def tick():
  global seconds
  if seconds>=1:
    alert()
    seconds-=1
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
  return int(argument)

seconds=parse(sys.argv[1])
tick()
