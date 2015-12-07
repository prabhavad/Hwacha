import tweepy
import smtplib

from email.mime.text import MIMEText

class Broadcast(object): #Abstract class 
    
    def authentication():
        raise NotImplementedError()
    def push():
        raise NotImplementedError()
    

class TwitterBroadcast(Broadcast): #concrete class for twitter
    
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

            


class mailBroadcast(Broadcast): #dummy mail concrete class

		def __init__(self,MESSAGE,SUBJECT,FROM,TO) :
			self.MESSAGE = MESSAGE
			self.SUBJECT = SUBJECT
			self.FROM = FROM
			self.TO = TO

    	def push(self) :
			msg = MIMEText(self.MESSAGE)
			msg['Subject'] = self.SUBJECT
			msg['From'] = self.FROM
			msg['To'] = self.TO 
	
			#Sending the message via once own SMTP server
			sendObject = smtplib.SMTP('localhost')
			sendObject.sendmail(self.FROM,[self.TO], msg.as_string())
			sendObject.quit()
			return 1

			

def init_twitter(message,key): # twitter key initialisation and broadcasting
    
    consumer_key = key['consumer_key']
    consumer_secret = key['consumer_secret']
    access_token = key['access_token']
    access_token_secret = key['acces s_token_secret']

    twitter=TwitterBroadcast(consumer_key,consumer_secret,access_token,access_token_secret)
    key=twitter.authentication()
    code=twitter.push(key,message)
    return code


def init_mail(message,key): #dummy mail initialisation
    
	fromAddress = key['from']
	toAddress = key['to']
	subject = key['subject']

	mail = mailBroadcast(message,subject,fromAddress,toAddress)
	sendMailStatus = mail.push()
	return sendMailStatus



def broadcastmessage(message,sm,key):
    soc_media={'twitter':init_twitter(message,key),
               'mail':init_mail(message,key)
               }
    code = soc_media[sm]
    return code





