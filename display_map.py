import matplotlib.pyplot as plt
import mplleaflet
f = open('Vis/out_path_lat_lon','r')

lat = []
lon = []
while True:
	line = f.readline()
	if not line :
		break
	lon.append(line.strip().split(',')[0])
	lat.append(line.strip().split(',')[1])
plt.plot(lon,lat,'b')

plt.plot(lon,lat,'bs')
try:
    plt.plot(lon[0],lat[0],'rs')
    plt.plot(lon[-1],lat[-1],'gs')
except:
    pass
mplleaflet.show()


