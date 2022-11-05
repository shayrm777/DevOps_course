"""
Working with API
"""


import requests as r
import urllib.request as urlreq
from PIL import Image

resp = r.get("https://randomfox.ca/floof", verify=False)
print(resp.status_code)
#print(resp.text)
fox = resp.json()
print(fox["image"])

opener = urlreq.URLopener()
opener.addheader('User-Agent', 'Mozilla/5.0')
opener.urlretrieve(fox["image"], "sample.png")

img = Image.open("sample.png")
img.show()