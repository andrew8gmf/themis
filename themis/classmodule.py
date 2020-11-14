import tweepy
import os
import io

from dotenv import load_dotenv, find_dotenv
load_dotenv(find_dotenv())

API_KEY = os.environ.get("API_KEY")
API_SECRET = os.environ.get("API_SECRET")
ACCESS_TOKEN = os.environ.get("ACCESS_TOKEN")
ACCESS_TOKEN_SECRET = os.environ.get("ACCESS_TOKEN_SECRET")

class StreamListener(tweepy.StreamListener):

    def __init__(self, api, fetched_tweets_filename):
        self.api = api
        self.me = api.me()

        self.fetched_tweets_filename = fetched_tweets_filename

    def on_status(self, tweet):
        try:
            print(f"{tweet.user.name}:{tweet.text}")
            with io.open(self.fetched_tweets_filename, 'a', encoding="utf-8") as tf:
                tf.write(str(tweet))
            return True
        except BaseException as e:
            print("Error on_data %s" % str(e))
        return True

    def on_error(self, status):
        print(status)

class TweepyStreamer():

    def __init__(self):
        pass

    def start(self, fetched_tweets_filename, keyword_list):
        auth = tweepy.OAuthHandler(API_KEY,API_SECRET)
        auth.set_access_token(ACCESS_TOKEN,ACCESS_TOKEN_SECRET)

        api = tweepy.API(auth)
        
        self.stream = tweepy.Stream(api.auth, StreamListener(api, fetched_tweets_filename))
        self.stream.filter(track=keyword_list)