import sys
filepath=sys.argv[1]
f = open(filepath+'/script1.py','w')
database_name="task2"
table_name="time"
column_name="time_then"
f.write("from pymongo import MongoClient\nclient = MongoClient()\ndb = client."+database_name+"\n")	#task2 is the database name
f.write("table = db."+table_name+"\n")	#time is the table name		
#f.write("print 'yipppie!! script 1 executed'")
'''time_then and index are the attributes to every row of data, they aren't initialised or anything in script1'''
f.close()
f = open(filepath+'/script2.py','w')
f.write("from datetime import datetime\n")
f.write("from pymongo import MongoClient\nclient = MongoClient()\ndb = client."+database_name+"\ntable = db."+table_name+"\n")
f.write("i=1\n")
f.write("for document in table.find():\n")
f.write("\ti+=1\n")
f.write("table.insert_one({'index':i,'"+column_name+"':datetime.strftime(datetime.now(),'%H:%M:%S')})\n")
f.close()
execfile(filepath+"/script1.py")
from crontab import CronTab
cronn=CronTab(user = True)
job=cronn.new("/usr/bin/python "+filepath+"/script2.py")
job.minute.every(10)
job.enable()
cronn.write()
#print "cronjob set"
