#!/usr/bin/python3
import os,math,datetime,simple_tray.tray,PyQt5.QtWidgets

MINUTE=60
HOUR=60*MINUTE
DURATIONS={'h':HOUR,'m':MINUTE,'s':1,}

class Tray(simple_tray.tray.Tray):
  def progress(self,seconds):
    if seconds<10:
      return
    for d in DURATIONS:
      if seconds>DURATIONS[d]:
        left=round(math.ceil(seconds/DURATIONS[d]))
        if left<10 or left%10==0:
          report=f'{message} in {left}{d}...'
          self.say(report)
        return
  
  def update(self):
    n=datetime.datetime.now()
    seconds=0 if n>=alarm else (alarm-n).seconds
    if seconds>0:
      self.progress(seconds)
      return
    self.say(f'{message}.',True)
    os.system('paplay bell.oga')
    self.application.quit()
    
class Input(PyQt5.QtWidgets.QDialog):#https://stackoverflow.com/a/56019738
  def __init__(self):
    super().__init__()
    self.setWindowTitle('Alarm')
    l=PyQt5.QtWidgets.QFormLayout(self)
    self.title=PyQt5.QtWidgets.QLineEdit(self)
    l.addRow("Title:",self.title)
    self.target=PyQt5.QtWidgets.QLineEdit(self)
    l.addRow("Target:",self.target)
    buttons=PyQt5.QtWidgets.QDialogButtonBox(PyQt5.QtWidgets.QDialogButtonBox.Ok)
    l.addWidget(buttons)
    buttons.accepted.connect(self.accept)
    buttons.rejected.connect(self.reject)

message='Alarm'
tray=Tray(message,'icon.png',1)
alarm=None
    
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

i=Input()
i.exec()
message=i.title.text()
target=i.target.text()
if target and message:
  alarm=datetime.datetime.now()+datetime.timedelta(seconds=parse(target)+1)
  message=message[0].upper()+message[1:]
  tray.start()
