#!/usr/bin/env/python2.7

"""check_url.

Usage:
    check_url.py [-o FILE] [-q | -v ] <url>
    check_url.py [ -h | --help ]
    check_url.py --version

Arguments:
    URL             url to check
    FILE            output file
    CONTENT         content to check

Options:
    -h,  --help     print usage
    -v, --verbose   verbose mode
    -q, --quiet     quiet mode
    -o, --output    output file
    --version       print version number
"""

import urllib2
from docopt import docopt
import subprocess
import sys
import time
import logging
import logging.handlers


""" Check website availability with footer content header.
    As such, for http://www.wincomparator.net will be checked
    with the page : 'http://www.wincomparator.com/fr-fr/match-en-direct/football/'
    to ensure the arbo is fully available. If not it will try to reload it as a cron
    job working each minute. """


url = ('www.wincomparator.com/fr-fr/match-en-direct/football/')
content = "Liste des RSS"
script_args = "php /home/windataco/batch/current/src/bin/old/reload_all_arbo.php >> /var/log/windataco/import/log_prod_reload_all_arbo.log"
logfile = "/var/log/windataco/import/check_wincomp_url.log"


def log_setup(logfile):
    #log_handler = logging.handlers.WatchedFileHandler('my.log')
    rotation_handler = logging.handlers.RotatingFileHandler(logfile, 'a', 100000000, 1)
    formatter = logging.Formatter("%(asctime)s %(filename)s [%(process)d]: %(message)s",
                                  "%b %d %H:%M:%S")
    formatter.converter = time.gmtime  # if you want UTC time
    #log_handler.setFormatter(formatter)
    rotation_handler.setFormatter(formatter)
    logger = logging.getLogger()
    #logger.addHandler(log_handler)
    logger.addHandler(rotation_handler)
    logger.setLevel(logging.DEBUG)

def Get_URL(url):
    """ Check if url is valid."""
    try:
        check = urllib2.urlopen("http://"+url)

        return check
    except (urllib2.URLError, urllib2.HTTPError) as e:
        logging.error("[RUN]\tAn error occured: %s", e)
        logging.info("[  END ]\tWINCOMPARATOR PAGE CHECK")
        sys.exit(1)


def Get_Content(resp_code, name, infile):
    """ Check whether content string is present."""
    logging.info("[RUN]\tContent to check defined as: ' %s '.", name)
    logging.info("[RUN]\tChecking whether content is loaded within the page...")
    if name in infile:
        logging.info("[RUN]\tContent: ' %s '  is present inside the page.", name)
        logging.info("[RUN]\tNothing to do...")

        return True

    else:
        logger.warning("[RUN]\tContent not found...")
        logger.warning("[RUN]\tAttempting to reload arbo...")

        return False


def Reload_Arbo(script_args, logfile):
    """ Launch script to reload arbo because WE NEED WINCOMPARATOR TO LIVE ! """

    args = script_args.split()
    logger.info("[RUN]\tReady to launch new process...")
    logger.info("[RUN]\tLogging output to: %s" , logfile)
    with open(logfile, "a") as f:
        process = subprocess.Popen(" ".join(args), shell=True, stdout=logfile, stderr=logfile, bufsize=1)
        #for line in process.stdout:
         #   logger.info(line)




def main():
     """ Main CLI entrypoint. """
    import commands

    options = docopt(__doc__, version='0.1')
   #print options

    """ Launch log setup"""
    log_setup(logfile)
    logging.info("[ START ]\tWINCOMPARATOR PAGE CHECK")



    url_check = Get_URL(url)
    resp_code = url_check.code
    logging.info("[RUN]\tTrying check for url: ' %s '" , url_check.geturl())
    logging.info("[RUN]\tGot response code: ' %d '... Attempting content check." , resp_code)


    """ Get all the html data. """
    html = url_check.read()
    #print "With data: \n%s" % html

    status = Get_Content(resp_code, content, html)

    if status:
        logging.info("[  END  ]\tWINCOMPARATOR PAGE CHECK")
        sys.exit(0)
    else:
        Reload_Arbo(script_args, logfile)
        logging.info("[  END  ]\tWINCOMPARATOR PAGE CHECK")

if __name__ == "__main__":
    main()
