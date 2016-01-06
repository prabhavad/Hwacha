import mock
import pytest
from ..Hwacha.appControl import appControl
from ..Hwacha.appControl.socialMediaControl import socialMediaControl
from ..Hwacha.appControl.socialMediaControl import key_file
from  ..Hwacha.appControl.broadcast import broadcast





def test_isInSmList(monkeypatch):
    mock_social = mock.Mock()
    mock_social.return_value = True
    smObject = socialMediaControl.socialMediaController()
    monkeypatch.setattr(smObject,'isSmAvailable',mock_social)
    appObject = appControl.appController()
    retValue = appObject.isInSmList('facebook')
    #smObject.isSmAvailable.assert_called_with('facebook')
    assert retValue == False #-----50:50-----



def test_addSm():
    mock_s = mock.Mock()
    smObject = socialMediaControl.socialMediaController()
    org = smObject.addSm
    smObject.addSm =  mock_s 
    smObject.addSm.return_value = True
    appObject = appControl.appController()
    retValue = appObject.addSm(['facebook'])
    smObject.addSm.called_with(['facebook'])
    assert retValue == False


def test_getAvailable():
    mock_s = mock.Mock()
    smObject = socialMediaControl.socialMediaController()
    org = smObject.displaySm
    smObject.addSm =  mock_s 
    smObject.addSm.return_value = ['facebook']
    appObject = appControl.appController()
    retValue = appObject.getAvailableSmList()
    smObject.addSm.called_with()
    assert retValue == []



def test_removeSm():
    mock_s = mock.Mock()
    smObject = socialMediaControl.socialMediaController()
    org = smObject.rmSm
    smObject.addSm =  mock_s 
    smObject.addSm.return_value = True
    appObject = appControl.appController()
    retValue = appObject.removeSm(['facebook'])
    smObject.addSm.called_with(['facebook'])
    

def test_braodacast(monkeypatch):
    mock_broadcast = mock.Mock()
    mock_key =mock.Mock()
    monkeypatch.setattr(key_file,'key',mock_key)
    monkeypatch.setattr(broadcast,'broadcastmessage',mock_broadcast)
    appObject = appControl.appController()
    retValue = appObject.broadcastMessage('testing',['facebook'])
    
    mock_broadcast.assert_called_with('testing',['facebook'],mock_key)
    monkeypatch.undo()
    
    
    


 



