#Imports
import pandas as pd
import requests
import requests.auth
import json
import datetime
import csv

#Getting coin data
url = 'https://pro-api.coinmarketcap.com/v1/cryptocurrency/listings/latest'
parameters = {
  'start':'1',
  'limit':'5000',
  'convert':'USD'
}

cmc_data = requests.get(url, params=parameters, headers=headers).json()

# Creating Coins dataset
coins = pd.json_normalize(cmc_data['data'])

# Keeping only useful columns
coins.drop(columns=['id', 'num_market_pairs',
       'tags', 'max_supply', 'self_reported_circulating_supply',
       'self_reported_market_cap', 'last_updated',
       'quote.USD.fully_diluted_market_cap', 'quote.USD.last_updated',
       'platform.name', 'platform.symbol', 'platform.slug',
       'platform.token_address', 'slug', 'platform.id', 'quote.USD.volume_change_24h', 'total_supply', 'platform'], inplace=True)

#Export df to csv
coins.to_csv('coins.csv', encoding='utf-8', index=False)

#Create dataset with top50 coins
top_50 = coins.head(50).copy()

#Def function to get crypto data from reddit submissions

def get_crypto_data(data_type, **kwargs):

    """
    Gets data from the pushshift api.

    """

    base_url = f"https://api.pushshift.io/reddit/search/{data_type}/"
    payload = kwargs
    request = requests.get(base_url, params=payload)
    reddit_data = request.json()
    return reddit_data['data']

#Create empty dict to store data
subStats = {}

#Def function to get useful information from crypto_data
def collectSubData(subm):
    """
    Get useful data from submission dictionary and store in subStats dict
    """

    subData = list() #list to store data points
    name = f"{coin_name}"
    title = subm['title']
    url = subm['url']
    try:
        flair = subm['link_flair_text']
    except KeyError:
        flair = "NaN"
    author = subm['author']
    sub_id = subm['id']
    score = subm['score']
    created = datetime.datetime.fromtimestamp(subm['created_utc']) #1520561700.0
    numComms = subm['num_comments']
    permalink = f"https://www.reddit.com{subm['permalink']}"
    subData.append((name,title,permalink,numComms))
    subStats[sub_id] = subData

    #Loop through each coin in top_50 to get its data and append to 'subStats'
data_type="submission"
size=50
after = "24h"
print(f"Loop through each coin in top_50 to get {size} posts for each coin, this may take a while")
for coin_name in top_50['name']:
    data = get_crypto_data(data_type=data_type,
                          q=coin_name,
                          size=size,
                          after=after)
    for i in range(0, len(data)):
        collectSubData(data[i])

def updateSubs_file():
    """
    Write csv with Subs information
    """
    upload_count = 0
    #location = "\\Reddit Data\\"
    print("input filename of submission file, please add .csv")
    filename = input()
    file = filename
    with open(file, 'w', newline='', encoding='utf-8') as file:
        a = csv.writer(file, delimiter=',')
        headers = ['Coin name','Title','Link','Number of comments']
        a.writerow(headers)
        for sub in subStats:
            a.writerow(subStats[sub][0])
            upload_count+=1

        print(str(upload_count) + " submissions have been uploaded")
        print(f'Program completed. Reddit data from top 50 coins wrote to {file}.csv')
updateSubs_file()
