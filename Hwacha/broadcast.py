import tweepy
import smtplib

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

            


class mailBroadcast(Broadcast): # mail concrete class

    def __init__(self,SUBJECT,TO,CONSUMER_KEY,CONSUMER_SECRET) :
        self.SUBJECT = SUBJECT
        self.TO = TO
        self.CONSUMER_KEY = CONSUMER_KEY
        self.CONSUMER_SECRET = CONSUMER_SECRET

    def authentication(self):
        auth = SMTP.login(self.CONSUMER_KEY, self.CONSUMER_SECRET)
        return auth

    def verification(self,CONSUMER_KEY):
        server = smtplib.SMTP('mail')
        server.set_debuglevel(True)
        try:
            username_result = server.verify('username')
        finally:
            server.quit()
        print 'username: {}'.format('username_result')


    def push(self,message) :

        #Setting Gmail Credentials
        gmailSender = self.CONSUMER_KEY
        gmailPass = self.CONSUMER_SECRET

        #Create connection to gmail server
        server = smtplib.SMTP('smtp.gmail.com',587)
        server.ehlo()
        server.starttls()
        server.ehlo()
        server.login(gmailSender, gamilPass)

        BODY = '\r\n'.join([
               'To: %s' % self.TO,
               'From: %s' % gmailSender,
               'Subject: %s' % self.SUBJECT,
               '%s' % message
               ])
	
        #Sending the message
        try:
            server.sendmail(gmailSender,[TO],BODY)
            server.quit()
            return "success"
        except:
            server.quit()
            return "Error: unable to send email"

        
			

def init_twitter(message,key): # twitter key initialisation and broadcasting
    
    consumer_key = key['consumer_key']
    consumer_secret = key['consumer_secret']
    access_token = key['access_token']
    access_token_secret = key['access_token_secret']

    twitter=TwitterBroadcast(consumer_key,consumer_secret,access_token,access_token_secret)
    key=twitter.authentication()
    status=twitter.push(key,message)
    return status


def init_mail(message,key): # mail initialisation
    
	toAddress = key['to']
	subject = key['subject']
        # Consumer key is the mail id of the sender and Consumer secret is the passphrase for it.
	consumerKey = key['consumer_key']
	consumerSecret = key['consumer_secret']

	mail = mailBroadcast(subject,toAddress,consumerKey,consumerSecret)
	sendMailStatus = mail.push(message)
	return sendMailStatus



def broadcastmessage(message,sm,key):

    if sm == 'mail':
        status = init_mail(message,key)
    elif sm == 'twitter':
        status = init_twitter(message,key)


    return status
    


