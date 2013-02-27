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

admin = """
<script>
function updateInitiative()
{
  var xmlhttp;
  if (window.XMLHttpRequest)
  {// code for IE7+, Firefox, Chrome, Opera, Safari
    xmlhttp=new XMLHttpRequest();
  }
  else
  {// code for IE6, IE5
    xmlhttp=new ActiveXObject("Microsoft.XMLHTTP");
  }
  xmlhttp.onreadystatechange=function()
    {
      if (xmlhttp.readyState==4 && xmlhttp.status==200)
      {
        document.getElementById("myDiv").innerHTML=xmlhttp.responseText;
      }
    }
  xmlhttp.open("POST","update.py",true);
  xmlhttp.send();
}
</script></head><body>

<button type="button" onclick="updateInitiative()">Update Initiative</button>

<table>
"""

print(headeropen)
print(admin)
for row in displist:
  print(rowtext % (row[1], row[2]))
print(footer)
