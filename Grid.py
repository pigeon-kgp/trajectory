import os
import numpy as np
import cv2
point1=[115.96198,39.75903]#test case
point2=[117.10539,40.11289]
def Grid(point1,point2):#point1 point2 are list
    path=raw_input("Enter Path\n")
    global OutputPath
    OutputPath=raw_input("Enter Output path\n")
    folderList=os.listdir(path+'/')
    
    lon=int(raw_input("Enter Columns : "))
    lat=int(raw_input("Enter Rows : "))
    
    loniterator=(point2[0]-point1[0])/lon
    latiterator=(point2[1]-point1[1])/lat

    os.chdir(OutputPath+'/')
    try:
        os.mkdir("Grid")
    except:
        print("Ho ho ho!")

    os.chdir("Grid")

    filePointerList={}
    grid={}

    for i in range(0,lat):
        for j in range(0,lon):
            filePointerList[str(i)+str(j)]=open(str(int(str(i))+1)+"x"+str(int(str(j))+1)+".txt",'a')
            grid[str(i)+str(j)]=[point1[0]+i*loniterator,point1[1]+j*latiterator]

    for folders in folderList:
        #os.chdir(path+'/'+folders+'/')
        fileList=os.listdir(path+'/'+folders+'/')
        try:
          for files in fileList:
              with open(path+'/'+folders+'/'+files,"rt") as InputFile:        
                #myfile = open(path+'/'+folders+'/'+files, "r")
                print("Extracting.."+path+'/'+folders+'/'+files)
                totalCost=0
                for line in InputFile:
                    totalCost+=1
                cost=0
                totalCost=float(totalCost)
		        #totalCost=float(totalCost)
                InputFile.seek(0)
                for lines in InputFile:
                    c=0
                    cost+=1
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
                    d=0
                    for i in range(0,lat):
                        for j in range(0,lon):
                            if(i==lat-1 and j==lon-1):
                                if(lonData>=grid[str(i)+str(j)][0]):
                                    if(latData>=grid[str(i)+str(j)][1]):
                                        key=str(i)+str(j)
                                        d=1
                            elif(j==lon-1):
                                if(lonData>=grid[str(i)+str(j)][0]):
                                    if(latData>=grid[str(i)+str(j)][1] and latData<grid[str(i+1)+str(j)][1]):
                                        key=str(i)+str(j)
                                        d=1
                            elif(i==lat-1):
                                if(lonData>=grid[str(i)+str(j)][0] and lonData<grid[str(i)+str(j+1)][0]):
                                    if(latData>=grid[str(i)+str(j)][1]):
                                        key=str(i)+str(j)
                                        d=1
                            else:
                                if(lonData>=grid[str(i)+str(j)][0] and lonData<grid[str(i+1)+str(j+1)][0]):
                                    if(latData>=grid[str(i)+str(j)][1] and latData<grid[str(i+1)+str(j+1)][1]):
                                        key=str(i)+str(j)
                                        d=1
                            #print(d)
                    cost=float(cost)
                    percent=float(cost/totalCost)*100
                    print("Completed......"+str(percent)+" %")
                            
                    if(d):
                        filePointerList[key].write(lines)
                print(files+".........complete.....")

        except:
              print "Some minor error occured."
def Assess():
    #1409,2008-02-02 13:33:45,116.34732,39.8881
    grno=raw_input("Which grid would you like to assess?: ")
    myfile=open(OutputPath+"/Grid/"+grno+".txt","r")
    dt=int(raw_input("Day?: "))
    sh=int(raw_input("Start hour?: "))
    eh=int(raw_input("End hour?: "))
    cars={}
    while(True):
        line=myfile.readline()
        if not line: break
        info=line.split(",")
        carno=info[0]
        day=int((info[1])[8:10])
        time=(info[1])[11:]; hr=int(time[0:2])
        time=int(time[0:2])*3600+int(time[3:5])*60+int(time[6:])
        if (hr>=sh and hr<eh and day==dt):
            try:
                if time<(cars[carno])[0]: (cars[carno])[0]=time
                if time>(cars[carno])[1]: (cars[carno])[1]=time
            except:
                cars[carno]=[time,time]
    print "Taxis present:"
    for i in cars: print i
    myfile.close()
    gpr=int(grno[0]); gpo=int(grno[2])
    inflow=[]; outflow=[]
    for i in xrange(gpr-1,gpr+2):
        for j in xrange(gpo-1,gpo+2):
            if (i==gpr and j==gpo): continue
            try:
                myfile=open(OutputPath+"/Grid/"+str(i)+"x"+str(j)+".txt","r")
            except: continue
            while(True):
                line=myfile.readline()
                if not line: break
                info=line.split(",")
                carno=info[0]
                day=int((info[1])[8:10])
                time=(info[1])[11:]; hr=int(time[0:2])
                time=int(time[0:2])*3600+int(time[3:5])*60+int(time[6:])
                if (hr>=sh and hr<eh and day==dt):
                    try:
                        if time<(cars[carno])[0]:
                            flag=1
                            for k in inflow:
                                if carno==k: flag=0; break
                            if flag==1: inflow.append(carno)
                        if time>(cars[carno])[1]:
                            flag=1
                            for k in outflow:
                                if carno==k: flag=0; break
                            if flag==1: outflow.append(carno)
                    except:
                        continue

    print "Inflow:"
    for i in inflow: print i
    print "Outflow:"
    for i in outflow: print i                


    




OutputPath="."
while(True):
    print "What would you like to do next?\n1) Create Grid\n2) Assess flow.\n3) Exit.\nPlease enter choice: "
    choice=int(raw_input())
    os.system("clear")
    if (choice==1): Grid(point1,point2)
    elif (choice==2): Assess()
    elif (choice==3): break
    else: print "Invalid choice."
