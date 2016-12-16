import os
import numpy as np
import cv2
point1=[116.10041,88322]
point2=[117.10539,40.11289]
def Grid(point1,point2):#point1 point2 are list
    path=raw_input("Enter Path\n")
    OutputPath=raw_input("Enter Output src\n")
    folderList=os.listdir(path+'/')
    
    lon=int(raw_input())
    lat=int(raw_input())
    
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
            with open(path+'/'+folders+'/'+files,"rt") as InputFile:        
                #myfile = open(path+'/'+folders+'/'+files, "r")
                print("Extracting.."+path+'/'+folders+'/'+files)
                for lines in InputFile:
                    c=0
                    for i in range(len(lines)):
                        
                        if(lines[i]==','):
                            c+=1
                        if(c==1):
                            lonBegin=i+2
                        if(c==2):
                            latBegin=i+2
                            lonEnd=i+1
                    latEnd=len(lines)-2

                    lonData=float(lines[lonBegin:lonEnd])
                    latData=float(lines[latBegin:latEnd])
                    
                    #print(lonData,latData)
                    c=0
                    for i in range(0,lat-1):
                        for j in range(0,lon-1):
                            
                            if(lonData>=grid[str(i)+str(j)][0] and lonData<grid[str(i+1)+str(j+1)][0]):
                                if(latData>=grid[str(i)+str(j)][1] and latData<grid[str(i+1)+str(j+1)][1]):
                                    key=str(i)+str(j)
                                    c=1


                    if(c):
                        
                        filePointerList[key].write(lines)
Grid(point1,point2)
                




                            
                        
                        
