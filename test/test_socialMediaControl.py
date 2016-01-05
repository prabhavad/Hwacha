import pytest
from ..Hwacha.appControl.socialMediaControl import socialMediaControl
import mock
import json
import __builtin__
from mock import mock_open, patch

def test_SmControl():
    smObject = socialMediaControl.socialMediaController()
    assert isinstance(smObject,socialMediaControl.socialMediaController)


    
    

def test_addSm_1(monkeypatch):
    mock_json = mock.Mock()
    mock_open = mock.Mock()
    default_file = './appControl/socialMediaControl/smName.txt'
    mock_display = mock.Mock()
    mock_display.return_value = ['google']
    smObject = socialMediaControl.socialMediaController()
    mock_file = mock.Mock()
    mock_open.return_value = mock_file
   
    monkeypatch.setattr(smObject,'displaySm',mock_display) 
    monkeypatch.setattr(__builtin__,'open',mock_open)
    monkeypatch.setattr(json,'dump',mock_json)
    
    assert smObject.displaySm() == ['google']
    retValue = smObject.addSm(['facebook'])
    
    mock_open.assert_called_with(default_file,'w')
    mock_json.assert_called_with(['google','facebook'],mock_file)
    
    monkeypatch.undo()


def test_addSm_fail(monkeypatch):
    mock_json = mock.Mock()
    mock_open = mock.Mock()
    default_file = './appControl/socialMediaControl/smName.txt'
    mock_display = mock.Mock()
    mock_display.return_value = ''
    smObject = socialMediaControl.socialMediaController()
    mock_file = mock.Mock()
    mock_open.return_value = mock_file
   
    monkeypatch.setattr(smObject,'displaySm',mock_display) 
    monkeypatch.setattr(__builtin__,'open',mock_open)
    monkeypatch.setattr(json,'dump',mock_json)
    
    with pytest.raises(socialMediaControl.SocialMediaError):
        retValue = smObject.addSm('wrong type') 
    monkeypatch.undo()



def test_rmSm_1(monkeypatch):
    mock_json = mock.Mock()
    mock_open = mock.Mock()
    default_file = './appControl/socialMediaControl/smName.txt'
    mock_display = mock.Mock()
    mock_display.return_value = ['facebook']
    smObject = socialMediaControl.socialMediaController()
    mock_file = mock.Mock()
    mock_open.return_value = mock_file
   
    monkeypatch.setattr(smObject,'displaySm',mock_display) 
    monkeypatch.setattr(__builtin__,'open',mock_open)
    monkeypatch.setattr(json,'dump',mock_json)
    
    assert smObject.displaySm() == ['facebook']
    retValue = smObject.rmSm(['facebook'])
    
    mock_open.assert_called_with(default_file,'w')
    mock_json.assert_called_with([],mock_file)
    
    monkeypatch.undo()

