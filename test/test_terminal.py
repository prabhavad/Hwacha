import mock
import pytest
import sys
from ..Hwacha import terminalUi as ui
from ..Hwacha.appControl import appControl


def test_broadcastMessage():
    
    mock_list = mock.Mock()
    availableList = ['twitter']
    mock_list.return_value = availableList
    appObject=appControl.appController()

    org_function = appObject.getAvailableSmList
    appObject.getAvailableSmList = mock_list
    
    return_value = ui.BroadcastMessage('testing',['mail'])
    assert return_value == None

    appObject.getAvailableSmList = org_function




def test_broadcastMessage_exiting():
    mock_sys = mock.Mock()
    
    originalsys = sys.exit 
    sys.exit = mock_sys
    
    ui.BroadcastMessage('testing',[])
    assert sys.exit.called_with("Exiting. Please select social media using '-b' option")
    sys.exit = originalsys




def test_removeSocialMedia():
    
    mock_list = mock.Mock()
    mock_rm = mock.Mock()
    availableList = ['twitter']
    mock_list.return_value = availableList
    appObject=appControl.appController()

    org_get = appObject.getAvailableSmList
    appObject.getAvailableSmList = mock_list
    org_rm = appObject.removeSm
    appObject.removeSm = mock_rm
    return_value= ui.removeSocialMedia(['mail'])

    assert appObject.removeSm.called_with(['mail'])
    assert return_value == None

    return_value= ui.removeSocialMedia(['twitter'])
    assert appObject.removeSm.called_with([])
    assert return_value == None
    
    appObject.getAvailableSmList = org_get
    appObject.removeSm = org_rm


def test_removeSocialMedia():
    
    mock_list = mock.Mock()
    mock_add = mock.Mock()
    availableList = ['twitter']
    mock_list.return_value = availableList
    appObject=appControl.appController()

    org_get = appObject.getAvailableSmList
    appObject.getAvailableSmList = mock_list
    org_rm = appObject.removeSm
    appObject.addSm = mock_add
    return_value= ui.removeSocialMedia(['mail'])

    assert appObject.addSm.called_with(['mail'])
    assert return_value == None

    return_value= ui.removeSocialMedia(['twitter'])
    assert appObject.addSm.called_with([])
    assert return_value == None
    
    appObject.getAvailableSmList = org_get
    appObject.addSm = org_rm
