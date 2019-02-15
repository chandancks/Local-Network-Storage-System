#!/usr/bin/python36

import subprocess as sp
import os
import cgi
import cgitb,pymysql
cgitb.enable()

form=cgi.FieldStorage()
name=form.getvalue('user')
size=form.getvalue('size')
ip=form.getvalue('ip')
password=form.getvalue('password')

print("content-type:text/html\r\n\r\n")



#sending data into table.

db=pymysql.connect("localhost","root","Chandan@123","drive")
cur=db.cursor()


sql='INSERT INTO user VALUES ("{0}","{1}","{2}")'.format(name,password,ip)
cur.execute(sql)
db.commit()
"""
cur.execute("SELECT * FROM user")

rows=cur.fetchall()
for eachRow in rows:
        print (eachRow)
"""
db.close()







sp.getoutput("sudo lvcreate storage_sea --size +{0}G --name {1}".format(int(size),name))
sp.getoutput("sudo mkfs.ext4 /dev/storage_sea/{0}".format(name))
sp.getoutput("sudo mkdir /logical_mount/{0}".format(name))

a=sp.getstatusoutput("sudo sshpass -p redhat ssh -o stricthostkeychecking=no -l root 192.168.43.102 mount /dev/storage_sea/{0} /logical_mount/{1}".format(name,name))
sp.getoutput("sudo chmod ugo=rwx /logical_mount/{0}".format(name))

if a[0]==0:
	print("Storage allocated successfully. Please login to use the storage")
	print("<html><body><a href='logical_html.py'>Login!</a></body></html>")
else:
	print("Something went wrong")
print(a)
