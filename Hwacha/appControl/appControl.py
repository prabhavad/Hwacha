# App controller layer

import sys, os
myPath = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, myPath + '/socialMediaControl/' + '/broadcast/')

class appController(object): # concrete class

    def getSmName(self,raw_input):
        smName = raw_input()
        return smName

    def getSmUserName(self):
        pass

    def getSmUserPasswd(self):
        pass

    def getMessage(self):
        pass

    def getSmList(self):
        pass

    def isInSmList(self):
        pass
