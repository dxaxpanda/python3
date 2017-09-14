#!/usr/bin/env python2.7

"""Python simple http server listening on port 8008."""


from BaseHTTPServer import BaseHTTPRequestHandler, HTTPServer
from CGIHTTPServer import CGIHTTPRequestHandler
from os import curdir, sep
import cgi
import urllib2
import subprocess
from sys import argv 


#global TOKEN
#global BUNDLE_ID
#global CERT_FILE
#global PAYLOAD

#TOKEN, BUNDLE_ID, CERT_FILE_PAYLOAD = '   '

#args = CURL_CMD.split()

#process = subprocess.Popen(args, shell=False, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
#stdout, stderr = process.communicate()


class S(CGIHTTPRequestHandler):
    def _set_headers(self):
        self.send_response(200)
        self.send_header('Content-type', 'text/html')
        self.end_headers()
        
    def do_GET(self):
        if self.path is "/":
            self.path = "/index.html"
        else:
            self.wfile.write("<html><body><h1>hello c'est moi!</h1></body></html>")
        
        try:
            sendReply = False
            if self.path.endswith(".html"):
                sendReply = True
        
            if sendReply is True:
                # Open file
                self._set_headers()
                f = open(curdir + sep + self.path)
                self.wfile.write(f.read())
                f.close()

            return


        except IOError:
            self.send_error(404, 'File Not Found: %s' % self.path)


    def do_HEAD(self):
        self._set_headers()
        
    def do_POST(self):
        # Handle posted data
            print "self.path"
            form = cgi.FieldStorage(
                    fp=self.rfile,
                    headers=self.headers,
                    environ={'REQUEST_METHOD':'POST',
                            'CONTENT_TYPE':self.headers['Content-Type'],
            })
            #r = ""
            #for key in form.keys():
            #    var = str(key)
            #    value = str(form.getvalue(var))
            #    r += "<p>" + var + ", "+ value + "</p>\n"
            #    print r
            #fields = "<p>"+ str(r) + "</p>"

            print "Your notification has been sent."
            self._set_headers()

            #data = dict(TOKEN=str(form.getvalue('token')),
            #            BUNDLE_ID=str(form.getvalue('bundle_id')),
            #            PAYLOAD=str(form.getvalue('message')),
            #            CERT_FILE=str(form.getvalue('certificat')))
            #self.wfile.write(data) 
            TOKEN = str(form.getvalue('token'))
            BUNDLE_ID = str(form.getvalue('bundle_id'))
            PAYLOAD = str(form.getvalue('message'))
            CERT_FILE = str(form.getvalue('certificat'))
            print "Thanks your notification has been sent with following parameters :"
            print "<p>TOKEN: %s</p>" % TOKEN
            print "<p>BUNDLE ID: %s</p>" % BUNDLE_ID
            print "<p>MESSAGE: %s</p>" % PAYLOAD
            print "<p>CERTIFICAT: %s</p>" % CERT_FILE
            


       # self._set_headers()
       # self.wfile.write("<html><body><h1>POST!</h1></body></html>")
    
def run(server_class=HTTPServer, handler_class=S, port=8008):
    server_address = ('', port)
    httpd_py = server_class(server_address, handler_class)
        
    print 'Starting HTTP Server on port %d...' % port
    httpd_py.serve_forever()
        

if __name__ == "__main__":

    if len(argv) == 2:
        try:
            run(port=int(argv[1]))
        except IOError  as e:
            print "%s. Can't listen on unallowed port. You need to specify a higher port." % e
    else:
        run()
        
