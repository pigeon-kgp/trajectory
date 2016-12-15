import glob
import os
#1131,2008-02-02 13:30:49,116.45804,39.86973
latmin=180;lonmin=180;latmax=-180;lonmax=-180
for i in range(1,15):
    loc="data/0"+str(i)+"/*"
    for file in glob.glob(loc):
        print ("Processing "+file)
        myfile = open(file, "r")
        counter=0
        while(True):
            counter+=1
            line = myfile.readline()
            if not line:
                myfile.close()
                break
            count=0;com1=0;com2=0
            for i in range(len(line)):
                if (line[i]=="," ):
                    count+=1
                    if (count==2): com1=i
                    if (count==3): com2=i; break
            try:
                lat=float(line[com1+1:com2])
                lon=float(line[com2+1:])
            except:
                print("Some error occured. Ignoring error.")
                continue   
            if (lat==0 or lon==0): print(counter); break
            if (lat>latmax): latmax=lat
            if (lat<latmin): latmin=lat
            if (lon>lonmax): lonmax=lon
            if (lon<lonmin): lonmin=lon

print ("Minimum: "+latmin+", "+lonmin)
print ("Maximum: "+latmax+", "+lonmax)
choice=input("Would you like to save it to a file?")
if (choice.lower()[0]=="y"):
    name=input("Pl. enter name of file without extension: ")
    f=open(name+".txt","w")
    f.write("Minimum: "+latmin+", "+lonmin+"\nMaximum: "+latmax+", "+lonmax)