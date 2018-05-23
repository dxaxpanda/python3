#!/usr/bin/python
'''
netcat python

Usage:
  netcat_python.py  --target HOST --port PORT [ --listen ] [ --command ]
  netcat_python.py [ --listen | --command | --upload DEST | --execute FILE ]
  netcat_python.py -h | --help 
  netcat_python.py --version

Options:
  -h, --help             Show this screen.
  -v, --version          Show version.
  -t, --target            Targeted host.
  -p, --port             Targeted port.
  -l, --listen           Start listen mode.
  -e, --execute          Execute a given file upon receiving a connection.
  -c, --command          Start a shell.
  -u, --upload           Upload a file and write to [destination]
'''

import sys
import socket
import getopt
import threading 
import subprocess
from docopt import docopt



def client_sender(buf):

    target = str(args['HOST'])
    port = int(args['PORT'])

# init client socket
    
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as client:

        try:
        # try to connect to the target
            client.connect((target,port))
        
        # send data only in some in buffer
            
            if len(buf):
                client.send(buf)
        
            while True:
            
            # handle the data response 
                recv_length = 1
                response = ""
            
                while recv_len:
                    data = client.recv(4096)
                    recv_length = len(data)
                    response += data
                
                # stop if length is to high
                    if recv_length < 4096:
                        break

                    print("[*] This is the received data: {}".format(response))

             # wait for any more input
            buf = b'input("")'
            buf+= "\n"

            # send the remaining data
            client.send(buf)

        except Exception as e:
            print("[*] Exception occured. EXITING...\r\n %s" % e)

            # close the connection
            client.close()


def server_loop(args):
        
    ''' Handle the listening loop '''

    target = str(args['HOST'])
    port = int(args['PORT'])

    # if no target is defined, listen on all interfaces

    if not len(target):
        target = "0.0.0.0"

    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as server:
        server.bind((target,port))
        server.listen(5)
        
        while True:
            client_socket, addr = server.accept()

            
            # starts a thread to handle new clients
            client_thread = t.Thread(target=client_handler,args=(client_socket,))
            
            client_thread.start()

 
def run_command(args):
    
    command = args['COMMAND']
    # remove any new line

    command = command.rstrip()

    # run the command and get the output back

    try:
        output = subprocess.check_output(command,stderr=subprocess.STDOUT,shell=True)

    except:
        output = "Failed to execute command.\r\n"

    # return the output 
    return output

def client_handler(client_socket):
    global upload 
    global execute
    global command

    upload = args['DEST']
    execute = args['FILE']

    # Check for upload
    if len(args['DEST']):
        # Read bytes and write to the destination

        file_buffer = ""

        # Read all the data until no more available and stores it inside a buffer
        while True:
            data = client_socket.recv(1024)

            if not data:
                break
            else:
                file_buffer += data

        # Write the uploaded bytes

        try:
            file_descriptor = open(args['DEST'],"wb")
            file_descriptor.write(file_buffer)
            file_descriptor.close()

            # Confirm writing
            client_socket.send("Saving to file %s was successful !\r\n" % args['DEST'])
        except:
            client_socket.send("Failed to save file to %s\r\n" % args['DEST'])

    # Now we check for command execution

    if execute:
        
        # attempt to run the command

        output = run_command(execute)

        client_socket.send(output)

    # goes into a loop if shell command requested
    if command:

        while True:
            # Show a simple prompt
            client_socket.send("<BHP:#> ")

            # Receive until we see a linefeed (enter key)

            cmd_buffer = ""

            while "\n" not in cmd_buffer:
                cmd_buffer += client_socket.recv(1024)

            # Send back the command output

            response = run_command(cmd_buffer)

            # Send back the response

            client_socket.send(response)


def main(args):
    print(args)

    # Handle starting check between listening or sending data through stdin
    try:
        if not args['--listen'] and len(args['HOST']) and int(args['PORT']) > 0:
             # read the buffer from the cmdline
            # blocking any input. Use CTRL-D if you are not sending input
            # to stdin
                buf = sys.stdin.read()

            # then send the data
                client_sender(buf)
    except TypeError as e:
        print("[*] Exception occured {}".format(e))
    # if listen is happening, files will be uploaded
    # commands executed, or shell potentially popping
    # depending on the commands passed
    if args['--listen']:

        # start the listening loop
        server_loop(args)

    
if __name__ == '__main__':
    args = docopt(__doc__,version="0.1")

    main(args)
