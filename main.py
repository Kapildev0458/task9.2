#!/usr/bin/python3

print("content-type: text/html")
print()

import cgi
import subprocess as sub
import os
a = cgi.FieldStorage()
yourChoice = a.getvalue('x')
imgName = a.getvalue('i')
osName = a.getvalue('name')
if yourChoice == "Configer yum":
	print("please wet a second...")
	s=sub.getstatusoutput("sudo yum install firefox")
	if s[0] == 0:
		print("  yum is already configered.")
	else:
		sub.getstatusoutput("sudo cp /root/yumconfi.repo /etc/yum.repos.d/yumsa.repo")

elif yourChoice == "Install Docker":
	sub.getstatusoutput("sudo cp /root/d.repo /etc/yum.repos.d/")
	s = sub.getstatusoutput("sudo yum install docker-ce --nobest -y")
	if s[0] == 0:
		print('docker is installed successfully')
	else:
		print('something want wrong')
elif yourChoice == "Download Docker image":
	sub.getstatusoutput("sudo systemctl start docker")
	print("wate few second your docker image is downloading...")
	s = sub.getstatusoutput("sudo docker pull {}".format(imgName))
	if s[0] == 0:
		print("your docker image is installed successfully")
	else:
		print('something want wrong.')

elif yourChoice == "Install Docker image":
	sub.getstatusoutput("sudo systemctl start docker")
	s = sub.getstatusoutput("sudo docker run -dit --name {} {}".format(osName,imgName))
	if s[0] == 0:
		print("os is install successfully, name {}".format(osName))
	else:
		print('something want wrong. Might be possiblity that, {} name is already exist'.format(osName))
				
elif yourChoice == "terminet docker image":
	sub.getstatusoutput("sudo systemctl start docker")
	s = sub.getstatusoutput("sudo docker rm {} -f".format(osName))
	if s[0] == 0:
		print("os is terminet successfully name {}".format(osName)) 
	else:
		print('something want wrong. Might be possiblity that, {} name is not exist'.format(osName))
			
elif yourChoice == "Create Master":
	s = sub.getstatusoutput("sudo cp /root/core /etc/hadoop/core-site.xml")
	b = sub.getstatusoutput("sudo cp /root/hdfs /etc/hadoop/hdfs-site.xml")
	if( s[0] == 0 and b[0] == 0):
		print("your master name node is created successfully")
	else:
		print('something want wrong. Might be possiblity that master is already configred')

elif yourChoice == "Create Slave":
	s = sub.getstatusoutput("sudo cp /root/coredata /etc/hadoop/core-site.xml")
	b = sub.getstatusoutput("sudo cp /root/hdfsdata /etc/hadoop/hdfs-site.xml")
	if( s[0] == 0 and b[0] == 0):	
		print("your slave or data node is created successfully")
	else:
		print('something want wrong. Might be possiblity that slave is already configred')

elif yourChoice == "Create Clint":
	s = sub.getstatusoutput("sudo cp /root/coreclint /etc/hadoop/core-site.xml")
	if s[0] == 0:
		print("your clint is created successfully")
	else:
		print('something want wrong. Might be possiblity that clint is already configred')

elif yourChoice == "Install httpd server":
	s = sub.getstatusoutput("sudo yum install httpd -y")
	if s[0] == 0:
		print("Httpd is installed")
	else:
		print('something want wrong')
				
elif yourChoice == "Start httpd Server":
	s = sub.getstatusoutput("sudo systemctl start httpd")
	if s[0] == 0:
		print("Httpd server is start")
	else:
		print('something want wrong')
