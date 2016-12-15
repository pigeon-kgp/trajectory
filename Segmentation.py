import os,sys
c=0
def T(startTime,endTime,DateInput):
    
    tstartTime=startTime[0]*3600+startTime[1]*60+startTime[2]
    tendTime=endTime[0]*3600+endTime[1]*60+endTime[2]
    tDateInput=DateInput[0]+'-'+DateInput[1]+'-'+DateInput[2]

    outputfilename=str(startTime[0])+":"+str(startTime[1])+" - "+str(endTime[0])+":"+str(endTime[1])
    OutputFile=open(outputfilename+".txt","wt")
    #os.mkdir(dir)
    #os.chdir(dir)
    tpath=raw_input("Enter path of data\n")
    os.chdir(tpath+'/')
    folderList=os.listdir(tpath+'/')

    

    for folder in folderList:
        
        path=tpath+'/'+folder+"/"
        os.chdir(path)
        folderFiles=os.listdir(path)

        for files in folderFiles:
            print("Extracting.."+path+files+"    complete...........")          
            with open(files,"rt") as InputFile:
                
                for line in InputFile:
                    c=0
                    
                    for i in range(len(line)):
                        if(line[i]==','):
                            c=c+1
                            if(c==1):
                                posDateBeg=i+1
                            if(c==2):
                                posTimeEnd=i
                            if(c>2):
                                c=0
                        
                        if(line[i]==' '):
                            posDateEnd=i
                            posTimeBeg=i+1
                    date=line[posDateBeg:posDateEnd]
       
                    h=int(line[posTimeBeg:posTimeBeg+2])*3600
                    m=int(line[posTimeBeg+3:posTimeBeg+5])*60
                    s=int(line[posTimeEnd-2:posTimeEnd])
                    time=h+m+s
                    
        
        
        
                    if(tDateInput==date and time>tstartTime and time<tendTime):
                        OutputFile.write(line) 
        
                
                        
    return
#def EndTime(start,date):

#def Interval(date,start,IntervalDist):
 #   d=int(raw_input("ENter the intervals\n"))
    

    
def Temporal():
    
    print("Insert Date YYYY MM DD")
    date=[str(x) for x in raw_input().split()]

    folderName=date[0]+"-"+date[1]+"-"+date[2]
    
    flag=0
    folders=os.listdir(os.getcwd())
    for name in folders:
        if(folderName == name):
            flag=1      
    if(flag):
        os.chdir(folderName)
    else:
        os.mkdir(folderName)
        os.chdir(folderName)
    print("Enter start Time HH MM SS")
    start=[int(x) for x in raw_input().split()]
    
    print("EndTime HH MM SS")
    end=[int(x) for x in raw_input().split()]
    T(start,end,date)


    
    return
Temporal()

    




                                               
                           


