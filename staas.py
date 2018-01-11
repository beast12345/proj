#!/usr/bin/python

import cgi,cgitb
import commands
import os
import socket,random


cgitb.enable()
print "Content-type:text/html"
print ""

data = cgi.FieldStorage()

name = data.getvalue('n')
size = data.getvalue('s')
protocol = data.getvalue('prt')
typ = data.getvalue('type')
smbuser = data.getvalue('usr')
smbpwd = data.getvalue('pwd')

#only for nfs sharing


if typ == 'object' and protocol == 'nfs' :
	commands.getoutput("sudo lvcreate -V"+size+" --name "+name+" --thin /dev/myvg/pool1") 
	commands.getoutput("sudo mkfs.xfs /dev/myvg/"+name)
	commands.getoutput("sudo mkdir /var/www/html/"+name)
	commands.getoutput("sudo mount /dev/myvg/"+name+" /var/www/html/"+name)
	f = open("/etc/exports", 'a')
	f.write("/var/www/html/"+name+"  *(rw)\n")
	f.close()
	commands.getoutput("sudo exportfs -r")
	hn = socket.gethostname()
	ip = socket.gethostbyname(hn)
	commands.getoutput("sudo chmod 777 /var/www/html/"+name)
	ff = open("/var/www/html/"+name+"/"+name+".py",'w')
	ff.write("#!/usr/bin/python\n")
	ff.write("import commands\n")
	ff.write("commands.getoutput('mkdir /media/vianfs')\n")
	ff.write("commands.getoutput('mount "+ip+":/var/www/html/"+name+" /media/vianfs')\n")
	ff.close()
	commands.getoutput("sudo chmod +x /var/www/html/"+name+"/"+name+".py")
	x = commands.getoutput("sudo tar -cvf /var/www/html/"+name+"/"+name+".tar /var/www/html/"+name+"/"+name+".py")

elif typ == 'block' and protocol == 'nfs' :
	commands.getoutput("sudo lvcreate -V"+size+" --name "+name+" --thin /dev/myvg/pool1") 
        x = random.random()
	y = str(x)
	commands.getoutput("sudo chmod 777 /etc/tgt/targets.conf")
	ff = open("/etc/tgt/targets.conf", 'a')
	ff.write("<target "+y+":"+name+">\nbacking-store /dev/myvg/"+name+"\n</target>\n")
	ff.close()
	commands.getoutput("sudo systemctl restart tgtd") 
	commands.getoutput("sudo mkdir /var/www/html/"+name)
	hn = socket.gethostname()
	ip = socket.gethostbyname(hn)
	commands.getoutput("sudo chmod 777 /var/www/html/"+name)
	ff = open("/var/www/html/"+name+"/"+name+".py",'w')
	ff.write("#!/usr/bin/python\n")
	ff.write("import commands\n")
	ff.write('commands.getoutput("iscsiadm --mode discoverydb --type sendtargets --portal '+ip+' --discover")\n')
	ff.write('commands.getoutput("iscsiadm --mode node --targetname '+y+':'+name+' --portal '+ip+':3260 --login")\n')
	ff.close()
	commands.getoutput("sudo chmod +x /var/www/html/"+name+"/"+name+".py")
	x = commands.getoutput("sudo tar -cvf /var/www/html/"+name+"/"+name+".tar /var/www/html/"+name+"/"+name+".py")

#elif typ == 'object' and protocol == 'cifs':
		























