import os
import numpy as np
import cv2
from math import fabs
img = np.zeros((700, 700, 3), np.uint8)
cenx=ceny=no=0
#cv2.imshow("image",img)
#1131,2008-02-02 13:30:49,116.45804,39.86973
#latmin=180;lonmin=180;latmax=-180;lonmax=-18000, 3), np.uint8)
path=raw_input("Enter Path\n")
folderList=os.listdir(path+'/')
for folders in folderList:
    os.chdir(path+'/'+folders+'/')
    fileList=os.listdir(path+'/'+folders+'/')
    for files in fileList:
        with open(files,"rt") as InputFile:        
            myfile = open(path+'/'+folders+'/'+files, "r")
            print("Extracting.."+path+'/'+folders+'/'+files)
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

                    latitude=int((lat-115.95)*550.0)
                    longitude=int((lon-39.5)*550.0)
                    #print("Merry Chritmas")

                except:
                    print("Some error occured. Ignoring error.")
                    continue   
                if (latitude<700 and latitude>=0 and longitude<700 and longitude>=0):
                  #print str(latitude)+"  "+str(longitude)
                  img[longitude,latitude][0]+=10          
                  img[longitude,latitude][1]+=10
                  img[longitude,latitude][2]+=10
                  cenx+=latitude; ceny+=longitude; no+=1

         #   if (lat==0 or lon==0): print(counter); break
         #   if (lat>latmax): latmax=lat
         #   if (lat<latmin): latmin=lat
         #   if (lon>lonmax): lonmax=lon
         #   if (lon<lonmin): lonmin=lon

#print ("Minimum: "+latmin+", "+lonmin)
#print ("Maximum: "+latmax+", "+lonmax)
#choice=input("Would you like to save it to a file?")
#if (choice.lower()[0]=="y"):
#    name=input("Pl. enter name of file without extension: ")
#    f=open(name+".txt","w")
#    f.write("Minimum: "+latmin+", "+lonmin+"\nMaximum: "+latmax+", "+lonmax)

def findout (cenx, ceny, l, b):
    count=0
    for x in xrange (cenx-l+1,cenx+l):
        for y in xrange (ceny-b+1, ceny+b):
            if (img[y,x][0]>0):
                count+=1
    return count

imgtemp=img
def resetc(event,x,y,flags,param):
    if (event == cv2.EVENT_LBUTTONDOWN):
        imgtemp=img
        pts = np.array([[x+l,y+b],[x+l,y-b],[x-l,y-b],[x-l,y+b]], np.int32)
        pts = pts.reshape((-1,1,2))
        cv2.polylines(imgtemp,[pts],True,(0,0,255))

cenx/=no; ceny/=no
l=2; b=2;num=0
while(True):
    num1=findout(cenx,ceny,l+2,b)
    num2=findout(cenx,ceny,l,b+2)
    if (fabs(num1-num)<10 and fabs(num2-num)<=10): break
    elif (num1>num2): l+=2; num=num1
    elif (num1<num2): b+=2; num=num2
    else: l+=2; b+=2; num=findout(cenx,ceny,l+2,b+2)
resetc(cv2.EVENT_LBUTTONDOWN,cenx,ceny, 1000,0)
cv2.setMouseCallback('Map',resetc)       
cv2.imshow("Map",imgtemp)
while(1):
    a=cv2.waitKey(2)
    if(a==27):
      break

