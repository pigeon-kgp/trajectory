import os, sys
if 'SUMO_HOME' in os.environ:
 tools = os.path.join(os.environ['SUMO_HOME'], 'tools')
 sys.path.append(tools)
else:   
 sys.exit("please declare environment variable 'SUMO_HOME'")
import sumolib

net = sumolib.net.readNet('sumo/map.net.xml')
# net.convertXY2LonLat()
# net.getEdge('myEdgeID').getToNode().getID()
print net.convertXY2LonLat(net.getNode(net.getEdge('103230546#1').getToNode().getID()).getCoord()[0],net.getNode(net.getEdge('103230546#1').getToNode().getID()).getCoord()[1])