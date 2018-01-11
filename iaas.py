#!/usr/bin/env python

import cgi
import commands
import socket
import time
import random


print "Content-type:text/html"
print ""

data = cgi.FieldStorage()

name = data.getvalue('n')
password = data.getvalue('p')
port = data.getvalue('port')
os = data.getvalue('os')
ram = data.getvalue('ram')
hdd = data.getvalue('hdd')
cores = data.getvalue('cores')

#print name+password+port+os+ram+hdd+cores
hn = socket.gethostname()
ip = socket.gethostbyname(hn)

x=commands.getoutput("sudo websockify -D --web=/usr/share/novnc 8888 "+ip+":"+port)
print x


if hdd == "0":
	if os == "windows 7":
		commands.getoutput("sudo virt-install --cdrom /images/Windows_7_Ultimate_Activated.iso --ram "+ram+" --vcpu "+cores+" --nodisk --name my"+name+" --graphics vnc,listen="+ip+",port="+port+",password="+password)
		
	elif os == "ubuntu":
		commands.getoutput("sudo virt-install --cdrom /images/ubuntu-16.04-beta2-desktop-amd64.iso --ram "+ram+" --vcpu "+cores+" --nodisk --name my"+name+" --graphics vnc,listen="+ip+",port="+port+",password="+password)
	elif os == "kali linux":
		commands.getoutput("sudo virt-install --cdrom /images/kali-linux-2.0-amd64.iso --ram "+ram+" --vcpu "+cores+" --nodisk --name my"+name+" --graphics vnc,listen="+ip+",port="+port+",password="+password)

else:
	if os == "windows 7":
		commands.getoutput("sudo qemu-img create -f qcow2 -b /var/lib/libvirt/images/windows7.qcow2 /var/lib/libvirt/images/"+name+".qcow2")
		commands.getoutput("sudo virt-install --name os"+name+" --ram "+ram+" --vcpu "+cores+" --disk path=/var/lib/libvirt/images/"+name+".qcow2 --import --graphics vnc,listen="+ip+",port="+port+",password="+password)

	elif os == "ubuntu":
		commands.getoutput("sudo qemu-img create -f qcow2 -b /var/lib/libvirt/images/myubuntu.qcow2 /var/lib/libvirt/images/"+name+".qcow2")
		commands.getoutput("sudo virt-install --name os"+name+" --ram "+ram+" --vcpu "+cores+" --disk path=/var/lib/libvirt/images/"+name+".qcow2 --import --graphics vnc,listen="+ip+",port="+port+",password="+password)

	elif os == "kali linux":
		commands.getoutput("sudo qemu-img create -f qcow2 -b /var/lib/libvirt/images/kali-linux2.0.qcow2 /var/lib/libvirt/images/"+name+".qcow2")
		commands.getoutput("sudo virt-install --name os"+name+" --ram "+ram+" --vcpu "+cores+" --disk path=/var/lib/libvirt/images/"+name+".qcow2 --import --graphics vnc,listen="+ip+",port="+port+",password="+password)


