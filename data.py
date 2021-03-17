import csv
import requests
import pandas as pd
from PIL import Image, ImageDraw

try:
    from urllib.request import Request, urlopen  # Python 3
except ImportError:
    from urllib2 import Request, urlopen  # Python 2

req = Request(
    "https://ark-funds.com/wp-content/fundsiteliterature/csv/ARK_INNOVATION_ETF_ARKK_HOLDINGS.csv")
req.add_header(
    'User-Agent', 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:77.0) Gecko/20100101 Firefox/77.0')
content = urlopen(req)

df = pd.read_csv(content)
print(df.dtypes)


df1 = df[['company', 'ticker', 'weight(%)']]
print(df1.head(20))

img = Image.new('RGB', (1000, 300), color=(73, 109, 137))

d = ImageDraw.Draw(img)
d.text((15, 15), df, fill=(255, 255, 0))

img.save('hello.png')
