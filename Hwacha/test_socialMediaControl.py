import pytest
import socialMediaControl

def test_countSm():
    smObject = socialMediaControl.socialMediaController()
    count = smObject.countSm()
    assert count == 0

def test_displaySm():
    smObject = socialMediaControl.socialMediaController()
    returnVal = smObject.displaySm()
    assert returnVal == []


    
