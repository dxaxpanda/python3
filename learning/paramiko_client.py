
import paramiko
from sys import argv, exit


ssh = paramiko.SSHClient()
ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())

script, filename = argv

def usage():
    print("Usage {} <filename>".format(script))
    

if len(argv) is not 2:
    usage()
    quit()

try:
    with open(filename, "r") as f:
        for line in readlines(test):
            print(line)
except Exception as e:
    with open(filename, "w") as f:
        f.write(""" aaaaaaaa \n aaaaaa  \n aaaa""")
try:
    ssh.connect('localhost', username='jmirre', password='pilatus')
except paramiko.SSHException as e :
    print("An error occured : ", e)
    quit()

stdin, stdout, stderr = ssh.exec_command("cat")

stdin.write("test")
for line in stdout.readlines():
    print(line.strip())

print("==="*200)




#ssh.close()

