
import socket


# define the constants

target_hostname = 'google.com'
target_port = 80
#request = 'GET / HTTP1.1\r\nHost: {}\r\n\r\n'.format(target_hostname)

request = 'GET / HTTP1.1\r\nHost: www.google.com\r\n\r\n'
print("Request is :", request)
# Create a IPV4 tcp socket object. AF_INET means IPV4 and SOCK_STREAM is TCP
tcp_client = socket.socket(socket.AF_INET,socket.SOCK_STREAM)

# Create a TCP connections
tcp_client.connect((target_hostname,target_port))

# send some data
tcp_client.sendto(b'GET / HTTP1.1\r\nHost: www.google.com\r\n\r\n', (target_hostname, target_port))

# show response (4096 bytes)
response = tcp_client.recv(10000000)

print(response.decode('UTF-8'))
