#!/usr/bin/python
rawlist = []; beforecur = []; aftercur = []

curf = open('../current_initiative.txt')
cur = float(curf.read().strip())
curf.close()
initf = open('../initiatives.csv')
inits = initf.readlines()
initf.close()

for initrow in inits:
  fields = [x.strip() for x in initrow.split(',')]
  rawlist.append((float(fields[0]), int(float(fields[0])), fields[1], fields[2])) # (27.6, 27, kahlan, gm details)
rawlist.sort(reverse=True)

for row in rawlist:
  ((aftercur, beforecur)[row[0] > cur]).append(row)
displist = aftercur + beforecur

content    = "Content-Type: text/html\n\n"
headeropen = """<!DOCTYPE html><html><head><meta name="viewport" content="width = 320" /><meta http-equiv="refresh" content="5" >"""
admin      = """<script>
function updateInitiative() {
  var xmlhttp;
  if (window.XMLHttpRequest) { xmlhttp=new XMLHttpRequest(); }
  else { xmlhttp=new ActiveXObject("Microsoft.XMLHTTP"); }
  xmlhttp.onreadystatechange=function() { 
    if (xmlhttp.readyState==4 && xmlhttp.status==200) 
      window.location.reload; }
  xmlhttp.open("GET","update.py", false);
  xmlhttp.send(); 
}
</script></head><body><button type="button" onclick="updateInitiative()">Update Initiative</button><table>"""
rowtext    = "<tr><td align=\"right\">%s</td><td> </td><td>%s</td><td>%s</td></tr>"
closetable = "</table>"
footer     = "</body></html>"

print content + headeropen + admin
for row in displist:
  print rowtext % (row[1], row[2], row[3])
print closetable + footer
