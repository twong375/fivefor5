#Import the necessary methods from tweepy library
from tweepy.streaming import StreamListener
from tweepy import OAuthHandler
from tweepy import Stream
from pprint import pprint
import json
import firebase


#Variables that contains the user credentials to access Twitter API 
access_token = "744337933713424388-19ocYNWcIldJLLsbv2ceZrIIMdiqXsG"
access_token_secret = "b2mwzQzisHg7Rh49ecXyO72ziC7FzhMXqffWuEphpLdZO"
consumer_key = "TJABGVm9A6p3HPEDIUntFAMi5"
consumer_secret = "KAsfjxxrh2qBbSGlZvrTlSaITh07XWlEBzhIPZ5LJf5sliwsrS"


#file = open('today.txt', 'a')

class CustomStreamListener(StreamListener):
    def on_status(self, status):
        print status.text

    def on_data(self, data):
        json_data = json.loads(data)
        print(json_data['tweet'])
        print type(json_data)
        #file.write(str(json_data))

    def on_error(self, status_code):
        print >> sys.stderr, 'Encountered error with status code:', status_code
        return True # Don't kill the stream

    def on_timeout(self):
        print >> sys.stderr, 'Timeout...'
        return True # Don't kill the stream



#This is a basic listener that just prints received tweets to stdout.
class StdOutListener(StreamListener):

    def on_data(self, data):
        json_data = json.loads(data)
        #print type(json_data)
        print(json_data['text'])
        #print json.loads(data)
        #file.write(str(json_data))
        #pprint(json_data)
        return True

    def on_error(self, status):
        print status


if __name__ == '__main__':

    #This handles Twitter authetification and the connection to Twitter Streaming API
    l = StdOutListener()
    auth = OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_token_secret)
    stream = Stream(auth, l)

    #This line filter Twitter Streams to capture data by userid
    stream.filter(follow=['744702845023326208'])