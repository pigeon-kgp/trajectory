#1131,2008-02-05 15:02:00,116.93127,40.42362
path=raw_input("Enter Path\n")
import os
from math import fabs
folderList=os.listdir(path+'/')
cars={}
for folders in folderList:
    os.chdir(path+'/'+folders+'/')
    fileList=os.listdir(path+'/'+folders+'/')
    for files in fileList:
        with open(files,"r") as InputFile:        
            myfile = open(path+'/'+folders+'/'+files, "r")
            print("Extracting.."+path+'/'+folders+'/'+files)
            prevlat=-180; prevlon=-180; prevtime=0
            while(True):
                line=myfile.readline()
                if not line: myfile.close(); break
                lat=float(line.split(",")[2])
                lon=float(line.split(",")[3])
                time=(line.split(",")[1])[11:]
                carno=line.split(",")[0]
                timenow=0
                try:
                    if prevlat==lat and prevlon==lon:
                        timenow=int(time[0:2])*3600+int(time[3:5])*60+int(time[6:])
                        timediff=fabs(timenow-prevtime)
                        cars[carno][str([lat,lon])]+=timediff
                    else:
                        cars[carno][str([lat,lon])]+=1
                except KeyError:
                    try:
                        cars[carno][str([lat,lon])]=1
                    except KeyError:
                        cars[carno]={}
                        cars[carno][str([lat,lon])]=1
                prevlat=lat; prevlon=lon; prevtime=timenow    
            myfile.close()
print "\n"
for i in cars:
    temp=""; max=0
    for j in cars[i]:
        if cars[i][j]>max: max=cars[i][j]; temp=str(j)
    print str(i)+" probably resides at: "+temp[1:len(temp)-1]+" as it has traced the point for "+str(max)+" seconds. "
