import sys
import time
import requests
import datetime
sys.path.append("..")

a = requests.session()
url = "http://132.232.34.26:8888"
get = a.get(url)
print(a.content)
