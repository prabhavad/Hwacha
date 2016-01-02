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





def test_broadcastMessage_exiting():
    mock_sys = mock.Mock()
    
    originalsys = sys.exit 
    sys.exit = mock_sys
    
    ui.BroadcastMessage('testing',[])
    assert sys.exit.called_with("Exiting. Please select social media using '-b' option")
    sys.exit = originalsys


