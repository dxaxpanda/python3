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


parsed = False
while not parsed:
    try:
        form = cgi.FieldStorage(environ={'REQUEST_METHOD': 'POST'})

        TOKEN = form.getvalue('token')
        BUNDLE_ID = form.getvalue('bundle_id')
        PAYLOAD = form.getvalue('message')
        CERT_FILE = form.getvalue('certificat')
        parsed = True
    except ValueError:
        print "Incorrect value entered, please try again"


if CERT_FILE == "Skores":
    CERT_FILE = '/usr/local/etc/ssl/myCertificateIphoneST.pem'
elif CERT_FILE == "FootEnDirect":
    CERT_FILE = '/usr/local/etc/ssl/myCertificateIphoneFED.pem'
elif CERT_FILE == "Hello":
    pass

def get_topic(name):
    if name == "SportyTrader":
        name = "/usr/local/etc/ssl/myCertificateIphoneST.pem"
    elif name == "FootEnDirect":
        name = "/usr/local/etc/ssl/myCertificateIphoneFED.pem"

    return name

CERTIFICAT = get_topic(CERT_FILE)

CURL_CMD = """/usr/local/bin/curl --verbose --data {}  --header \"apns-topic: {}\" --header \"apns-priority: 10\" --header \"method: POST\" --http2 --cert {} {}/{}""".format(PAYLOAD, BUNDLE_ID, CERTIFICAT, APPLE_API_URL, TOKEN)



#rootLogger = logging.getLogger()

logfile = open('log-apache.txt', 'w')


args = CURL_CMD.split()
#print "%s" % args

f2 = open("test.test.test", "w")
#process = subprocess.Popen(args, stdout=f2, stderr=f2, bufsize=1)
#process = subprocess.Popen(" ".join(args), shell=True, stdout=f2, stderr=f2, bufsize=1)
process = subprocess.Popen(" ".join(args), shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, bufsize=1)

#output = process.stdout.read()
for line in process.stdout:
    if line is True:
        print "<h3>The Notification was sent successfully ! </h3>"
        print "<h2>Thanks your notification has been sent with following parameters:</h2>"
        print "<p>TOKEN: %s</p>" % TOKEN
        print "<p>BUNDLE ID: %s</p>" % BUNDLE_ID
        print "<p>MESSAGE: \'%s\'</p>" % PAYLOAD
        print "<p>CERTIFICAT: %s</p>" % CERTIFICAT
        print "<p>COMMAND: %s</p>" % CURL_CMD
    else:
        print "<h3> An error occured while sending the token : \n %s </h3>" % line
        print "<h4> Please refer to the following table to know why. \n </h4>"
        #print "<p> See : https://developer.apple.com/library/content/documentation/NetworkingInternet/Conceptual/RemoteNotificationsPG/CommunicatingwithAPNs.html for more information on errors
        #print "<table style=\"width:%\">"
        with open ("../error_code.html", "r") as f:
            for line in f:
                print line


#with process.stdout, open(logfile, 'ab') as file:
 #       for line in iter(process.stdout.readline, b''):
   #         print line,
  #          file.write(line)
#process.wait()



print "</body></html>"
