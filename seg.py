import glob
import os
#366,2008-02-02 13:30:48,116.45353,39.90732
#6656,2008-02-02 13:38:10,116.36422,39.95658
def timeonly(a_list):
    return a_list[1]
def seg(hours):
    time=0
    if (24%hours!=0): print("Hours can only be factors of 24."); return
    while(True):
        time+=hours
        parentlist=[]
        broken=0
        for i in range(1,15):
            loc="data/0"+str(i)+"/*"
            for file in glob.glob(loc):
                print ("Processing "+file+" located in "+loc)
                myfile = open(file, "r")
                flocate=open("pos.txt","r")
                currpos=0
                while(True):
                    linehere=flocate.readline()
                    if not linehere: break
                    if (linehere.find(str(file))):
                      for j in range(len(linehere)):
                          if (linehere[j]==" "):  currpos=int(linehere[j+1:])
                      break
                flocate.close()
                myfile.seek(currpos)
                lines = myfile.readlines()
                if not lines:
                    myfile.close()
                    broken+=1
                    continue
                for line in lines:
                    if (line[3]==","):
                        date=line[4:14]
                        time=int(line[15:17])*3600+int(line[18:20])*60+int(line[21:23])+24*3600*(int(line[12:14])-2)
                    else:
                         date=line[5:15]
                         time=int(line[16:18])*3600+int(line[19:21])*60+int(line[22:24])+24*3600*(int(line[13:15])-2)                       
                    parentlist.append([line,time,date])
                    if (time>=3600*hours):
                        pos=myfile.tell()
                        myfile.close()
                        myfile=open("pos.txt","r+")
                        while(True):
                            currpos=myfile.tell()
                            linehere=myfile.readline()
                            if not linehere: break
                            if (linehere.find(str(file))):
                                break
                        myfile.seek(currpos)
                        myfile.write(str(file)+": "+str(pos)+"\n")
                        myfile.close()
                        break
        if (broken==14): break
        parentlist.sort(key=timeonly) 
        os.system("mkdir "+(parentlist[0])[2])
        os.system("cd "+(parentlist[0])[2])
        os.system("cd ../")
        towrite=file((parentlist[0])[2]+"/"+time,"a")
        for i in parentlist:
            towrite.write(i[0]+"\n")

n=int(input("Pl enter hour segments: "))
temp=open("pos.txt","w")
temp.close()
seg(n)