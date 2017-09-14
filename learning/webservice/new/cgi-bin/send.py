
#!/usr/local/bin/python
# -*- coding: UTF-8 -*-

import subprocess
import cgi
import sys
#import logging
#from StringIO import StringIO
#from threading import Thread
import cgitb


# Tell the browser how to render the text
print "Content-tpe: text/plain;charset=utf-8\n\n"
print "<html><body>"
cgitb.enable(logdir="log")

#cgi.test()
APPLE_API_URL = "https://api.push.apple.com/3/device"

form = cgi.FieldStorage(environ={'REQUEST_METHOD': 'POST'})

TOKEN = form.getvalue('token')
BUNDLE_ID = form.getvalue('bundle_id')
PAYLOAD = form.getvalue('message')
CERT_FILE = form.getvalue('certificat')

if CERT_FILE is "SportyTrader":
    CERT_FILE = myCertificateIphoneST.pem
elif CERT_FILE is "FootEnDirect":
    CERT_FILE = myCertificateIphoneFED.pem 
elif CERT_FILE is "Hello":
    pass


CURL_CMD = """/usr/local/bin/curl --verbose --data "{}" --header "apns-topic: {}" \
            --header "apns-priority: 10" --header "method: POST" --http2 \
            --cert {} {}/{}""".format(PAYLOAD, BUNDLE_ID, CERT_FILE,
            APPLE_API_URL, TOKEN)

print "<h2>Thanks your notification has been sent with following parameters:</h2>"
print "<p>TOKEN: %s</p>" % TOKEN
print "<p>BUNDLE ID: %s</p>" % BUNDLE_ID
print "<p>MESSAGE: %s</p>" % PAYLOAD
print "<p>CERTIFICAT: %s</p>" % CERT_FILE
print "<p>COMMAND: %s</p>" % CURL_CMD





with open ("../log.txt", "w") as f:
    f.write("CURL_COMMAND: "+CURL_CMD)
    f.write("TOKEN: "+TOKEN+"\n")
    f.write("Bundle ID : "+ BUNDLE_ID+"\n")
    f.write("Message : "+ PAYLOAD+"\n")
    f.write("Certificat File : "+ CERT_FILE+"\n")




#rootLogger = logging.getLogger()

logfile = open('log-apache.txt', 'w')


args = CURL_CMD.split()
f2 = open("test.test.test", "w")
process = subprocess.Popen(args, stdout=f2, stderr=f2, bufsize=1)
#with process.stdout, open(logfile, 'ab') as file:
 #       for line in iter(process.stdout.readline, b''):
   #         print line,
  #          file.write(line)
#process.wait()



print "</body></html>"
