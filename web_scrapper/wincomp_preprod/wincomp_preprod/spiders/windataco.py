# -*- coding: utf-8 -*-

from scrapy.spiders import CrawlSpider, Rule
from scrapy.linkextractors import LinkExtractor
from scrapy.utils.log import configure_logging

import logging
import os
import time 

def log_setup():
    print("Preparing Log Setup...")
    try:
        print("Checking whether log file already exists...")
        if os.path.exists("spider.log") is False:
            print("File doesnt exists. Creating it.")
            with open('spider.log', 'w') as f:
                f.write("[!] Stating NEW LOG FLE [!]")
                
        else:
            try:
                print("[!] Renaming old file for new spider crawl [!]")
                os.rename('spider.log', 'spider.log-old')
            except FileNotFoundError as e:
                raise e
            log_handler = logging.handlers.WatchedFileHandler('spider.log', 'a')
            formatter = logging.Formatter('%(asctime)s  \program_name [%(process)d]: %(message)s', '%b %d %H:%M:%S')
            formatter.converter = time.gmtime
            log_handler.setFormatter(formatter)
            logger = logging.getLogger()
            logger.addHandler(log_handler)
            logger.setLevel(logging.DEBUG)
    except Exception as e:
        print(e)

#configure_logging(install_root_handler=False)
#logging.basicConfig(
#        filename='log.txt',
#        format='%(levelname)s: %(message)s',
#        level=logging.INFO
#)

log_setup()

class WindatacoSpider(CrawlSpider):
    name = 'windataco'
    http_user = 'webtour'
    http_pass = 'wcomp'
    allowed_domains = [
            'www.wincomparator.com.preprod2.wincomparator.net',
            'www.wincomparator.gr.preprod2.wincomparator.net',
            'www.wincomparator.pt.preprod2.wincomparator.net',
            'fb-wincomparator2.wincomparator.net',
            'fb.wincomparator.com.web7.preprod.wincomparator.net',
            'bo.wincomparator.net.preprod2.wincomparator.net',
            'm.wincomparator.com.preprod2.wincomparator.net',
            ]
    start_urls = [
            'http://www.wincomparator.com.preprod2.wincomparator.net/',
            'http://www.wincomparator.com.preprod2.wincomparator.net/fr-fr/cotes/football/',
            'http://www.wincomparator.com.preprod2.wincomparator.net/fr-fr/cotes/basketball/']

    rules = (
            Rule(LinkExtractor(
                    allow=(),
                    tags=('a','area'),
                    #attrs=('href'),
                    restrict_css=('.bt_more',)),
                    #restrict_css=('bt_more',)),
                    callback="parse_item",
                    follow=True),
            )

    def parse_item(self, response):
            #print('Processing...' + response.url)
            #self.logger.info("Logging in :" + '\n' + response.url)
            logging.info("Logging in :" + '\n' + response.url)
            #logger.info(
            print('Processing...' + response.url)

