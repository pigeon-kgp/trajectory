import reader
import math
THRESH=0.001
points=reader.get_points('kolkata.osm')
row=[]
G={}
prevpoint=0
for point in points:
	if len(row)==0:
		row.append(point)
		prevpoint=point
		continue
	try:
		dist=G[str(point)+" "+str(prevpoint)]
		dist=0
	except:
		dist=math.fabs(point[0]-prevpoint[0])+math.fabs(point[1]-prevpoint[1])
	if dist>THRESH:
		for each in G:
			if G[each]<=THRESH: continue
		G[str(point)+" "+str(prevpoint)]=dist
		G[str(prevpoint)+" "+str(prevpoint)]=dist
print G