#!/usr/bin/python3

''' Basic tcp proxy '''

import sys
import socket as sock
import threading


def server_loop(local_h, local_p, remote_h, remote_p, receive_first):
    ''' basic function handling the server loop '''

    server = sock.socket(sock.AF_INET, sock.SOCK_STREAM)

    try:
        server.bind((local_h,local_p))

    except Exception as e:
        print("[*] Failed to listen on %s:%d" % (local_h,local_p))
        print("[*]" + e)
        sys.exit(1)

    print("[*] Listening on %s:%d" % (local_h,local_p))

    server.listen(5) # Accept connections with a max of 5

    while True:
        ''' Start the loop '''
        client_socket, addr = server.accept() # returns socket obj and remote addr

        # Print local connection info addr[0] is ip and addr[1] is port
        print("[==>] Received incoming connection from %s:%d" % (addr[0],addr[1]))
    
        # Start thread to talk to the remote host

        proxy_thread = threading.Thread(target=proxy_handler,
                args=(client_socket,remote_h,remote_p,receive_first))
        
        proxy_thread.start()
    


def proxy_handler(client_socket,remote_h,remote_p,receive_first):
    ''' handle the proxy behaviours '''
    # connect to the remote host

    remote_socket = sock.socket(sock.AF_INET,sock.SOCK_STREAM)

    remote_socket.connect((remote_h,remote_p))

    # receive data if necessary

    if receive_first:

        remote_buffer = receive_from(remote_socket)
        hexdump(remote_buffer)

        # send the data to our response handler function
        remote_buffer = response_handler(remote_buffer)

        # send data to local client if needed
        if len(remote_buffer):
            print("[<==] Sending %d bytes to localhost." % len(remote_buffer))

<<<<<<< HEAD
            client_socket.send(remote_buffer)
=======
            client_socket.send(bytes(remote_buffer, 'utf-8'))
>>>>>>> 01053f0098ddeea2e9cc314da2ee3ec09f01f26f

        # Starts to loop now and read from local
        # sending to remote then sending to local, 
        # rinse and repeat

        while True:

            # read from local 
            local_buffer = receive_from(client_socket)

            if len(local_buffer):

                print("[==>] Received %d bytes from localhost." % len(local_buffer))
                hexdump(local_buffer)

                # send it to our request handler

                local_buffer = request_handler(local_buffer)

                # Then send the data to remote host
<<<<<<< HEAD
                remote_socket.send(local_buffer)
=======
                remote_socket.send(bytes(local_buffer, 'utf-8'))
>>>>>>> 01053f0098ddeea2e9cc314da2ee3ec09f01f26f
                print("[==>] Sent local data to remote.")

            # Receive back the reponse
            remote_buffer = receive_from(remote_socket)

            if len(remote_buffer):
                print("[<==] Received %d bytes from remote." % len(remote_buffer))
                hexdump(remote_buffer)

                # Send to the response handler
                remote_buffer = response_handler(remote_buffer)

                # Send the response to the local socket
<<<<<<< HEAD
                client_socket.send(remote_buffer)
=======
                client_socket.send(bytes(remote_buffer, 'utf-8'))
>>>>>>> 01053f0098ddeea2e9cc314da2ee3ec09f01f26f

                print("[<==] Sent to localhost.")

            # If there are no more data on either side, close the connections
            if not len(local_buffer) or not len(remote_buffer):
                client_socket.close()
                remote_socket.close()
                print("[*] No more data. Closing connections.")

                break




def receive_from(connection):

    ''' handle the received data in a buffer '''

    # initialize the empty buffer

    buf = ""

    # Set a 2 second timeout to the socket connection

    connection.settimeout(30)

    try:
        # keep reading into the buffer until there's no more data 
        # or timeout
        while True:

            data = connection.recv(4096)

            # if no data is sent or timeout we break the connection

            if not data: 
                break

            # add our data to the buffer
            buf += data.decode()

    except Exception as e:
        raise e
        #print("[*] An exception occured:\n", e)
        #pass
    
    return buf


def hexdump(src, length=16):
    ''' Hex dumping function which dumps an hex value of the src  
        the comments here:
        # http://code.activestate.com/recipes/142812-hex-dumper/ 
    '''
    result = []
    digits = 4 if isinstance(src,str) else 2
    for i in range(0, len(src), length):
        s = src[i:i+length]
<<<<<<< HEAD
        hexa = ' '.join(["%0*X" % (digits, ord(x))  for x in s]).encode('UTF-8')
        text = ''.join([x if 0x20 <= ord(x) < 0x7F else '.'.encode('UTF') for x in s]).encode()
        print(text)
        result.append( "%04X   %-*s   %s" % (i, length*(digits + 1), hexa, text))
    
    print(b'\n'.join(result))

=======
        print("src: %s\n" % (src))
        print("s: %s\n" % (s))
        print("i: %s\n" % (i))
        hexa = bytes(' '.join(["%0*X" % (digits, ord(x))  for x in s]), 'utf-8')
        text = bytes(''.join([x if 0x20 <= ord(x) < 0x7F else '.' for x in s]), 'utf-8')
        result.append(bytes("%04X   %-*s   %s" % (i, length*(digits + 1), hexa, text), 'utf-8'))
    print(b"\n ".join(result))
>>>>>>> 01053f0098ddeea2e9cc314da2ee3ec09f01f26f

    
def request_handler(buffer):
    ''' This method performs the request packets  modification / redirection '''

    return buffer

def response_handler(buffer):
    ''' This method performs the response packets modification / redirection '''

    return buffer


def main():

    # basic command-line parsing
    # Check wether 5 arguments are passed
    
    if len(sys.argv[1:]) != 5:
        print("[*] Usage : tcp_proxy.py [localhost] [localport] [remotehost] [remoteport] [receive_first => True or False]")
        print("Example: ./tcp_proxy.py 127.0.0.1 8080 10.10.10.20 8080 True")
        sys.exit(0)

    # setup local listening params
    local_h = sys.argv[1]
    local_p = int(sys.argv[2])

    # setup remote target params
    remote_h = sys.argv[3]
    remote_p = int(sys.argv[4])

    # Ensure the proxy makes connection and receives data before sending to the remote_host
    receive_first = sys.argv[5]

    if "True" in receive_first:
        receive_first = True
    else:
        receive_frist = False


    # Starts the server loop

    server_loop(local_h,local_p,remote_h,remote_p,receive_first)



if __name__ == '__main__':
    
    main()

