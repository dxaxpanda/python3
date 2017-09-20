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
logfile = "/var/log/windataco/arbo_script.log"


def log_setup():
    log_handler = logging.handlers.WatchedFileHandler('my.log')
    formatter = logging.Formatter("%(asctime)s url_checker.py [%(process)d]: %(message)s",
                                  "%b %d %H:%M:%S")
    formatter.converter = time.gmtime  # if you want UTC time
    log_handler.setFormatter(formatter)
    logger = logging.getLogger()
    logger.addHandler(log_handler)
    logger.setLevel(logging.DEBUG)

def Get_URL(url):
    """ Check if url is valid."""
    try:
        check = urllib2.urlopen("http://"+url)
        return check
    except (urllib2.URLError, urllib2.HTTPError) as e:
        print "[!]\tAn error occured: %s" % e
        sys.exit(1)


def Get_Content(name, infile):
    """ Check whether content string is present."""
    print "[!]\tContent defined as: ' %s '" % name
    print "[!]\tChecking whether content is loaded within the page..."
    if name in infile:
        print "Content: ' %s '  is present inside the page." % name
        print "Nothing to do..."
        
        return sys.exit(0)
    
    else:
        print "[!]\tContent not found..."
        print "[!]\tAttempting to reload arbo..."

        return False


def Reload_Arbo(script_args, logfile):
    """ Launch script to reload arbo because WE NEED WINCOMPARATOR TO LIVE ! """
    
    args = script_args.split()
    process = subprocess.Popen(" ".join(args), shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, bufsize=1)
    with open(logfile, "a") as f:
        for line in process.stdout:
            logger.info(line)

    


def main():
    """ Main CLI entrypoint. """
    import commands

    options = docopt(__doc__, version='0.1')
   #print options
    
    log_setup()
    logging.info('Hello, World!')
    

    check = Get_URL(url)
    print "[!]\tThis is our url : ' %s '" % url
    print "Trying check for url: ' %s '" % check.geturl()
    print "With response code: ' %d '" % check.code

    """ Get all the html data. """
    html = check.read()
    #print "With data: \n%s" % html

    Get_Content(content, html)
     
    Reload_Arbo(script_args, logfile)    



if __name__ == "__main__":
    main()
