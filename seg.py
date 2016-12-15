import glob
import os
def timeonly(a_list):
    return a_list[1]
def seg(hours):
    time_out=0
    if (24%hours!=0): print("Hours can only be factors of 24."); return
    while(True):
        time_out+=hours
        parentlist=[]
        broken=0
        for i in range(1,15):
            loc="data/0"+str(i)+"/*"
            for file in glob.glob(loc):
                print ("Processing "+file)
                myfile = open(file, "r")
                while(True):
                    line = myfile.readline()
                    if not line:
                        myfile.close()
                        broken+=1
                        break
                    try:
                      for k in range(len(line)):
                          if (line[k]==","): break
                      date=line[k+1:k+11]
                      time=int(line[k+12:k+14])*3600+int(line[k+15:k+17])*60+int(line[k+18:k+20])+24*3600*(int(line[k+9:k+11])-2)
                    except:
                        print ("Some error has occurred. Ignoring error.")
                        continue
                    if (time>=3600*(time_out-hours) and time <=time_out*3600):   
                      parentlist.append([line,time,date])
                    if (time>=3600*time_out):
                        myfile.close()
                        break
        if (broken==14): break
        parentlist.sort(key=timeonly) 
        if (len(parentlist)>0):
          os.system("mkdir "+str((parentlist[0])[2]))
          time_print=(time_out)-(int(str((parentlist[0])[2])[8:10])-2)*24
          time_print=str(time_print-hours)+":00 - "+str(time_print)+":00"
          towrite=open(str ((parentlist[0])[2])+"/"+time_print+".txt","a")
          for i in parentlist:
            towrite.write(i[0])

n=int(input("Pl enter hour segments: "))
temp=open("pos.txt","w")
temp.close()
seg(n)
