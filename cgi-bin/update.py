#!/usr/bin/python
curf = open('../current_initiative.txt', 'r+')
cur = float(curf.read().strip())

inits = []
initrows = open('../initiatives.csv').readlines()
for initrow in initrows:
  inits.append(float(initrow.split(',')[0].strip()))

next = max([x for x in inits if x < cur] or [max(inits or [0.0])])
  
curf.seek(0)
curf.write(str(next))
curf.close()

print "Content-Type: text/html\n\n"
