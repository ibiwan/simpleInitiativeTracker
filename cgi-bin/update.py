#!/usr/bin/python
curf = open('../current_initiative.txt', 'r+')
cur = float(curf.read().strip())
  
initf = open('../initiatives.csv')
lines = "".join(initf.readlines()).split(';')
initf.close()
inits = []
for initrow in lines:
  fields = initrow.split('#')
  if fields != None and len(fields) != 2 and len(fields) != 3:
    continue
  inits.append(float(fields[0].strip()))
  
next = max([x for x in inits if x < cur] or [max(inits or [0.0])])
    
curf.seek(0)
curf.write(str(next))
curf.close()

print "Content-Type: text/html\n\nThanks!"
