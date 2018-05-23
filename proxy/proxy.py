#### Simple tcp proxy


import sys
import threading
import socket
#import hexdump
import time

def usage():
    print("                                                                           ")
    print("************************ Python TCP Proxy *********************************")
    print("Usage: python3 ch2_tcpproxy_example.py 127.0.0.1 21 ftp.example.com 21 True")
    print("1st arg                                                   localhost address")
    print("2nd arg                                                      localhost port")
    print("3rd arg                                                  remotehost address")
    print("4th arg                                                         remote port")
    print("5th arg                                 receive from remote (True or False)")
    print("                                                                           ")
    sys.exit(0)

usage()


def server_loop(localhost, localport, remotehost, remoteport, receive_first):

    # create the server socket
    server_socket = socket.socket(socket.AF_INT, socket.SOCK_STREAM)

    # bind the server socket
    try:
        server_socket.bind((localhost,localport))
    except:
        print(f"[!] Error binding with {localhost}:      {server_socket.getsockname()[1]}")
        sys.exit(0)


    # listen to incoming conenctions
    server_socket.listen(5)
    print(f"[*] TCP proxy listening on {localhost}: {server_socket.getsockname()[1]}")


    # accept incoming connections and spawn a proxy thread with client socket

    while True:
        client_socket, addr = server_socket.accept()
        print(f"[==>] Incoming tcp connection from client: {addr[0]}:{addr[1]}")
        proxy_thread = threading.Thread(target=proxy_handler, args=( \
           client_socket, remotehost, remoteport, receive_first))

        proxy_thread.start()

def proxy_handler(client_socket, remotehost, remoteport, receive_first):

    # start a timer
    connectionTime = time.time()

    # helper function to receive the complete data buffer
    def receive
