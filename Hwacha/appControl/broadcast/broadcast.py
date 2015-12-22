import tweepy
import smtplib

class BroadcastError(Exception):
    pass

class AuthenticationError(Exception):
    pass

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
               api.update_status(status=message)
           except tweepy.TweepError as e:
        #       raise BroadcastError(e[0][0]['message'],e[0][0]['code'])
               raise BroadcastError()               

            


class mailBroadcast(Broadcast): # mail concrete class

    def __init__(self,SUBJECT,TO,CONSUMER_KEY,CONSUMER_SECRET) :
        self.SUBJECT = SUBJECT
        self.TO = TO
        self.gmailSender = CONSUMER_KEY
        self.gmailPass = CONSUMER_SECRET

    def authentication(self,server):# authentication for the mail
        
        server.ehlo()
        server.starttls()
        server.ehlo()
        try:
            auth = server.login(self.gmailSender, self.gmailPass)
            return "success"
        except AuthenticationError as excptn:
            return "failure"

    def push(self,message,server) :

        TO = self.TO

        BODY = '\r\n'.join([
               'To: %s' % self.TO,
               'From: %s' % self.gmailSender,
               'Subject: %s' % self.SUBJECT,
               '%s' % message
               ])
	
        #Sending the message
        try:
                server.sendmail(self.gmailSender,[TO],BODY)
                server.quit()
                return "success"
	except Exception as exptn:
                server.quit()
                print exptn
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


def init_mail(message,server,key): # mail initialisation
    
	toAddress = key['to']
	subject = key['subject']
        # Consumer key is the mail id of the sender and Consumer secret is the passphrase for it.
	consumerKey = key['consumer_key']
	consumerSecret = key['consumer_secret']
        
	mail = mailBroadcast(subject,toAddress,consumerKey,consumerSecret)

        try:
            # Authentication for the mailBroadcaster
            login = mail.authentication(server)
            # push message
            if login == "success":
                sendMailStatus = mail.push(message,server)
            else:
                sendMailStatus = "login failure"
            return sendMailStatus
        except:
            return "Authentication failed"



def broadcastmessage(message,smList,key):
    statusMessage={}
    for sm in smList:
        if sm == 'mail':
            server = smtplib.SMTP('smtp.gmail.com',587)
            status = init_mail(message,server,key[sm])
            statusMessage[sm] = status
        
        elif sm == 'twitter':
            status = init_twitter(message,key[sm])
            statusMessage[sm] = status
    
    return statusMessage


