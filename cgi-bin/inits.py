#!/usr/bin/python
rawlist = []; beforecur = []; aftercur = []
curf = open('../current_initiative.txt')
cur = float(curf.readline().strip())
curf.close()
initf = open('../initiatives.csv')
inits = initf.readlines()
initf.close()

for initrow in inits:
  fields = [x.strip() for x in initrow.split(",")]
  rawlist.append((float(fields[0]), int(float(fields[0])), fields[1])) # (27.6, 27, kahlan)
rawlist.sort(reverse=True)

for row in rawlist:
  ((aftercur, beforecur)[row[0] > cur]).append(row)
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
