import os
import sys

try:
	import httplib
except:
	import http.client as httplib

def netstat():

	conn = httplib.HTTPConnection("www.google.com", timeout=5)
	try:
		conn.request("HEAD","/")
		conn.close()
		return True
	except:
		conn.close()
		return False
