import os
import numpy as np
import cv2
img = np.zeros((700, 700, 3), np.uint8)

folderList=os.listdir(path+'/')
for folders in folderList:
    os.chdir(path+'/'+folders+'/')
    fileList=os.listdir(path+'/'+folders+'/')
    for files in fileList:
        with open(files,"rt") as InputFile:        
            myfile = open(path+'/'+folders+'/'+files, "r")
            print("Extracting.."+path+'/'+folders+'/'+files)
            counter=0
            while(True):
                counter+=1
                line = myfile.readline()
                if not line:
                    myfile.close() 
                    break
                count=0;com1=0;com2=0
                for i in range(len(line)):
                    if (line[i]=="," ):
                        count+=1
                        if (count==2): com1=i
                        if (count==3): com2=i; break
                try:
                    lat=float(line[com1+1:com2])
                    lon=float(line[com2+1:])

                    latitude=int((lat-int(lat))*700)
                    longitude=int((lon-int(lon))*700)
                    #print("Merry Chritmas")

                except:
                    print("Some error occured. Ignoring error.")
                    continue   
                img[latitude,longitude][0]+=10          
                img[latitude,longitude][1]+=10
                img[latitude,longitude][2]+=10

                                      
cv2.imshow("image",img)
while(1):
    a=cv2.waitKey(1)
    if(a=='27'):
        break

