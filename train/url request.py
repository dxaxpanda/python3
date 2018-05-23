import requests

import webbrowser
from sys import os


response = requests.get("http://sportytrader.com")

sportytrader = response.text

print(sportytrader)


webbrowser.open('file://' + os.path.realpath(sportytrader))
