#!/usr/bin/python
rawlist = []; beforecur = []; aftercur = []

curf = open('../current_initiative.txt')
cur = float(curf.read().strip())
curf.close()

initf = open('../initiatives.csv')
inits = initf.readlines()
initf.close()

for initrow in inits:
  fields = initrow.split(",")
  fields = [x.strip() for x in fields]
#  (init, character) = initrow.split(',')
#  init = init.strip(); character = character.strip()
  rawlist.append((float(fields[0]), int(float(fields[0])), fields[1]))
rawlist.sort(reverse=True)

for row in rawlist:
  if row[0] > cur: beforecur.append(row)
  else:            aftercur.append(row)
displist = aftercur + beforecur

content = "Content-Type: text/html\n\n"
headeropen = """<!DOCTYPE html><html><head><meta http-equiv="refresh" content="5" >"""
nocache = """<META HTTP-EQUIV="Pragma" CONTENT="no-cache"> <META HTTP-EQUIV="Expires" CONTENT="-1">"""
bodytable = '</head><body><table>'
rowtext = "<tr><td align=\"right\">%s</td><td> </td><td>%s</td></tr>"
footer = "</table></body>%s</html>"

print content + headeropen + nocache + bodytable
for row in displist:
  print rowtext % (row[1], row[2])
print footer % ("<head>" + nocache + "</head>")
