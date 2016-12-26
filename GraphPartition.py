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
        if (hr>=sh and hr<eh and day>=sdt and day<=edt):
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
                if (hr>=sh and hr<eh and day>=sdt and day<=edt):
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
import os
from math import fabs
fileList=os.listdir(OutputPath+'/')
for files in fileList:
    with open(OutputPath+'/'+files,"rt") as InputFile:
        print("Extracting.."+OutputPath+'/'+files)
        Assess(sdt,edt,sh,eh,InputFile,files)
graph.sort(key=toret, reverse=True)
prevt=graph[0][1]
toplot={}
count=0
for i in graph:
    gst=int(i[0][0])
    gen=int(i[0][2])
    tr=int(i[1])
    for j in xrange(gst-1,gst+2):
        for k in xrange (gen-1,gen+2):
            for l in graph:
                if l[0]==str(j)+"x"+str(k) and fabs(l[1]-tr)<=1:
                    try:
                        toplot[count].append(str(j)+'x'+str(k))
                    except:
                        toplot[count]=[str(j)+'x'+str(k)]
                    graph.remove(l)
    count+=1

print "Low level regeions: "+str(toplot)
fname=raw_input("\nName of output file (avoid extension): ")
myfile=open(fname+".txt","w")
for i in toplot:
    for j in toplot[i]:
        myfile.write(str(i)+","+str(int(j[0])-1)+","+str(int(j[2])-1)+","+str(int(j[0]))+","+str(int(j[2]))+"\n")


"""
toplot={}
prevt=graph[0][1]
count=0
for i in graph:
    if i[1]==0:
        try:
            toplot[count+1].append(i[0])
        except:
            toplot[count+1]=[i[0]]
        continue
    if prevt-i[1]>1:
        count+=1
    try:
            toplot[count].append(i[0])
    except:
            toplot[count]=[i[0]]
    prevt=i[1]
"""
