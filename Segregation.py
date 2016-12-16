import os
def timeonly(line):
     for k in range(len(line)):                    
                          if (line[k]==","):
                              break
     timehere=int(line[k+12:k+14])*3600+int(line[k+15:k+17])*60+int(line[k+18:k+20])+24*3600*(int(line[k+9:k+11])-2)
     return timehere
def seg(hours):
    
    path=raw_input("Enter Path\n")
    OutputPath=raw_input("Enter output path\n")
    OutputPath+='/'
    path+='/'
    folderList=os.listdir(path)
    time_out=0
    if (24%hours!=0): print("Hours can only be factors of 24."); return
    
    while(True):
        time_out+=hours
        parentlist=[]
        broken=0

        
        for folders in folderList:
            filePath=path+folders+'/'
            os.chdir(filePath)
            fileList=os.listdir(filePath)
            for file in fileList:
                print(filePath+file)
                #print ("Extracting.. "+path+file)
                myfile = open(filePath+file, "rt")
                while(True):
                    line = myfile.readline()
                    if not line:
                        myfile.close()
                        broken+=1
                        break
                    try:
                      time=timeonly(line)
                    except:
                       print ("Some error has occurred. Ignoring error.")
                       continue
                    if (time>=3600*(time_out-hours) and time <=time_out*3600):
                        parentlist.append(line)
                    if (time>=3600*time_out):
                        myfile.close()
                        break
        if (broken==14): 
            break
        parentlist.sort(key=timeonly) 
        if (len(parentlist)>0):
            os.chdir(OutputPath+'/')
            try:
                for k in range(len(parentlist[0])):
                    if (line[k]==","):
                              break
                datenow=line[k+1:k+11]
                os.mkdir(datenow)
            except:
                print("Directory already exists :-) !")
            
            time_print=(time_out)-(int(datenow[8:10])-2)*24
            time_print=str(time_print-hours)+":00 - "+str(time_print)+":00"
            towrite=open(OutputPath+'/'+datenow+"/"+time_print+".txt","a")
            for i in parentlist:   
                towrite.write(i[0])

n=int(raw_input("Pl enter hour segments: "))
temp=open("pos.txt","w")
temp.close()
seg(n)
