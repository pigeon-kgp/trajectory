#1131,2008-02-05 15:02:00,116.93127,40.42362
path=raw_input("Enter Path\n")
import os
folderList=os.listdir(path+'/')
cars={}
for folders in folderList:
    os.chdir(path+'/'+folders+'/')
    fileList=os.listdir(path+'/'+folders+'/')
    for files in fileList:
        with open(files,"r") as InputFile:        
            myfile = open(path+'/'+folders+'/'+files, "r")
            print("Extracting.."+path+'/'+folders+'/'+files)
            while(True):
                line=myfile.readline()
                if not line: myfile.close(); break
                lat=float(line.split(",")[2])
                lon=float(line.split(",")[3])
                carno=line.split(",")[0]
                try:
                    cars[carno][str([lat,lon])]+=1
                except KeyError:
                    try:
                        cars[carno][str([lat,lon])]=1
                    except KeyError:
                        cars[carno]={}
                        cars[carno][str([lat,lon])]=1
            myfile.close()
print "\n"
for i in cars:
    temp=""; max=0
    for j in cars[i]:
        if cars[i][j]>max: max=cars[i][j]; temp=str(j)
    print str(i)+" probably resides at: "+temp[1:len(temp)-1]+" as it has traced the point "+str(max)+" times."
