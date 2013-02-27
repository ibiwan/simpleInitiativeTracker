#!/usr/bin/python

curf = open('current_initiative.txt', 'r+')
cur = float(curf.read().strip())

inits = []
initrows = open('initiatives.csv').readlines()
for initrow in initrows:
  (init, character) = initrow.split(',')
  init = init.strip()
  inits.append(float(init))

next = max([x for x in inits if x < cur] or [max(inits or [0.0])])
#print(next)
curf.seek(0)
curf.write(str(next))
