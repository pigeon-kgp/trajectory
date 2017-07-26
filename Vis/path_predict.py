import os
from copy import copy
source_org=raw_input("Enter source edge: ")
source=copy(source_org)
destin=raw_input("Enter destination edge: ")
foo=open("/home/ubuntu/Desktop/trajectory_clone/Vis/out_path","w")
foo.write(str(source)+"\n")
while(1):
    flag=0
    try:
        f=open("/home/ubuntu/Desktop/trajectory_clone/Vis/tables/"+str(source),"r")
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
        foo=open("/home/ubuntu/Desktop/trajectory_clone/Vis/out_path","a")
        foo.write(str(source)+"\n")
        if source==destin: break
    else:
        f=open("temp_trip","w")
        str_to_write="<trips><trip id  = \"0\" depart=\"0.00\" from=\""+str(source.split('\"')[0])+"\" to =\""+str(destin.split('\"')[0])+"\" /> </trips>"
        f.write(str_to_write)
        try:
            f=open("/home/ubuntu/Desktop/trajectory_clone/Vis/tables/"+str(source.split('\"')[0]),"a")
        except:
            f=open("/home/ubuntu/Desktop/trajectory_clone/Vis/tables/"+str(source.split('\"')[0]),"w")
        os.system('duarouter --trip-files temp_trip --net-file /home/ubuntu/Desktop/trajectory_clone/Vis/sumo/map.net.xml --weight-files /home/ubuntu/Desktop/trajectory_clone/Vis/weights --output-file /home/ubuntu/Desktop/trajectory_clone/Vis/result_here.rou.xml ')
        result=open("/home/ubuntu/Desktop/trajectory_clone/Vis/result_here.rou.alt.xml","r")
        all_text=result.read()
        next_id=(all_text.split('edges'))[1].split(' ')[1]
        print ("Go to "+str(next_id.split('\"')[0]))
        foo=open("/home/ubuntu/Desktop/trajectory_clone/Vis/out_path","a")
        foo.write(str(next_id.split('\"')[0])+"\n")
        source=next_id.split('\"')[0].split('\n')[0]
        if source==destin: break
        f.write(str(destin.split('\"')[0])+": "+str(next_id.split('\"')[0])+"\n")
