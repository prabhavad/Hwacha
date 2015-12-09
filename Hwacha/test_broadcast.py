import broadcast
import pytest
import random
from mock import Mock

def test_broadcst():
    key={'consumer_key':'igjX6vqB8HtMzPByguX9KUtqv',
     'consumer_secret': 'R8pyvLiKSDDTjyf84DnKVgM4IQLYTXq9fDdCbsq3vCEzXkC7qz',
     'access_token': '4472517314-QveTAuRwPQ0JKnBTkVobZZTG3KusZm8fFBUSXKw',
     'access_token_secret':'XItUgPH1VCP027HufEewBqdO45dCEz4Ga4IwqOmgo2brN',
      }
    soc_media= 'twitter'
    error_code = None
    message='Hello Hwacha'+str(random.random()) # random message
    push = broadcast.broadcastmessage(message,soc_media,key) 
    assert push == error_code
    

def test_broadcst2():

    wrong_key = {'consumer_key':'qB8HtMzPByguX9KUtqv',
     'consumer_secret': 'R8pyvLiKSDDTjyf84DnKVgM4IQLYTXq9fDdCbsq3vCEzXkC7qz',
     'access_token': '44725173veTAuRwPQ0JKnBTkVobZZTG3KusZm8fFBUSXKw',
     'access_token_secret':'tUgPH1VCP027HufEewBqdO45dCEz4Ga4IwqOmgo2brN'
     }
    soc_media= 'twitter'
    error_code = 89
    
    push = broadcast.broadcastmessage('Hello Hwach',soc_media,wrong_key)
    print push
    assert push == error_code

def test_mailBroadcast():

	key = {'subject':'Test Subject', 'to':'simsarulhaqv@gmail.com', 'consumer_key':'simsar012smtp@gmail.com', 'consumer_secret':'givecorrectPasshere'}
	soc_media = 'mail'
	code = "Error: unable to send email"

	push_return = broadcast.broadcastmessage('Hello',soc_media,key)
	assert push_return == code 
	
    
def test_authentication():
    mock = Mock()
    mock.authentication()
    mock.return_value = "SMTPAuthenticationError"
    mock.authentication.assert_called_with()

def test_verification():
    mock = Mock()
    mock.verification()
    mock.attribute = True
    mock.verification.assert_called_with()
    
