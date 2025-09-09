#!/usr/bin/python3
TESTS={
  'N-1':'23:00','N-2':'22:00','N-3':'21:00',
  'E+3':'21:00','E+2':'20:00','E+1':'19:00','E+0':'18:00','E-0':'18:00','E-1':'17:00','E-2':'16:00','E-3':'15:00',
  'D+3':'15:00','D+2':'14:00','D+1':'13:00','D+0':'12:00','D-0':'12:00','D-1':'11:00','D-2':'10:00','D-3':'9:00',
  'M+3':'9:00','M+2':'8:00','M+1':'7:00','M+0':'6:00','M-0':'6:00','M-1':'5:00','M-2':'4:00','M-3':'3:00',
  'N+3':'3:00','N+2':'2:00','N+1':'1:00','N+0':'0:00','N-0':'0:00',
}
PERIODS={'N': 0,'M':6,'D':12,'E':18}

class SunFormat:
  def translate(self,time):
    time=time.replace(' ','').upper()
    if not time[0].isalpha():
      return time
    period=time[0]
    operator=time[1]
    offset=int(time[2:])
    hour=PERIODS[period]
    if operator=='+':
      hour+=offset
    else:
      hour-=offset
    while hour>24:
      hour+=24
    return f'{abs(hour%24)}:00'

if __name__=='__main__':
  converter=SunFormat()
  for test in TESTS:
    expected=TESTS[test]
    result=converter.translate(test)
    if result!=expected:
      raise Exception('Cannot convert from sun-format to clock-format!',test,result)
    standard=[expected,expected.replace(':','')]
    for expected in standard:
      result=converter.translate(expected)
      if result!=expected:
        raise Exception('Converter failed to preserve clock-format!',expected,result)
  print('Success!')
