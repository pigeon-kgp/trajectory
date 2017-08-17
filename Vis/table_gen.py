import json
import os
# from xml.dom import minidom


dest_edges=[]
data={}
with open('out.json') as data_file:    
    data = json.load(data_file)

weight_file=open("weights","w")
weight_file.write("<meandata>\n  <interval begin=\"0\" end=\"360000\" id=\"whatever\">")
for edge in data:
    str_to_write="<edge id= \""+str(edge)+"\" traveltime=\""+str(data[edge]["traffic"]*data[edge]["distance"])+"\"/>\n"
    weight_file.write(str_to_write)
weight_file.write(" </interval>\n</meandata>\n")
weight_file.close()
total_edge=len(data)

while(1):
    ids=raw_input("Enter popular edge ids to keep in routing table (0 to stop): ")
    if ids!='0': dest_edges.append(ids)
    else: break

total_edge*=len(dest_edges)
count=0
for dest in dest_edges:
    for each in data:
        count+=1
        os.system('clear')
        print(str(count*100.0/total_edge)+" %  complete")
        if each==dest: continue
        start_edge=each
        end_edge=dest
        f=open("temp_trip","w")
        str_to_write="<trips><trip id  = \"0\" depart=\"0.00\" from=\""+str(start_edge)+"\" to =\""+str(end_edge)+"\" /> </trips>"
        f.write(str_to_write)
        f.close()
        try:
            f=open("tables/"+str(each),"a")
        except:
            f=open("tables/"+str(each),"w")
        try:
            os.system('duarouter --trip-files temp_trip --net-file sumo/map.net.xml --weight-files weights --output-file result_here.rou.xml ')
            result=open("result_here.rou.alt.xml","r")
            all_text=result.read()
            next_id=(all_text.split('edges'))[1].split(' ')[1]
            f.write(str(dest)+": "+str(next_id)+"\n")
        except: continue
        # xmldoc = minidom.parse('result_here.rou.xml')
        # junclist= xmldoc.getElementsByTagName('routes')
        # junclist[0].getElementsByTagName('vehicle')


        # exit(0)


