import os
import numpy as np
import cv2
def Grid(point1,point2):
    path=raw_input("Enter Path\n")
    OutputPath=raw_input("Enter Output src\n")
    folderList=os.listdir(path+'/')
    lon,lat=int(raw_input())
    loniterator=(point2[0]-point1[0])/lon
    latiterator=(point2[1]-point1[1])/lat

    os.chdir(OutputPath+'/')
    os.mkdir("Grid")
    os.chdir("Grid")

    filePointerList={}
    grid={}

    for i in range(0,lat):
        for j in range(0,lon):
            filePointerList[str(i)+str(j)]=open(str(i)+"x"+str(j)+".txt",'a')
            grid[str(i)+str(j)]=[point1[0]+i*loniterator,point1[1]+j*latiterator]

    for folders in folderList:
        #os.chdir(path+'/'+folders+'/')
        fileList=os.listdir(path+'/'+folders+'/')
        for files in fileList:
            with open(files,"rt") as InputFile:        
                myfile = open(path+'/'+folders+'/'+files, "r")
                print("Extracting.."+path+'/'+folders+'/'+files)
                for lines in InputFile:
                    c=0
                    for i in range(len(lines)):
                        
                        if(line[i]==','):
                            c+=1
                        if(c==1):
                            lonBegin=i+2
                        if(c==2):
                            latBegin=i+2
                            lonEnd=i+1
                    latEnd=len(lines)-2

                    lonData=float(lines[lonBegin:lonEnd])
                    latData=float(lines[latBegin:latEnd])
                    
                    print(lonData,latData)
                    
                    for i in range(0,lat):
                        for j in range(0,lon):
                            if(grid[str(i)+str(j)]
                




                            
                        
                        
