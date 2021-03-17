from tabulate import tabulate
import csv
import requests
import tweepy
from credentials import *

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)

auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth, wait_on_rate_limit=True, wait_on_rate_limit_notify=True)

URL = "https://ark-funds.com/wp-content/fundsiteliterature/csv/ARK_INNOVATION_ETF_ARKK_HOLDINGS.csv"

with requests.Session() as s:
    download = s.get(URL)

    decoded_content = download.content.decode('utf-8')

    data = csv.reader(decoded_content.splitlines(), delimiter=',')
    dataList = list(data)

    date = ""
    array = []

    for row in dataList[1:11]:
        date = row[0]
        row = row[3], row[7]
        array.append(row)
    print('hello')
    table = tabulate(array, headers=['Ticker', 'Weight %'])
    tweet = f"$ARKK Top 10 {date}\n{table}"
    print(len(tweet))
    print(tweet)

    api.update_status(status=tweet, tweet_mode='extended')
