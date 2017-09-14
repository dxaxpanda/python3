#!/usr/bin/env python2.7
import subprocess
import cgi
import sys
import logging
from StringIO import StringIO
from threading import Thread
import cgitb

cgitb.enable(logdir="log")

APPLE_API_URL = "https://api.push.apple.com/3/device"

form = cgi.FieldStorage(environ={'REQUEST_METHOD': 'POST'})

TOKEN = form.getvalue('token')
BUNDLE_ID = form.getvalue('bundle_id')
PAYLOAD = form.getvalue('message')
CERT_FILE = form.getvalue('certificat')

wfile.write("<html><body><h1>POST!</h1></body></html>")
print "Thanks your notification has been sent with following parameters :"
print "<p>TOKEN: %s</p>" % TOKEN
print "<p>BUNDLE ID: %s</p>" % BUNDLE_ID
print "<p>MESSAGE: %s</p>" % PAYLOAD
print "<p>CERTIFICAT: %s</p>" % CERT_FILE




with open ("../log.txt", "w") as f:
    f.write(TOKEN)
    f.write(BUNDLE_ID)
    f.write(PAYLOAD)
    f.write(CERT_FILE)

print "<TITLE>CGI script output</TITLE>"

