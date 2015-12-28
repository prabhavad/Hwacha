import mock
import pytest
from ..Hwacha.appControl import appControl
from ..Hwacha.appControl.socialMediaControl import socialMediaControl

def test_getSmName():
    appObject = appControl.appController()
    retValue = appObject.getSmName(lambda: "Facebook")
    assert retValue == "Facebook"


def test_getSmUserName():
    Object= appControl.appController()
    retValue = Object.getSmUserName(lambda: "fb_uname")
    assert retValue == "fb_uname"

def test_getSmUserPasswd():
    Object= appControl.appController()
    retValue=Object.getSmUserPasswd(lambda: "fbpwd12#3")
    assert retValue == "fbpwd12#3"

def test_getMessage():
    Object= appControl.appController()
    retValue=Object.getMessage(lambda: "This is a test message")
    assert retValue == "This is a test message"

def test_getAddList():
    Object= appControl.appController()
    retValue=Object.getAddList(lambda: "Mail")
    assert retValue == ["Mail"]

def test_getRmList():
    Object= appControl.appController()
    retValue=Object.getRmList(lambda: "Mail")
    assert retValue == ["Mail"]
    
def test_getSmList():
    Object= appControl.appController()
    retValue=Object.getSmList(lambda: "Twitter Facebook Gmail Tumblr")
    assert retValue == "Twitter Facebook Gmail Tumblr"

def test_isInSmList():
    appObject = appControl.appController()
    smObject = socialMediaControl.socialMediaController()
    retAdd = smObject.addSm(['twitter','facebook'])
    retValue = appObject.isInSmList('facebook')
    assert retValue == True

def test_isInSmList2():
    appObject = appControl.appController()
    smObject = socialMediaControl.socialMediaController()
    retAdd = smObject.addSm(['twitter','facebook'])
    retValue = appObject.isInSmList('mail')
    assert retValue == False

def test_addSm():
    appObject = appControl.appController()
    retValue = appObject.addSm('Mail')
    assert retValue == True

def test_getAvailableSmList():
    smObject = socialMediaControl.socialMediaController()
    appObject = appControl.appController()
    retValue = appObject.getAvailableSmList()
    assert retValue == smObject.displaySm()

    
def test_removeSm():
    sm_object = mock.Mock()
    sm_object.rmSm = mock.MagicMock(return_value = True)
    
    original = appControl.socialMediaControl.socialMediaController
    appControl.socialMediaControl.socialMediaController = sm_object 
    
    app_object = appControl.appController()
    value = app_object.removeSm(['twitter'])
#    sm_object.rmSm.assert_called_with(['twitter'])
    assert value == True
    appControl.socialMediaControl.socialMediaController = original

