#!/usr/bin/python3
import os,math,datetime,simple_tray.tray,PyQt6.QtWidgets,PyQt6.QtGui

MINUTE=60
HOUR=60*MINUTE
DURATIONS={'h':HOUR,'m':MINUTE,'s':1,}

class Tray(simple_tray.tray.Tray):
  def progress(self,force=False):
    n=datetime.datetime.now()
    seconds=0 if n>=alarm else (alarm-n).seconds
    if seconds>=10 or force:
      for d in DURATIONS:
        if seconds>DURATIONS[d]:
          left=round(math.ceil(seconds/DURATIONS[d]))
          if left<10 or left%10==0 or force:
            report=f'{message} in {left}{d}...'
            self.say(report)
          break
    return seconds
  
  def update(self):
    if self.progress()==0:
      self.say(f'{message}.',True)
      os.system('paplay bell.oga')
      self.application.quit()
    
class Input(PyQt6.QtWidgets.QDialog):
  def __init__(self):
    super().__init__()
    self.setWindowTitle('Alarm')
    l=PyQt6.QtWidgets.QFormLayout(self)
    self.title=PyQt6.QtWidgets.QLineEdit(self)
    l.addRow("Title:",self.title)
    self.target=PyQt6.QtWidgets.QLineEdit(self)
    l.addRow("Target:",self.target)
    cancel=PyQt6.QtWidgets.QDialogButtonBox.StandardButton.Cancel
    ok=PyQt6.QtWidgets.QDialogButtonBox.StandardButton.Ok
    buttons=PyQt6.QtWidgets.QDialogButtonBox(ok|cancel)
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
  tray.progress(force=True)
  target=PyQt6.QtGui.QAction()
  target.setText(f'{message} at {alarm.strftime("%H:%M")}')
  tray.menu.addAction(target)
  tray.start()
