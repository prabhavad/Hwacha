
import pytest
#import socialMediaControl
from .. import appControl



def test_getSmName():
    appObject = appControl.appController()
    retValue = appObject.getSmName(lambda: "Facebook")
    assert retValue == "Facebook"


def test_getSmUserName():
    appObject = appControl.appController()
    retValue = appObject.getSmUserName(lambda: "fb_uname")
    assert retValue == "fb_uname"

def test_getSmUserPasswd():
    appObject = appControl.appController()
    retValue = appObject.getSmUserPasswd(lambda: "fbpwd12#3")
    assert retValue == "fbpwd12#3"

#def test_isInSmList():
 #   appObject = appControl.appController()
 #    smObject = socialMediaControl.socialMediaController()
 #   retAdd = smObject.addSm('twitter')
 #   retValue = appObject.isInSmList(lambda: 'twitter')
 #   assert retValue == True
    
