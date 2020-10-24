from pyfiglet import Figlet

from classmodule import TwitterStreamer, StdOutListener

def main():
    f = Figlet(font='slant')
    print(f.renderText('themis')) 

    hash_tag_list = ["donald trump"]
    fetched_tweets_filename = "tweets.txt"

    twitter_streamer = TwitterStreamer()
    twitter_streamer.stream_tweets(fetched_tweets_filename, hash_tag_list)

if __name__ == '__main__':
    main()