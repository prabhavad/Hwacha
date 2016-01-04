
# Test for broadcast

from ..Hwacha.appControl.broadcast import broadcast #path set
import pytest
import random
import mock
from mock import Mock
import tweepy
import smtplib
    
def test_twitter_broadcast():
      mock_update_status = mock.Mock()
      mock_authenticate = mock.Mock()
      api = mock.Mock()
      mock_authenticate.return_value = api
      original_update = api.update_status
      api.update_status = mock_update_status

      t = broadcast.TwitterBroadcast("test_consumer_key", 
                "test_consumer_secret", 
                "test_access_token",
                "test_access_token_secret")

      ret = t.push(api,'testing')
      api.update_status.assert_called_with(status='testing')
      
      api.update_status = api.update_status


def test_twitter_init():
      mock_broadcast = mock.Mock()
      mock_auth = mock.Mock()
      mock_push = mock.Mock()
      mock_key = mock.Mock()
      mock_message = mock.Mock()
      twitter = broadcast.TwitterBroadcast('consumer_key','consumer_secret','access_token','access_token_secret')
      original_auth = twitter.authentication
      twitter.authentication = mock_auth
      original_push = twitter.push
      twitter.push  = mock_push

      twitter.authentication.return_value = mock_key
      twitter.push.assert_called_with=(mock_key,mock_message)
     
      twitter.authentication = original_auth
      twitter.push = original_push
      



def test_twitter_auth():
    mock_oauthhandler = mock.Mock()
    mock_API = mock.Mock()
    mock_api = mock.Mock()
    mock_auth = mock.Mock()

    original_oauthhandler = tweepy.OAuthHandler
    original_API = tweepy.API
    tweepy.OAuthHandler = mock_oauthhandler
    tweepy.API = mock_API

    mock_oauthhandler.return_value = mock_auth
    mock_API.return_value = mock_api
    
    t = broadcast.TwitterBroadcast("test_consumer_key", 
                "test_consumer_secret", 
                "test_access_token",
                "test_access_token_secret")

    ret = t.authentication()
    tweepy.OAuthHandler.assert_called_with("test_consumer_key", "test_consumer_secret")
    mock_auth.set_access_token.assert_called_with("test_access_token", "test_access_token_secret")
    tweepy.API.assert_called_with(mock_auth)
    assert ret == mock_api
    
    tweepy.OAuthHandler = original_oauthhandler
    tweepy.API = original_API



def test_init_twitter():
      key = {'consumer_key':'test',
             'consumer_secret':'test','access_token':'test','access_token_secret':'test'}
      mock_broadcast = mock.Mock()
      mock_auth= mock.Mock()
      mock_push = mock.Mock()
      mock_auth_key = mock.Mock() 
      mock_auth.return_value = mock_auth_key
      mock_br = mock.Mock()
      mock_broadcast.return_value = mock_br


      original_TwitterBroadcast = broadcast.TwitterBroadcast
      broadcast.TwitterBroadcast = mock_broadcast
      original_auth = mock_br.authentication
      mock_br.authentication = mock_auth
      original_push = mock_br.push 
      mock_br.push = mock_push

      broadcast.init_twitter('testing',key)
      broadcast.TwitterBroadcast.assert_called_with('test','test','test','test')
      mock_br.authentication()
      mock_br.push.assert_called_with(mock_auth_key,'testing')

      


def test_mailBroadcast():
    mock_server = Mock()
    mock_subject = Mock()
    mock_to = Mock()
    mock_sender = Mock()
    mock_pass = Mock()
    mailObject = broadcast.mailBroadcast(mock_subject, mock_to, mock_sender, mock_pass)
    retAuthValue = mailObject.authentication(mock_server)
    assert retAuthValue == "success"
    mock_server.login.assert_called_with(mock_sender, mock_pass)
    retPushValue = mailObject.push("hello",mock_server)
    assert retPushValue == "success"
    assert mock_server.ehlo.called
    assert mock_server.starttls.called

def test_mailBroadcast_auth_failure():
    mock_server = Mock()
    mock_server.login = Mock()
    mock_server.login.side_effect = broadcast.AuthenticationError()
    mock_subject = Mock()
    mock_to = Mock()
    mock_sender = Mock()
    mock_pass = Mock()
    mailObject = broadcast.mailBroadcast(mock_subject, mock_to, mock_sender, mock_pass)
    #with pytest.raises(broadcast.AuthenticationError):
    retAuthValue =mailObject.authentication(mock_server)
    assert retAuthValue == "failure"
	
    
def test_authentication():
    mock = Mock()
    mock.authentication()
    mock.return_value = "True"
    mock.authentication.assert_called_with()

    



def test_broadcast_message():
     
      key ={
            'twitter':{'consumer_key' : 'test',
                       'consumer_secret':'test',
                       'access_token':'test',
                       'access_token_secret':'test'},
            'mail':{'subject':'Test Subject', 
                    'to':'test',
                    'consumer_key':'test', 
                    'consumer_secret':'test'}
      }


      sm_list = ['mail','twitter']
      mock_smtp = mock.Mock()
      mock_server = mock.Mock()
      mock_smtp.return_value = mock_server
      mock_mail = mock.Mock()
      mock_twitter = mock.Mock()

      original_mail = broadcast.init_mail
      broadcast.init_mail = mock_mail
      
      original_twitter = broadcast.init_twitter
      broadcast.init_twitter = mock_twitter
      
      original_smtp = smtplib.SMTP
      smtplib.SMTP = mock_smtp
      



      broadcast.broadcastmessage('testing',sm_list,key)
      smtplib.SMTP.assert_called_with('smtp.gmail.com',587)
      broadcast.init_mail.assert_called_with('testing',mock_server,key['mail'])
      broadcast.init_twitter.assert_called_with('testing',key['twitter'])

      smtplib.SMTP = original_smtp
      broadcast.init_mail = original_mail
      broadcast.init_twitter = original_twitter
      
      
      
