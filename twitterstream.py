from tweepy import Stream
from tweepy import OAuthHandler
from tweepy.streaming import StreamListener
import json

#the keys can be obtained through twitter
ckey = "ckey"
csecret = "csecret"
atoken = "atoken"
asecret = "asecret"


class listener(StreamListener):
    def on_data(self, data):
        # tweet = data.split(',"text":"')[1].split('","source')[0]
        try:
            all_data = json.loads(data)
            tweet = all_data['text']
            output = open('output.csv','a')
            output.write('TwEeT: '+tweet.rstrip('\n')+'\n')
            output.close()
        except:
            print("Could not load data")
        return True

    def on_error(self, status):
        print(status)


auth = OAuthHandler(ckey, csecret)
auth.set_access_token(atoken, asecret)
twitterStream = Stream(auth, listener())
twitterStream.filter(track=["Bernie Sanders","#bernie","Sanders","#Bernie2016", "@berniesanders","#feelthebern",
                            "Hillary Clinton","@HillaryClinton","Clinton",
                            "Donald Trump","Trump",  "@realDonaldTrump",
                            "Senator Ted Cruz","Ted Cruz","Senator Ted Cruz","SenTedCruz",
                            "Democrat", "Republican"
                            ],async=True)
