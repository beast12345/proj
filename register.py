#!/usr/bin/python

import cgi
import commands

print "Content-type:text/html"
print ""

data = cgi.FieldStorage()

username = data.getvalue('u')
password = data.getvalue('p')
email = data.getvalue('e')
contact = data.getvalue('c')

print "Registration Successful"
print "</br>"
print "username  "+username
print "</br>"
print "password  "+password
print "</br>"
print "email  "+email
print "</br>"
print "contact  "+contact
print "</br>"

print ("<meta http-equiv='Refresh' content='5; url=http://127.0.0.1/index.html'>")

