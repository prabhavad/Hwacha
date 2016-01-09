import tweepy
import smtplib

class BroadcastError(Exception):
    pass

class AuthenticationError(Exception):
    pass

class Broadcast(object): #Abstract class 
    
    def authentication(self,server):
        raise NotImplementedError()
    def push(self,message,server):
        raise NotImplementedError()
    

class TwitterBroadcast(Broadcast): #concrete class for twitter
    
        def __init__(self,consumerKey,consumerSecret,
                          accessToken,accessTokenSecret):
            

            self.consumerKey = consumerKey
            self.consumerSecret = consumerSecret
            self.accessToken = accessToken
            self.accessTokenSecret = accessTokenSecret
            
            
        def authentication(self,server=None):
            auth = tweepy.OAuthHandler(self.consumerKey,self.consumerSecret)
            auth.set_accessToken(self.accessToken,self.accessTokenSecret)
            api = tweepy.API(auth)
            return api

        def push(self,message,server):
           try:
               server.update_status(status=message)
           except tweepy.TweepError as e:
        #       raise BroadcastError(e[0][0]['message'],e[0][0]['code'])
               raise BroadcastError()               

            


class mailBroadcast(Broadcast): # mail concrete class

    def __init__(self,subject,to,consumerKey,consumerSecret) :
        self.subject = subject
        self.to = to
        self.gmailSender = consumerKey
        self.gmailPass = consumerSecret

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

        to = self.to

        BODY = '\r\n'.join([
               'To: %s' % self.to,
               'From: %s' % self.gmailSender,
               'subject: %s' % self.subject,
               '%s' % message
               ])
	
        #Sending the message
        try:
                server.sendmail(self.gmailSender,[to],BODY)
                server.quit()
                return "success"
	except Exception as exptn:
                server.quit()
                print exptn
                return "Error: unable to send email"

def init_twitter(message,key): # twitter key initialisation and broadcasting
    
    consumerKey = key['consumerKey']
    consumerSecret = key['consumerSecret']
    accessToken = key['accessToken']
    accessTokenSecret = key['accessTokenSecret']

    twitter=TwitterBroadcast(consumerKey,consumerSecret,accessToken,accessTokenSecret)
    key=twitter.authentication()
    status=twitter.push(message,key)
    return status


def init_mail(message,server,key): # mail initialisation
    
	toAddress = key['to']
	subject = key['subject']
        # Consumer key is the mail id of the sender and Consumer secret is the passphrase for it.
	consumerKey = key['consumerKey']
	consumerSecret = key['consumerSecret']
        
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


