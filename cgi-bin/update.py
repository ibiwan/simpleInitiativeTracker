#!/usr/bin/python
curf = open('../current_initiative.txt', 'r+')
cur = float(curf.read().strip())
  
initf = open('../initiatives.csv')
inits = [float(initrow.split(',')[0].strip()) for initrow in initf.readlines()]
initf.close()
  
next = max([x for x in inits if x < cur] or [max(inits or [0.0])])
    
curf.seek(0)
curf.write(str(next))
curf.close()
