import pytest
import appControl

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
