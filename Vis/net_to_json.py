import random
from xml.dom import minidom
import os

os.environ['SUMO_HOME'] = "/usr/share/sumo"

import sys
if 'SUMO_HOME' in os.environ:
 tools = os.path.join(os.environ['SUMO_HOME'], 'tools')
 sys.path.append(tools)
else:   
 sys.exit("please declare environment variable 'SUMO_HOME'")
import sumolib

net = sumolib.net.readNet('sumo/map.net.xml')

xmldoc = minidom.parse('/home/ss/Dropbox/Wriju/Codes/10.4.1.72_trajectory_clone/Vis/sumo/map.net.xml')
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
	output[idno]={"from":net.convertXY2LonLat(junctions[fr][0],junctions[fr][1]),"to":net.convertXY2LonLat(junctions[to][0],junctions[to][1]),"distance":float(dist),"traffic":random.randrange(1,6)}
# print output
import json
string=json.dumps(output, indent=2)
print string
f=open("/home/ss/Dropbox/Wriju/Codes/10.4.1.72_trajectory_clone/Vis/out.json","w")
f.write(string)
os.system('rm /home/ss/Dropbox/Wriju/Codes/10.4.1.72_trajectory_clone/Vis/tables/*')