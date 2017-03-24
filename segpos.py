from writepos import write, auth
thr=float(raw_input("Enter threshold (recommended 0.01) : "))
auth()
path=raw_input("Enter full input path (root directory of the files) : ")
#thr=0.001
#path="/home/ss/Dropbox/Wriju/Codes/trajectory/data"
import os
import psycopg2
os.chdir(path)
counter=0
'''
def write(taxino,lat,lon,starttime,endtime,count):
   print(taxino,lat,lon,starttime,endtime,count)
   global counter
   pint counter
'''  
 
#from writepos import write 
taxi={}
folderlist=os.listdir(os.getcwd())
totnum=0
for folder in folderlist:
  os.chdir(path+"/"+folder)
  filelist=os.listdir(os.getcwd())
  for files in filelist:
    totnum+=1
    
numnow=0
prec=1
precision=2
for folder in folderlist:
  os.chdir(path+"/"+folder)
  filelist=os.listdir(os.getcwd())
  for files in filelist:
    os.system("clear")
    print "Scanned file(s) "+str(numnow)+" of "+str(totnum)+"."
    print "% complete: "+str(numnow*100/totnum)
    numnow+=1
    f=open(files,"r")
    pumbalines=0
    while(1):
      line=f.readline()
      pumbalines+=1
      if not line: break
      data=line.split(",")
      dates=data[1].split()
      date=dates[0].split("-")
      time=dates[1].split(":")
      day, month, year =int(date[2]), int(date[1]), int(date[0])
      hr, mins, sec = int(time[0]), int(time[1]), int(time[0])
      lat=float(data[2])
      lon=float(data[3])
      if prec:	precision=len(str(lat).split(".")[1]); prec=0
      taxino=int(data[0])
      templat=0; templon=0
      try:
      	count=len(taxi[taxino])-1
      	#print("count changed   : "+str(count))
      except:
      	#print("except")
      	taxi[taxino]=[]
      	taxi[taxino]=[[day,month,year,hr,mins,sec],lat,lon]
      	count=1
      try:
      	i=1
        while(1):
           try:
      		templat+=taxi[taxino][i]
      		templon+=taxi[taxino][i+1]
      		i+=2
      	   except: 
      	   	count=(len(taxi[taxino])-1)/2
      	   	break
      	#print("try")
      	dist=(((templat/count)-lat)**2)+(((templon/count)-lon)**2)
      	#print(str(templat/count)+"  "+str(templon/count)+" "+str(lat)+" "+str(lon))
      	#print "dist: "+str(dist)
      	if (dist<thr**2):
      		taxi[taxino].append(lat)
      		taxi[taxino].append(lon)
      		#print("if")
      	else:
      		write(taxino,(templat+lat)/count,(templon+lon)/count, taxi[taxino][0],[day,month,year,hr,mins,sec],count,precision)
      		counter+=1
      		taxi[taxino]=[[day,month,year,hr,mins,sec],lat,lon]
      		#print("else")     		
      except Exception, e:
      	print e
      	taxi[taxino]=[]
      	taxi[taxino]=[[day,month,year,hr,mins,sec],lat,lon]
      	#print("oexceptf")
  #os.chdir(path)
print("This algorithmn successfully compressed the raw data to "+str(counter)+" from "+str(pumbalines)+" units.\n% compression: "+str(float(pumbalines-counter)*100/pumbalines))
     
