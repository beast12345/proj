#!/usr/bin/python

import cgi
import commands
import random
import time


print "Content-type:text/html"
print ""

data = cgi.FieldStorage()

lang = data.getvalue('lang')

if lang == "python":
	bport = random.random()
	fport = str(bport)[-4:]
	x = commands.getoutput("sudo docker run -itd --rm -p "+fport+":4200 paaaas")
	print x
	print fport
	print ("<meta http-equiv='Refresh' content='2; url=http://127.0.0.1:"+fport+"'>")
