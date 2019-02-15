#!/usr/bin/python36

print("content-type:text/html\n")
print("")

import cgi
import os
import cgitb
from os import environ
cgitb.enable()


f=cgi.FieldStorage()
fileitem=f['userfile']
#print(fileitem)

user_id=""
if 'HTTP_COOKIE' in environ:
        cookies=environ['HTTP_COOKIE']
        cookies=cookies.split('; ')
        for cookie in cookies:
                cookie=cookie.split("=")
                if cookie[0] == "username":
                        user_id = cookie[1]

if fileitem.filename:
	name=os.path.basename(fileitem.filename)
	open("/logical_mount/"+user_id+"/"+name,"wb").write(fileitem.file.read())
	print("Uploaded Successfully")
	#print("<html><head>")
	#print("<script>alert('File Uploaded Successfully');</script>")
	#print("<meta http-equiv='refresh' content='0;url=http://192.168.43.102/drive/files.html'/>")
        #print("</head></html>") 
else:
	#print("<script>alert('File Uploading Unsuccessful');</script>")
	#print("<html><head>")
        #print("<meta http-equiv='refresh' content='0;url=http://192.168.43.102/drive/upload_file.html'/>")
        #print("</head></html>")
	print("Problem while uploading!!")
