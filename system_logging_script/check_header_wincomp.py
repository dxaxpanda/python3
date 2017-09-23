#!/usr/bin/env/python2.7

import urllib2
from bs4 import BeautifulSoup 
import subprocess
import sys
import time
import logging
import logging.handlers
import urllib
import httplib

""" Check website availability with footer content header.
    As such, for http://www.wincomparator.net will be checked
    with the page : 'http://www.wincomparator.com/fr-fr/match-en-direct/football/'
    to ensure the arbo is fully available. If a 404 occured or the text isn't loaded inside the page it
    will try to reload it as a cron job working each minute. """

""" Solo url check with related variable."""
url = ('www.wincomparator.com/fr-fr/match-en-direct/football/')
content = "Liste des RSS"

"""Home pages check with related variables."""
home_pages = ('www.wincomparator.com',
              'www.wincomparator.com/pl-pl/home.html',
              'www.wincomparator.com/da-dk/home.html',
              'www.wincomparator.com/it-it/home.html',
              'www.wincomparator.com/en-gb/home.html',
              'www.wincomparator.com/el-gr/home.html',
              'www.wincomparator.com/pt-pt/home.html',
              'www.wincomparator.com/es-es/home.html',
              'www.wincomparator.com/de-de/home.html')

tag = "div"
attrib = "id"
value = "matchs-list"

"""php reload script variables"""
script_args = """php /home/windataco/batch/current/src/bin/old/reload_all_arbo.php >> /var/log/windataco/import/log_prod_reload_all_arbo.log"""
logfile = "/var/log/windataco/batch/check_wincomp_url.log"
#logfile = "/opt/check_wincomp_url.log"


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

def Get_URL(url):
    """ Check if url is valid."""
    try:
        check = urllib2.urlopen("http://"+url)

        return check
    except urllib2.HTTPError as e:
        logging.warning("[RUN]\tAn error occured: %s", e)
        check = False

        return check

    except urllib2.URLError as e:
        logging.error("[RUN]\tAn error occured: %s", e)
        logging.info("[   END  ]\tWINCOMPARATOR PAGE CHECK")
        sys.exit(1)


def Get_Content(name, infile):
    """ Check whether content string is present."""
    logging.info("[RUN]\tContent to check defined as: ' %s '.", name)
    logging.info("[RUN]\tChecking whether content is loaded within the page...")
    if name in infile:
        logging.info("[RUN]\tContent: ' %s '  is present inside the page.", name)
        logging.info("[RUN]\tNothing to do...")

        return True

    else:
        logging.warning("[RUN]\tContent not found...")
        logging.warning("[RUN]\tAttempting to reload arbo...")

        return False

def Parse_HTML(tag, attrib, value, result):
    """ Check whether the menu tree is broken with h2 presence """
    logging.info("[RUN]\tChecking if menu tree is broken...")  
    parsed_html = BeautifulSoup(result, "html.parser")
    
    get_value = parsed_html.find(tag, attrs={attrib:value})#.text 
    #logging.info("[RUN]\t Got value: %s", get_value)
    print get_value
    return get_value

def Menu_Rebuild(url):
    """ Rebuild the menu tree with a specific request to the page."""
    logging.info("[RUN]\tMenu tree is broken... Attempting rebuild.")
    logging.info("[RUN]\tRebuild done.")
    rebuild = urllib2.urlopen("http://"+url+"?ds_rebuild_cache=ds")

    return rebuild

def Varnish_Purge(url):
    """ Send purge request to varnish. """
    logging.info("[RUN]\tSending purge request to varnish.")
    logging.info("[RUN]\tURL=%s", url)
    varnish = httplib.HTTPConnection("www.wincomparator.com")
    purge_req = varnish.request("PURGE", url)
    purge_resp = varnish.getresponse()
    logging.info("[RUN]\tInfo : %s", purge_resp)
    
    
def Reload_Arbo(script_args, logfile):
    """ Launch script to reload arbo because WE NEED WINCOMPARATOR TO LIVE ! """

    args = script_args.split()
    logging.warning("[RUN]\tReady to launch new process...")
    #logging.info("[RUN]\tLogging output to: %s" , logfile)
    with open(logfile, "a") as f:
        process = subprocess.Popen(" ".join(args), shell=True, stdout=f, stderr=f, bufsize=1)
        #for line in process.stdout:
         #   logger.info(line)




def main():
    """ Launch log setup"""
    log_setup(logfile)

    logging.info("[ START ]\tWINCOMPARATOR PAGE CHECK")
    logging.info("[RUN]\tTrying check for url: ' %s '" , url)
    
    page_response = Get_URL(url)

    if page_response:
        resp_code = page_response.code
        logging.info("[RUN]\tGot response code: ' %d '... Attempting content check." , resp_code)
    
        """ Get all the html data. """
        html = page_response.read()
        status = Get_Content(content, html)
        if status:
           pass 
        else:
            Reload_Arbo(script_args, logfile)
            logging.info("[  END  ]\tWINCOMPARATOR PAGE CHECK")

    else:
        Reload_Arbo(script_args, logfile)
        #logging.info("[  END  ]\tWINCOMPARATOR PAGE CHECK")

    """ Now we are going to check the homes pages..."""

    logging.info("[RUN]\tNow trying to check homepages...")
    
    for homepage in home_pages:
        logging.info("[RUN]\t"+"-"*50)
        logging.info("[RUN]\tChecking page: ' %s ' ...", homepage)
        result = Get_URL(homepage)
        html = result.read()
        logging.info("[RUN]\tChecking whether %s div is present with values :", value)
        logging.info("[RUN]\tTag: %s", tag)
        logging.info("[RUN]\tAttribute: %s", attrib)
        logging.info("[RUN]\tValue: %s", value)
        home_page_html = Parse_HTML(tag, attrib, value, html)
        logging.info("[RUN]\tChecking cache freshness...")
        cache_status = Get_URL(homepage).info().getheader('X-Cache')
        if cache_status == "HIT":
            logging.info("[RUN]\tPage %s is a HIT", homepage)

        if home_page_html:
            logging.info("[RUN]\t%s part is present inside the page !", value)
            logging.info("[RUN]\tNothing to do...")

        else:
            Menu_Rebuild(homepage)

            if cache_status == "HIT":
                Varnish_Purge(homepage)

                 
         


if __name__ == "__main__":
    main()

