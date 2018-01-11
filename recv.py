#!/usr/bin/python

import cgi
import commands

print "Content-type:text/html"
print ""

data = cgi.FieldStorage()

user = data.getvalue('u')
password = data.getvalue('p')

if user == "root" and password == "redhat":
	print "<center><b>"
	print "access granted"
	print "</br>"
	print "</br>"
	print "<a href = 'http://127.0.0.1/services.html'>click to enjoy our services"
	print "</a>"
	print "</b></center>"
else:
	print "<center><b>"
	print "invalid username or password"
	print "</br>"
	print "</br>"
	print "<a href = 'http://127.0.0.1/index.html'>click here to go back to main page"
	print "</a>"
	print "</b></center>"
