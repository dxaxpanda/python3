#!/usr/bin/python3.6

''' Simple multi-threaded http client using python requests lib '''

import requests as r
import queue
import os
import threading

hosts = ("http://google.com",
         "http://jeuxvideo.com",
         "https://www.sportytrader.com",
         "http://facebook.fr",
         "http://netflix.com",
         "http://stackoverflow.com",
         "http://dealabs.fr",
         "http://gmail.com",
         "http://voo.be",
         "http://asus.fr",
         "http://supinfo.com",
         "http://youtube.fr",
         "http://wincomparator.net",
         "http://last.fm",
         )

threads = 10

# initialize the queue
q = queue.Queue()

headers={'User-agent': 'Googlebot'}



def get():
    while not q.empty():
        url = q.get()
        print("[*] Printing headers for request: ", headers)
        req = r.get(url,headers=headers)
        print("[*] And our response headers: ")
        print("[*] [response headers] ==>", req.headers)
        print("-" * 20)
        q.task_done()



# Fill our queue
for h in hosts:
    # add our websites to the queue
    print("[*] Adding host: %s to queue" % h)
    q.put(h)

for thread in range(threads):
    print("[*] Spawning thread: %d" % thread)

    t = threading.Thread(target=get)

    t.start()

q.join()

