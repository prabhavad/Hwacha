import sys, os
myPath = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, myPath + '/../broadcast/')

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

	key = {'subject':'Test Subject', 'to':'simsar009@gmail.com', 'consumer_key':'simsar012smtp@gmail.com', 'consumer_secret':'newPass295'}
	soc_media = 'mail'
	code = "success"

	push_return = broadcast.broadcastmessage('Hello',soc_media,key)
	assert push_return == code 

def test_mailBroadcast2():

	key = {'subject':'Test Subject', 'to':'simsar009@gmail.com', 'consumer_key':'simsar012smtp@gmail.com', 'consumer_secret':'wrongPass123'}
	soc_media = 'mail'
	code = "Authentication failed"

	push_return = broadcast.broadcastmessage('Hello',soc_media,key)
	assert push_return == code
	
    
def test_authentication():
    mock = Mock()
    mock.authentication()
    mock.return_value = "True"
    mock.authentication.assert_called_with()

    

