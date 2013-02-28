#!/usr/bin/python
rawlist = []; beforecur = []; aftercur = []
with open('../current_initiative.txt') as curf:
  cur = float(curf.readline().strip())
with open('../initiatives.csv') as initf:
  inits = initf.readlines()

for initrow in inits:
  fields = [x.strip() for x in initrow.split(",")]
  rawlist.append((float(fields[0]), int(float(fields[0])), fields[1])) # (27.6, 27, kahlan)
rawlist.sort(reverse=True)

for row in rawlist:
  (beforecur if row[0] > cur else aftercur).append(row)
displist = aftercur + beforecur

content    = "Content-Type: text/html\n\n"
headeropen = """<!DOCTYPE html><html><head><meta http-equiv="refresh" content="5" >"""
nocache    = """<meta name="viewport" content="width = 320" /><META HTTP-EQUIV="Pragma" CONTENT="no-cache"> <META HTTP-EQUIV="Expires" CONTENT="-1">"""
bodytable  = "</head><body><table>"
rowtext    = "<tr><td align=\"right\">%s</td><td> </td><td>%s</td></tr>"
footer     = "</table></body>%s</html>"

print content + headeropen + nocache + bodytable
for row in displist:
  print rowtext % (row[1], row[2])
print footer % ("<head>" + nocache + "</head>")
