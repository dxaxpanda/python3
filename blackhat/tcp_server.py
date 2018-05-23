
import socket as s
import threading as t

bind_ip = "127.0.0.1"
bind_port = 9999

# TCP server object
server = s.socket(s.AF_INET, s.SOCK_STREAM)

# Sets the server bind
server.bind((bind_ip,bind_port))

# Make the server listenning for 10 incoming connection at best
server.listen(10)


print "[*] TCP Server listenning on %s:%d" % (bind_ip,bind_port)

# And now we are going to write how to handle the connections

def handle_conn(client_socket):

    # Print what the client sends
    request = client_socket.recv(1024)

    print "[*] Receiving this request... \n\n %s \n\n " % request

    # Sends a packet back for acknowledging the request
    client_socket.send("Request acknowlodged.")

    client_socket.close()


# And now we are going to listen forever

while True:

    client, addr = server.accept()

    print "[*] Showing all variables for debugging..."
   # print "[*] addr value is : %s " % addr
    print "[*] Client request incomming"
    for idx, value in enumerate(addr):
        print "[*] idx is %d with value %s" % (idx,value)
    print "[*] Accepted connection from : %s:%d" % (addr[0],addr[1])
    

    # handles incoming data

    handler = t.Thread(target=handle_conn,args=(client,))
    
    # Starts handler thread
    handler.start()
