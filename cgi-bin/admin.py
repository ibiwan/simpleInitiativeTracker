#!/usr/bin/python
rawlist = []; beforecur = []; aftercur = []

curf = open('../current_initiative.txt')
cur = float(curf.read().strip())
curf.close()
initf = open('../initiatives.csv')
inits = "".join(initf.readlines()).split(';')
initf.close()

for initrow in inits:
  fields = [x.strip() for x in initrow.split("#")]
  if fields != None and len(fields) != 2 and len(fields) != 3:
    continue
  f = float(fields[0])
  i = int(f)
  rawlist.append((f, i, fields[1], fields[2])) # (27.6, 27, kahlan, gm details)
rawlist.sort(reverse=True)

displist = [x for x in rawlist if x[0] <= cur] + [x for x in rawlist if x[0] > cur]

content    = "Content-Type: text/html\n\n"
headeropen = """<!DOCTYPE html><html><head><meta name="viewport" content="width = 320" /><meta http-equiv="refresh" content="5" >"""
admin      = """<script>
function updateInitiative() {
  var xmlhttp;
  if (window.XMLHttpRequest) { xmlhttp=new XMLHttpRequest(); }
  else { xmlhttp=new ActiveXObject("Microsoft.XMLHTTP"); }
  xmlhttp.open("POST","update.py", false);
  xmlhttp.send(); 
  window.location.reload();
}
</script></head><body><button type="button" onclick="updateInitiative()">Update Initiative</button><table border=1 cellpadding=3>"""
rowtext    = "<tr><td align=\"right\">%s</td><td>%s</td><td>%s</td></tr>"
closetable = "</table>"
footer     = "</body></html>"

print content + headeropen + admin
for row in displist:
  print rowtext % (row[1], row[2], row[3])
print closetable + footer
