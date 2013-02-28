#!/usr/bin/python
rawlist = []; beforecur = []; aftercur = []

curf = open('../current_initiative.txt')
cur = float(curf.read().strip())
curf.close()

initf = open('../initiatives.csv')
inits = initf.readlines()
initf.close()

for initrow in inits:
  fields = initrow.split(',')
  fields = [x.strip() for x in fields]
  rawlist.append((float(fields[0]), int(float(fields[0])), fields[1], fields[2]))
rawlist.sort(reverse=True)

for row in rawlist:
  if row[0] > cur: beforecur.append(row)
  else:            aftercur.append(row)
displist = aftercur + beforecur

content = "Content-Type: text/html\n\n"
headeropen = """<!DOCTYPE html><html><head><meta http-equiv="refresh" content="5" >"""
admin = """<script>
function updateInitiative() {
  var xmlhttp;
  // code for IE7+, Firefox, Chrome, Opera, Safari
  if (window.XMLHttpRequest) { xmlhttp=new XMLHttpRequest(); }
  // code for IE6, IE5
  else { xmlhttp=new ActiveXObject("Microsoft.XMLHTTP"); }
  xmlhttp.onreadystatechange=function() {
      if (xmlhttp.readyState==4 && xmlhttp.status==200) {
        document.getElementById("myDiv").innerHTML=xmlhttp.responseText; } }
  xmlhttp.open("POST","update.py", false);
  xmlhttp.send(); 
  window.location.reload(); 
  //history.go(0);
}
</script></head><body><button type="button" onclick="updateInitiative()">Update Initiative</button><table>"""
rowtext = "<tr><td align=\"right\">%s</td><td> </td><td>%s</td><td>%s</td></tr>"
closetable = "</table>"
footer = "</body></html>"

print content + headeropen + admin
for row in displist:
  print rowtext % (row[1], row[2], row[3])
print closetable 
#print " " + str(cur) + " : " + str(beforecur) + " : " + str(aftercur) + " " + 
print footer
