import os
import numpy as np
import cv2
from math import fabs
point1=[115.96198,39.75903]#test case
point2=[117.10539,40.11289]
def Assess(sdt,edt,sh,eh,myfile, files):
    #1409,2008-02-02 13:33:45,116.34732,39.8881
    cars={}
    while(True):
        line=myfile.readline()
        if not line: break
        info=line.split(",")
        carno=info[0]
        day=int((info[1])[8:10])
        time=(info[1])[11:]; hr=int(time[0:2])
        time=int(time[0:2])*3600+int(time[3:5])*60+int(time[6:])
        if (hr>=sh and hr<eh and day>=sdt and day<edt):
            try:
                if time<(cars[carno])[0]: (cars[carno])[0]=time
                if time>(cars[carno])[1]: (cars[carno])[1]=time
            except:
                cars[carno]=[time,time]
    myfile.close()
    grno=str(files)
    gpr=int(grno[0]); gpo=int(grno[2])
    inflow=[]; outflow=[]
    for i in xrange(gpr-1,gpr+2):
        for j in xrange(gpo-1,gpo+2):
            if (i==gpr and j==gpo): continue
            try:
                myfile=open(OutputPath+"/"+str(i)+"x"+str(j)+".txt","r")
            except: continue
            while(True):
                line=myfile.readline()
                if not line: break
                info=line.split(",")
                carno=info[0]
                day=int((info[1])[8:10])
                time=(info[1])[11:]; hr=int(time[0:2])
                time=int(time[0:2])*3600+int(time[3:5])*60+int(time[6:])
                if (hr>=sh and hr<eh and day>=sdt and day<edt):
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

    graph.append([str(files)[:len(str(files))-4],int(fabs(len(inflow)-len(outflow)))])


    

def toret(abc):
    return abc[1]

graph=[]
OutputPath="./Grid"
sdt=int(raw_input("Start day?: "))
edt=int(raw_input("End day?: "))
sh=int(raw_input("Start hour?: "))
eh=int(raw_input("End hour?: "))
fileList=os.listdir(OutputPath+'/')
for files in fileList:
    with open(OutputPath+'/'+files,"rt") as InputFile:
        print("Extracting.."+OutputPath+'/'+files)
        Assess(sdt,edt,sh,eh,InputFile,files)
graph.sort(key=toret, reverse=True)
print graph