import random
from xml.dom import minidom
import os
xmldoc = minidom.parse('/home/ubuntu/Desktop/trajectory_clone/Vis/sumo/map.net.xml')
junclist= xmldoc.getElementsByTagName('junction')
junctions={}
for junc in junclist:
	idno=str(junc.attributes['id'].value)
	try:
		x=float(junc.attributes['x'].value)
		y=float(junc.attributes['y'].value)
	except: continue
	junctions[idno]=[x,y]
itemlist = xmldoc.getElementsByTagName('edge')
output={}
for item in itemlist:
	idno=str(item.attributes['id'].value)
	try:
		fr=str(item.attributes['from'].value)
		to=str(item.attributes['to'].value)
	except:  continue
	lanes=item.getElementsByTagName('lane')
	dist=0
	for lane in lanes:
		dist+=float(lane.attributes['length'].value)
	output[idno]={"from":junctions[fr],"to":junctions[to],"distance":float(dist),"traffic":random.randrange(1,6)}
# print output
import json
string=json.dumps(output, indent=2)
print string
f=open("/home/ubuntu/Desktop/trajectory_clone/Vis/out.json","w")
f.write(string)
os.system('rm /home/ubuntu/Desktop/trajectory_clone/Vis/tables/*')