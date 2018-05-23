# -*- encoding: utf-8 -*-
#!/usr/bin/env python3

import ovh
import logging
import logging.handlers


def log_setup(logfile):
    #log_handler = logging.handlers.WatchedFileHandler('my.log')
    rotation_handler = logging.handlers.RotatingFileHandler(logfile, 'a', 100000000, 1) 
    formatter = logging.Formatter("%(asctime)s %(filename)s [%(levelname)s] [%(process)d]: %(message)s",
                                  "%b %d %H:%M:%S")
    formatter.converter = time.gmtime  # if you want UTC time
    #log_handler.setFormatter(formatter)
    rotation_handler.setFormatter(formatter)
    logger = logging.getLogger()
    #logger.addHandler(log_handler)
    logger.addHandler(rotation_handler)
    logger.setLevel(logging.DEBUG)

# Instantiate. Visit https://api.ovh.com/createToken/index.cgi?GET=/me
# create a client using configuration
client = ovh.Client(config_file='ovh.conf')

# Request RO, /me API access
ck = client.new_consumer_key_request()
ck.add_recursive_rules(ovh.API_READ_WRITE, "/")

# Request token
validation = ck.request()

print("Please visit {} to authenticate" .format(validation['validationUrl']))
input("and press Enter to continue...")

# Print nice welcome message
print("Welcome", client.get('/me')['firstname'])
print("Btw, your 'consumerKey' is '{}'".format(validation['consumerKey']))



