#!/usr/bin/python36

print("content-type:text/html")
print("")

import subprocess as sp
import cgi
import cgitb
cgitb.enable()



file=cgi.FieldStorage()
ip=file.getvalue("ip")
name=file.getvalue("name")
size=file.getvalue("size")

#print("content-type:text/html\r\n\r\n")


sp.getoutput("sudo lvcreate --size +{0}G --name {1} storage_sea".format(int(size),name))

sp.getoutput("sudo mkfs.ext4 /dev/storage_sea/{0}".format(name))
sp.getoutput("sudo mkdir /logical_mount/{0}".format(name))
x=sp.getstatusoutput("sudo sshpass -p redhat ssh -o stricthostkeychecking=no -l root 192.168.43.102 mount /dev/storage_sea/{0} /logical_mount/{1}".format(name,name))
#sp.getoutput("sudo sshpass -p redhat ssh -o stricthostkeychecking=no -l root {0} mkdir /logical_mount/{1}".format(ip,name))

sp.getoutput("sudo echo -e '/logical_mount/{0} {1}(rw,no_root_squash)' >> /etc/exports".format(name,ip))
z=sp.getstatusoutput("sudo service nfs restart")

#y=sp.getstatusoutput("sudo sshpass -p redhat ssh -o stricthostkeychecking=no -l root {0} mount 192.168.43.102:/logical_mount/{1} /logical_mount/{2}".format(ip,name,name))
#print(x)
if x[0]==0 and z[0]==0:
	print("<script>alert('Storage Successfully alloted')</script>")
	print("<html><head>")
	print("<meta http-equiv='refresh' content='0;url=http://192.168.43.102/drive/files.html'/>")
	print("</head></html>")
else:
	print("Unsuccessful")


