import tweepy
# import key_file
# import wrong_key_file # wrong key file used for py.test purpose

class Broadcast(object):
    

    def authentication():
        raise NotImplementedError()
    def push():
        raise NotImplementedError()
    

class TwitterBroadcast(Broadcast):
    
        def __init__(self,CONSUMER_KEY,CONSUMER_SECRET,
                          ACCESS_TOKEN,ACCESS_TOKEN_SECRET):
            

            self.CONSUMER_KEY = CONSUMER_KEY
            self.CONSUMER_SECRET = CONSUMER_SECRET
            self.ACCESS_TOKEN = ACCESS_TOKEN
            self.ACCESS_TOKEN_SECRET = ACCESS_TOKEN_SECRET
            
            
        def authentication(self):
            auth = tweepy.OAuthHandler(self.CONSUMER_KEY,self.CONSUMER_SECRET)
            auth.set_access_token(self.ACCESS_TOKEN,self.ACCESS_TOKEN_SECRET)
            api = tweepy.API(auth)
            return api

        def push(self,api,message):
           try:
               api.update_status(message)
           except tweepy.TweepError as e:
               return  e[0][0]['code']

            

def pushmessage(message,sm,key):
    soc_media={'twitter':init_twitter(message,key),
               'mail':init_mail()#init_mail()
               }
    code = soc_media[sm]
    return code


def init_twitter(message,key):
    
    consumer_key = key['consumer_key']
    consumer_secret = key['consumer_secret']
    access_token = key['access_token']
    access_token_secret = key['access_token_secret']

    twitter=TwitterBroadcast(consumer_key,consumer_secret,access_token,access_token_secret)
    key=twitter.authentication()
    code=twitter.push(key,message)
    return code


def init_mail():
    pass



wrong_key={'consumer_key':'qB8HtMzPByguX9KUtqv',
     'consumer_secret': 'R8pyvLiKSDDTjyf84DnKVgM4IQLYTXq9fDdCbsq3vCEzXkC7qz',
     'access_token': '44725173veTAu0JKnBTkVobZZTG3KusZm8fFBUSXKw',
     'access_token_secret':'tUgPCP027HufEewBqdO45dCEz4Ga4IwqOmgo2brN'
     }


key={'consumer_key':'igjX6vqB8HtMzPByguX9KUtqv',
     'consumer_secret': 'R8pyvLiKSDDTjyf84DnKVgM4IQLYTXq9fDdCbsq3vCEzXkC7qz',
     'access_token': '4472517314-QveTAuRwPQ0JKnBTkVobZZTG3KusZm8fFBUSXKw',
     'access_token_secret':'XItUgPH1VCP027HufEewBqdO45dCEz4Ga4IwqOmgo2brN'
      }
print pushmessage('ultimaddd','twitter',wrong_key)
