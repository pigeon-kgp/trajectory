#Pretty print as csv day wise only for stay points.
path=raw_input("Enter full input path (root directory of the files) : ")
print("Output would be stored in "+path+"/../csv")
dbs=raw_input("Enter database name:  (trajectory_thres) ")
usr=raw_input("Enter user name : (ubuntu) ")
import getpass
print("Enter password : (lion) ")
passw=getpass.getpass()

import os
import psycopg2

db_con = psycopg2.connect(database=dbs, user=usr, password=passw, host="127.0.0.1", port="5432")
cursor = db_con.cursor()
cursor.execute("ROLLBACK")

firstdate=0
os.chdir(path)
folderlist=os.listdir(os.getcwd())
for folder in folderlist:
  firstdate+=1
  os.chdir(path+"/"+folder)
  filelist=os.listdir(os.getcwd())
  for files in filelist:
    f=open(path+"/../csv/"+folder+"-"+files.split('.')[0]+".csv", "w")
    f.write("name,latitude,longitude\n")
    #os.system("touch "+path+"/../csv/"+folder+"-"+files.split('.')[0]+".csv")
    #statement="copy (select * from a"+files.split('.')[0]+" where type=\'SP\') to \'"+path+"/../csv/"+folder+"-"+files.split('.')[0]+".csv\' with csv delimiter \',\'\n"
    #statement="copy_to (select * from a"+files.split('.')[0]+" where type=\'SP\') to STDOUT with csv delimiter \',\'\n"
    statement="select * from a"+files.split('.')[0]+" where type='SP';"
    print statement
    try:
	    cursor.execute(statement)
	    a = cursor.fetchall()
	    print "Processing"+files
	    for each in a:
		f.write(str(each[0])+","+str(each[2])+","+str(each[3])+"\n")
    except: pass
