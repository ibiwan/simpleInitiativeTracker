#!/usr/bin/python
rawlist = []; beforecur = []; aftercur = []

cur = float(open('current_initiative.txt').read().strip())

inits = open('initiatives.csv').readlines()
for initrow in inits:
  (init, character) = initrow.split(',')
  init = init.strip(); character = character.strip()
  rawlist.append((float(init), int(float(init)), character))

rawlist.sort(reverse=True)

for row in rawlist:
  if row[0] > cur: beforecur.append(row)
  else:            aftercur.append(row)

displist = aftercur + beforecur

headeropen = """
<!DOCTYPE html>


<html><head><meta http-equiv="refresh" content="5" >
"""
bodytable = '</head><body><table>'
rowtext = "<tr><td>%s</td><td>%s</td></tr>"
footer = "</table></body></html>"

print(headeropen)
print(bodytable)
for row in displist:
  print(rowtext % (row[1], row[2]))
print(footer)
