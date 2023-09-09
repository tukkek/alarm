#!/usr/bin/python3
import os,threading,sys,math,datetime

BELL='/usr/share/sounds/freedesktop/stereo/complete.oga'
MINUTE=60
DURATIONS={'h':60*MINUTE,'m':MINUTE,'s':1,}

message=' '.join(sys.argv[2:]) if len(sys.argv)>2 else 'Alarm'
seconds=-1
lastalert=False

def sound():
  if os.path.exists(BELL):
    os.system('paplay '+BELL)

def alert(force=False):
  global lastalert
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
  argument=argument.split(':') if ':' in argument else [argument[0:2],argument[2:4]]
  argument=[int(a) for a in argument]
  now=datetime.datetime.now().time()
  then=datetime.time(argument[0],argument[1])
  seconds=(then.hour-now.hour)*DURATIONS['h']+(then.minute-now.minute)*DURATIONS['m']
  if seconds<0:
    raise Exception('Alarm time in the past!')
  return seconds

seconds=parse(sys.argv[1])
message=message[0].upper()+message[1:]
alert(True)
tick()
