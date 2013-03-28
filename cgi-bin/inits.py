#!/usr/bin/python
rawlist = []; beforecur = []; aftercur = []
curf = open('../current_initiative.txt')
cur = float(curf.readline().strip())
curf.close()
initf = open('../initiatives.csv')
inits = "".join(initf.readlines()).split(';')
initf.close()

for initrow in inits:
  fields = [x.strip() for x in initrow.split("#")]
  if fields != None and len(fields) != 2 and len(fields) != 3:
    continue
  rawlist.append((float(fields[0]), int(float(fields[0])), fields[1])) # (27.6, 27, kahlan)
rawlist.sort(reverse=True)

displist = [x for x in rawlist if x[0] <= cur] + [x for x in rawlist if x[0] > cur]

content    = "Content-Type: text/html\n\n"
headeropen = """<!DOCTYPE html><html><head><meta http-equiv="refresh" content="5" >"""
nocache    = """<meta name="viewport" content="width = 320" /><META HTTP-EQUIV="Pragma" CONTENT="no-cache"> <META HTTP-EQUIV="Expires" CONTENT="-1">"""
bodytable  = "</head><body><table border=1 cellpadding=3>"
rowtext    = "<tr><td align=\"right\">%s</td><td>%s</td></tr>"
footer     = "</table></body>%s</html>"

print content + headeropen + nocache + bodytable
for row in displist:
  print rowtext % (row[1], row[2])
print footer % ("<head>" + nocache + "</head>")
