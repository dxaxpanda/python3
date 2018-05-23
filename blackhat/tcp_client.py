#!/usr/bin/python

import socket as s
<<<<<<< HEAD
import random

target_host = "127.0.0.1"
target_port = 9999
aleatoire = random.random()
=======

target_host = "127.0.0.1"
target_port = 9999
>>>>>>> refs/remotes/origin/master

# Setup the socket 
client = s.socket(s.AF_INET, s.SOCK_STREAM)

# And now we are going to connect the client 
# Since TCP is a connection protocol
client.connect((target_host,target_port))


# Now that the connection is established. We are going to send some data...
<<<<<<< HEAD
#request = client.send("GET / HTTP/1.1\r\nHost: jeuxvideo.com\r\n\r\n")
request = client.send("Sending something.. Whello Horld! %s" % aleatoire)
=======
request = client.send("GET / HTTP/1.1\r\nHost: jeuxvideo.com\r\n\r\n")
>>>>>>> refs/remotes/origin/master

# In order to receive data use the recv command
response = client.recv(8192)

print "Printing the response from host {} and port {}...\n and the following response: \n\n {}".format(target_host, target_port, response)
