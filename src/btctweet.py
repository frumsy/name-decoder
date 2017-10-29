import pandas as pd
import numpy as np

# Import the necessary package to process data in JSON format
try:
    import json
except ImportError:
    import simplejson as json

# Import the necessary methods from "twitter" library
from twitter import Twitter, OAuth, TwitterHTTPError, TwitterStream

# Variables that contains the user credentials to access Twitter API 
ACCESS_TOKEN = '924609786989174785-KUxNuqeHzkaOUm4HptahSqisQlFt5xo'
ACCESS_SECRET = 'gBl1JQs5Quz5XjKFeKKT1k3IhnNNypFzihkiXQVTzVmoA'
CONSUMER_KEY = 'eSOiGoWWooQGjI2Mgyag1SFVB'
CONSUMER_SECRET = 'qlwEOia8KPDdgciXoFXPXCo1hHhbnvMyrxwOtSDKPNgnXEAGp9'

oauth = OAuth(ACCESS_TOKEN, ACCESS_SECRET, CONSUMER_KEY, CONSUMER_SECRET)

# Initiate the connection to Twitter REST API
twitter = Twitter(auth=oauth)

count = 90
# Search for latest tweets about "#nlproc"
tweets = twitter.search.tweets(q='#bitcoin', until='2017-10-22', lang='en', count=count)

data = []
#posts = []
for i in range(0, count):
	data.append(tweets['statuses'][i]['created_at'])
	data.append(tweets['statuses'][i]['text'])
	#print(tweets['statuses'][i]['created_at'])
	#print(tweets['statuses'][i]['text'])


data = np.asarray(data)

df = pd.DataFrame(data)
df.to_csv("10-22.csv", index=False)

#print(tweets[1]['text'])
#print(json.loads(tweets, indent=4)['text'])

"""
tweet_count = 10
for tweet in tweets:
	tweet_count -= 1

	break
	if tweet_count <= 0:
		break 
"""