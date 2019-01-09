import tweepy
import csv
import pandas as pd
from tweepy.streaming import StreamListener
from tweepy import OAuthHandler
from tweepy import Stream

####input your credentials here
consumer_key = ''
consumer_secret = ''
access_token = ''
access_token_secret = ''

tweets = []
class StdOutListener(StreamListener):

    def on_data(self, data):
        #if data['lang'] == 'en':
        #tweets.append(data)
        with open('tweetfile.txt', 'w') as f: 
        f.write('Text')
        writer = csv.writer(f)
        writer.writerow([data.text])
        	
    def on_error(self, status):
    	print (status)
if __name__ == '__main__':
	l = StdOutListener()		    	
	auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
	auth.set_access_token(access_token, access_token_secret)
	stream = Stream(auth, l)

		    #This line filter Twitter Streams to capture data by the keywords: 'python', 'javascript', 'ruby'
	stream.filter(track=['trump'],languages=['en'])
