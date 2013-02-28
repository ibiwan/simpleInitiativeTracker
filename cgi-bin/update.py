#!/usr/bin/python
with open('../current_initiative.txt', 'r+') as curf:
  cur = float(curf.read().strip())
  
  with open('../initiatives.csv') as initf:
    inits = [float(initrow.split(',')[0].strip()) for initrow in initf.readlines()]
  
  next = max([x for x in inits if x < cur] or [max(inits or [0.0])])
    
  curf.seek(0)
  curf.write(str(next))
