#!/usr/bin/env python2.7
import subprocess
import cgi
import sys
import logging
from StringIO import StringIO
from threading import Thread


cgitb.enable()

sys.stdout = open('log.txt', 'w')

APPLE_API_URL = "https://api.push.apple.com/3/device"
try:
    form = cgi.FieldStorage(environ={'REQUEST_METHOD':'POST'})
    print form
except:
    print "over"
                   # fp=self.rfile,
                 #   headers=self.headers,
                  # environ={'REQUEST_METHOD':'POST'})

#self._set_headers()

TOKEN = form.getvalue('token')
BUNDLE_ID = form.getvalue('bundle_id')
PAYLOAD = form.getvalue('message')
CERT_FILE = form.getvalue('certificat')

with open("vars.log", "w") as file:
        f.write(TOKEN)
CURL_CMD = """/usr/local/bin/curl --verbose --data {} --header "apns-topic: {}" \
            --header "apns-priority: 10" --header "method: POST" --http2
            --cert {} {}/{}""".format(PAYLOAD, BUNDLE_ID, CERT_FILE,
            APPLE_API_URL, TOKEN)

with open ("test.log", "w") as f:
    f.write("CURL_CMD: {}".format(CURL_CMD))
    f.write("TOKEN: ".format(TOKEN)
    f.write("BUNDLE_ID: ".format(BUNDLE_ID)
    f.write("PAYLOAD: ".format(PAYLOAD)
    f.write("CERT_FILE: ".format(CERT_FILE)
rootLogger = logging.getLogger()

logfile = open('/home/jeremy/skores/webservices/log.txt', 'w')


args = CURL_CMD.split()
f2 = open("test.test.test", "w")
process = subprocess.Popen(args, stdout=f2, stderr=f2, bufsize=1)
with process.stdout, open(logfile, 'ab') as file:
        for line in iter(process.stdout.readline, b''):
            print line,
            file.write(line)
process.wait()



#print args

#process = subprocess.Popen(args, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)

#for line in process.stdout:
#    sys.stdout.write(line)
#    logfile.write(line)
#process.wait()

#(out, err) = process.communicate()
#
#logger.info('Main script output : ')
#logger.INFO(out)










#def consume_lines(pipe, consume):
#    with pipe:
#        for line in iter(pipe.readline, b''):
#            consume(line)


#def run_shell_command(command):
#    args = command.split()
#
#    logging.info('Subprocess: "' + command + + '"')
#
#    print args
#
#    try: 
#        process = subprocess.Popen(args, shell=False, stdout=subprocess.PIPE, stderr=subprocess.STDOUT, bufsize=1)
#        Thread(target=consume_lines, args=[process.stdout, consume]).start()
#        process.wait
#
#        stdout, stderr = process.communicate()
#       log_subuprocess_output(stdout)
#        print process
#    except (OSerror, CalledProcessError) as exception:
#        logging.info('Exception occured: ' + str(exception))
#        logging.info('Subprocess failed')
#        
#        return False
#    else:
  #      # no exception was raised
 #       logging.info('Subprocess finished')
#
#        return True

#logger = logging.getLogger(__name__)

#logging.basicConfig(level=logging.INFO, format='%(asctime)s %(message)s')
#consume = lambda line: logging.info('OUPUT : %r', line)

