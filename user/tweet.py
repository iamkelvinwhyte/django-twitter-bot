import os
import tweepy as tw
import pandas as pd
import json
from random import randint


def random_gentarted(n):
    range_start = 10**(n-1)
    range_end = (10**n)-1
    return randint(range_start, range_end)


def AuthKey() :
    #Import and read setting json file
    with open('settings.json','r') as f:
            settings=json.load(f)
    return settings



# Tweet to Text
def tweet2txt(tweets):
    filename=str(random_gentarted(10))+".txt"
    try:
        with open("uploads/"+filename, 'a+') as filehandle:
            for tweet in tweets:
                filehandle.write('%s\n' % tweet.text)
        return filename
    except:
        return "Invalid data type"

# Tweet to CSV
def tweet2csv(tweets):
    try:
        tweet_logs = [[tweet.id, tweet.text] for tweet in tweets]
        tweet_text= pd.DataFrame(data=tweet_logs, columns=['id', "text"]) 
        filename=str(random_gentarted(10))+".csv"
        tweet_csv=tweet_text.to_csv('uploads/'+filename) 
        return filename
    except:
        return "Invalid data type"

# Tweet to Json
def tweet2json(tweets):
     try:
        tweet_logs = [[tweet.id, tweet.text] for tweet in tweets]
        tweet_text= pd.DataFrame(data=tweet_logs, columns=['id', "text"]) 
        filename=str(random_gentarted(10))+".json"
        tweet_json=tweet_text.to_json("uploads/"+filename) 
        return filename
     except:
        return "Invalid data type"


def SearchTweet(search_words,max_results):
    Token = AuthKey()
    client = tw.Client(Token['bearer_token'])
    try:
        tweets= tw.Paginator(client.search_recent_tweets, query=search_words,
                                    tweet_fields=['context_annotations', 'created_at'], max_results=10).flatten(limit=max_results)
        return tweets
    except:
        return ("Sorry, unable to access Api")



