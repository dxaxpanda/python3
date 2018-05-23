#!/usr/bin/env python
 
import BaseHTTPServer
import CGIHTTPServer
import cgitb; cgitb.enable()  ## This line enables CGI error reporting
from sys import argv  
port = 8000

def run(port):
    server = BaseHTTPServer.HTTPServer
    handler = CGIHTTPServer.CGIHTTPRequestHandler
    server_address = ("", port)
    handler.cgi_directories = ["cgi-bin"]
   
    print 'Starting HTTP Server on port %d...' % port
    httpd = server(server_address, handler)
    httpd.serve_forever()



if __name__ == "__main__":
    if len(argv) == 2:
        try:
            run(port=int(argv[1]))
        except IOError  as e:
            print "%s. Can't listen on unallowed port. You need to specify a higher port." % e
    else:
        run()

