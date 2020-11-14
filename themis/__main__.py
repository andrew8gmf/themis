from pyfiglet import Figlet

from classmodule import TweepyStreamer

def main():
    f = Figlet(font='slant')
    print(f.renderText('themis')) 

    hash_tag_list = ["donald trump"]
    fetched_tweets_filename = "tweets.txt"

    stream = TweepyStreamer()
    stream.start(fetched_tweets_filename, hash_tag_list)

if __name__ == '__main__':
    main()