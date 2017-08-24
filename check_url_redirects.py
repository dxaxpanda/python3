#!/usr/bin/env python3

import sys
import requests

def check_for_redirects(url):
    try:
        r = requests.get(url, allow_redirects=False, timeout=0.5)
        if 300 <= r.status_code < 400:
            return r.headers['location']
        else:
            return '[no redirect]'
    except requests.exceptions.Timeout:
        return '[timeout]'
    except requests.exceptions.ConnectionError:
        return '[connection error]'


def check_domains(urls):
    for url in urls:
        url_to_check = url if url.startswith('http') else f"http://{url}"
        redirect_url = check_for_redirects(url_to_check)
        print(f"{url_to_check} => {redirect_url}")

if __name__ == '__main__':
    fname = 'domains.txt'
    try:
        fname = sys.argv[1]
    except IndexError:
        pass
    urls = (l.strip() for l in open(fname).readlines())
    check_domains(urls)
