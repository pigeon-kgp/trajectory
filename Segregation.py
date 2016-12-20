import os
def timeonly(line):
     for k in range(len(line)):
                          if (line[k]==","):
                              break
     timehere=int(line[k+12:k+14])*3600+int(line[k+15:k+17])*60+int(line[k+18:k+20])+24*3600*(int(line[k+9:k+11])-2)
     return timehere
def seg(hours):
    countp=0
    path=raw_input("Enter Path\n")
    OutputPath=raw_input("Enter output path\n")
    OutputPath+='/'
    path+='/'
    folderList=os.listdir(path)
    time_out=0; rem=0
    if (24%hours!=0): print("Hours can only be factors of 24."); return
    
    while(True):
        time_out+=hours
        parentlist=[]
        brakeflag=1
        countp+=1

        
        for folders in folderList:
            filePath=path+folders+'/'
            os.chdir(filePath)
            fileList=os.listdir(filePath)
            for file in fileList:
                os.system("clear")
                print (str(((countp)*100)/countmax)+"% complete. ")
                print("Extracting "+filePath+file+". ")
                try:
                  myfile = open(filePath+"/"+file, "rt")
                except IOError:
                    ech="y"
                    if (rem==0):
                      print ("Well, there seems to be a folder here instead of a file. Skip it and continue?")
                      ech=raw_input()
                    if (ech.lower()[0]!="y"):
                      os._exit(0)
                    else:
                        if (rem==0):
                          print ("Remember choice?")
                          er=raw_input()
                          if (er.lower()[0]=="y"):
                              rem=1
                        continue
                flocate.seek(0)
                fpos=0; flag=1
                fposinline=0
                while(True):
                    fpos=flocate.tell()
                    fline=flocate.readline()
                    if not fline: flag=0; break
                    if (str(file) in fline):
                        for i in xrange(len(fline)):
                            if(fline[i]==" "):
                                fposinline=int(fline[i+1:])
                                break
                        break
                if (flag==1):
                    myfile.seek(fposinline)
                else:
                    myfile.seek(0)
                while(True):
                    pos=myfile.tell()
                    line = myfile.readline()
                    if not line:
                        myfile.close()
                        break
                    try:
                      time=timeonly(line)
                    except:
                       print ("Some error has occurred. Ignoring error.")
                       continue
                    if (time>=3600*(time_out-hours) and time <=time_out*3600):
                        parentlist.append(line)
                    if (time>=3600*time_out):
                        brakeflag=0
                        myfile.close()
                        flocate.seek(fpos)
                        wrstr=str(file)+" "+str(pos)
                        for sp in xrange(len(wrstr),30): wrstr+=" "
                        flocate.write(wrstr+"\n")
                        break
        if (brakeflag==1): 
            break
        parentlist.sort(key=timeonly) 
        if (len(parentlist)>0):
            os.chdir(OutputPath+'/')
            try:
                for k in range(len(parentlist[0])):
                    if ((parentlist[0])[k]==","):
                              break
                datenow=(parentlist[0])[k+1:k+11]
                os.mkdir(datenow)
            except:
                print("Directory already exists :-) !")
            
            time_print=(time_out)-(int(datenow[8:10])-2)*24
            time_print=str(time_print-hours)+":00 - "+str(time_print)+":00"
            towrite=open(OutputPath+'/'+datenow+"/"+time_print+".txt","a")
            for i in parentlist:
                towrite.write(i)

n=int(raw_input("Pl enter hour segments: "))
countmax=24/n * 7
flocate=open("pos.txt","w")
flocate.close()
flocate=open("pos.txt","r+")
seg(n)
os.system("clear")
print "100% complete"
print("\nDone!")
flocate.close()