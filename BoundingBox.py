import os
import numpy as np
import cv2
from math import fabs
img = np.zeros((700, 700, 3), np.uint8)
cenx=ceny=no=0

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

                except:
                    print("Some error occured. Ignoring error.")
                    continue   
                if (latitude<700 and latitude>=0 and longitude<700 and longitude>=0):
                  img[longitude,latitude][0]+=10          
                  img[longitude,latitude][1]+=10
                  img[longitude,latitude][2]+=10
                  cenx+=latitude; ceny+=longitude; no+=1

def findout (cenx, ceny, l, b):
    count=0
    for x in xrange (cenx-l+1,cenx+l):
        for y in xrange (ceny-b+1, ceny+b):
            if (img[y,x][0]>0):
                count+=1
    return count

imgtemp= np.zeros((700, 700, 3), np.uint8)
def resetc(event,x,y,flags,param=None):
    global tempx; global tempy
    tempx=x; tempy=y
    if (event == cv2.EVENT_LBUTTONDOWN):
        for i in xrange(700):
            for j in xrange(700):
                imgtemp[i,j][0]=img[i,j][0]
                imgtemp[i,j][1]=img[i,j][1]
                imgtemp[i,j][2]=img[i,j][2]
        pts = np.array([[x+l,y+b],[x+l,y-b],[x-l,y-b],[x-l,y+b]], np.int32)
        pts = pts.reshape((-1,1,2))
        cv2.polylines(imgtemp,[pts],True,(0,0,255))

def lch(pos):
    global tempx; global tempy
    resetc(cv2.EVENT_LBUTTONDOWN,tempx,tempy,1000)

print("\nCreating map...\n\nOn the map use w,a,s,d to control the bounding box and +,-,>,< to adjust its size.\nHit space to reset the box and q to quit.")

cenx/=no; ceny/=no
l=2; b=2;num=0
while(True):
    num1=findout(cenx,ceny,l+2,b)
    num2=findout(cenx,ceny,l,b+2)
    if (fabs(num1-num)<10 and fabs(num2-num)<=10): break
    elif (num1>num2): l+=2; num=num1
    elif (num1<num2): b+=2; num=num2
    else: l+=2; b+=2; num=findout(cenx,ceny,l+2,b+2)
lorg=l;borg=b
resetc(cv2.EVENT_LBUTTONDOWN,cenx,ceny, 1000)
tempx=cenx;tempy=ceny
cv2.setMouseCallback('Map',resetc,param=None)  
cv2.createTrackbar("Length","Map",l,100,lch)
while(1):
    cv2.imshow("Map",imgtemp)
    flag=0
    c = cv2.waitKey(1)
    if( 'w' == chr(c & 255)):
        tempy-=10; flag=1
    if( 's' == chr(c & 255)):
        tempy+=10; flag=1
    if( 'a' == chr(c & 255)):
        tempx-=10; flag=1
    if( 'd' == chr(c & 255)):
         tempx+=10; flag=1
    if( ' ' == chr(c & 255)):
         tempx=cenx; tempy=ceny; l=lorg; b=borg; flag=1
    if( '+' == chr(c & 255)):
        b+=10; flag=1
    if( '-' == chr(c & 255) and b>10):
        b-=10; flag=1
    if( '>' == chr(c & 255)):
        l+=10; flag=1
    if( '<' == chr(c & 255) and l>10):
        l-=10; flag=1
    if (flag==1):
        resetc(cv2.EVENT_LBUTTONDOWN,tempx,tempy,1000)
    if( 'q' == chr(c & 255)):
        break
choice=raw_input("Would you like to save the data of the bounding box?")
if (choice.lower()[0]=="y"):
    name=raw_input("Pl. enter name of file without extension: ")
    path=raw_input("Where would you like to save it? ")
    os.chdir(path)
    f=open(name+".txt","w")
    f.write("Minimum: "+str(((tempx-l)/550.0)+115.95)+", "+str((((tempy-b)/550.0)+39.5))+"\nMaximum: "+str(((tempx+l)/550.0)+115.95)+", "+str(((tempy+b)/550.0)+39.5))