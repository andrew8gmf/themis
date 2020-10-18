from pyfiglet import Figlet

from tweepy_streamer import TwitterStreamer, StdOutListener

def main():
    f = Figlet(font='slant')
    print(f.renderText('themis')) 

    hash_tag_list = ["donald trump", "hillary clinton", "barack obama", "bernie sanders"]
    fetched_tweets_filename = "tweets.json"

    twitter_streamer = TwitterStreamer()
    twitter_streamer.stream_tweets(fetched_tweets_filename, hash_tag_list)

if __name__ == '__main__':
    main()