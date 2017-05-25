def get_points(filename):
	from xml.dom import minidom
	xmldoc = minidom.parse(filename)
	itemlist = xmldoc.getElementsByTagName('way')
	nodelist=[]
	for item in itemlist:
		each=item.getElementsByTagName('nd')
		tags=item.getElementsByTagName('tag')
		flag=0
		for tag in tags:
			if tag.attributes['k'].value=="highway":
				flag=1; break
		if flag==1:
			for e in each:
				nodelist.append(str(e.attributes['ref'].value))
	print nodelist
	points=[]
	itemlist = xmldoc.getElementsByTagName('node')
	for item in itemlist:
		idno=item.attributes['id'].value
		if idno in nodelist:
			lat=float(str(item.attributes['lat'].value))
			lon=float(str(item.attributes['lon'].value))
			time=str(item.attributes['timestamp'].value)
			points.append([lat,lon,time])
	return points #Since the data from .osm file is time sorted, no further sorting is being done