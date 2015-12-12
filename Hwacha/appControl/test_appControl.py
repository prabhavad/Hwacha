import sys, os
myPath = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, myPath + '/../appControl/')
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

def test_getMessage():
    Object= appControl.appController()
    retValue=Object.getMessage(lambda: "This is a test message")
    assert retValue == "This is a test message"

def test_getSmList():
    Object= appControl.appController()
    retValue=Object.getSmList(lambda: "Twitter Facebook Gmail Tumblr")
    assert retValue == "Twitter Facebook Gmail Tumblr"

    

    
