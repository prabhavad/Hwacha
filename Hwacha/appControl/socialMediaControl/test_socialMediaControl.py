import pytest
import socialMediaControl


def test_SmControl():
    smObject = socialMediaControl.socialMediaController()
    assert isinstance(smObject,socialMediaControl.socialMediaController)

def test_addSm():
    smObject = socialMediaControl.socialMediaController()
    retValue = smObject.addSm('facebook')
    retValue2 = smObject.addSm('twitter')
    assert retValue == True
    assert retValue2 == True

def test_rmSm():
    smObject = socialMediaControl.socialMediaController()
    retValue = smObject.rmSm('facebook')
    assert retValue == True

def test_rmSm2():
    smObject = socialMediaControl.socialMediaController()
    retValue = smObject.rmSm('NotInSmListName')
    assert retValue == False

def test_isSmAvailable():    
    smObject = socialMediaControl.socialMediaController()
    retValue = smObject.isSmAvailable('twitter')
    assert retValue == True

def test_isSmAvailable2():    
    smObject = socialMediaControl.socialMediaController()
    retValue = smObject.isSmAvailable('NotInSmlistName')
    assert retValue == False
