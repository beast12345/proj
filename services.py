#!/usr/bin/python

import cgi

print  "Content-type:text/html"
print  ""

data=cgi.FieldStorage()

service = data.getvalue('n')
	
if service == "ss" :
	print  "<a href = 'http://192.168.10.59/saas.html'>click to use saas"
	print  "</a>"	
elif service == "ps" :
	print  "<a href = 'http://192.168.10.59/paas.html'>click to use paas"
	print  "</a>"
elif service == "sts" :
	print  "<a href = 'http://192.168.10.59/staas.html'>click to use staas"
	print  "</a>"
elif service == "is" :
	print  "<a href = 'http://192.168.10.59/iaas.html'>click to use iaas"
	print  "</a>"
else:
	print "you din't select anything"
	print "</br>"
	print  "<a href = 'http://192.168.10.59/services.html'>click to go back"
	print  "</a>"

