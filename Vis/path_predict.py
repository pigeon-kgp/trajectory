import os
from copy import copy
source_org=raw_input("Enter source edge: ")
source=copy(source_org)
destin=raw_input("Enter destination edge: ")
while(1):
    flag=0
    try:
        f=open("tables/"+str(source),"r")
        while(1):
            line=f.readline()
            if not line: break
            if line.split(':')[0]==destin:
                now_dest=line.split(':')[1]
                flag=1
                break
    except: pass
    if flag==1:
        source=now_dest[1:].split('\n')[0]
        print("Just go to "+str(source))
        if source==destin: break
    else:
        f=open("temp_trip","w")
        str_to_write="<trips><trip id  = \"0\" depart=\"0.00\" from=\""+str(source)+"\" to =\""+str(destin)+"\" /> </trips>"
        f.write(str_to_write)
        f.close()
        try:
            f=open("tables/"+str(source),"a")
        except:
            f=open("tables/"+str(source),"w")
        try:
            os.system('duarouter --trip-files temp_trip --net-file sumo/map.net.xml --weight-files weights --output-file result_here.rou.xml ')
            result=open("result_here.rou.alt.xml","r")
            all_text=result.read()
            next_id=(all_text.split('edges'))[1].split(' ')[1]
            print ("Go to "+str(next_id))
            source=next_id[1:].split('\n')[0]
            if source==destin: break
            f.write(str(destin)+": "+str(next_id)+"\n")
        except: continue
