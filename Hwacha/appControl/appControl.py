# App controller layer
from socialMediaControl import socialMediaControl

class appController(object): # concrete class

    def getSmName(self,raw_input):
        try:
            smName = raw_input()
            return smName
        except:
            return "Failed"

    def getSmUserName(self,raw_input):
        try:
            smUserName = raw_input()
            return smUserName
        except:
            return "Failed"

    def getSmUserPasswd(self,raw_input):
         try:
            smPwd = raw_input()
            return smPwd
         except:
            return "Failed"

    def getMessage(self,raw_input):
        try:
            smMsg = raw_input()
            return smMsg
        except:
            return "Failed"
<<<<<<< HEAD
        
=======

>>>>>>> 0ba22edb0243ccb11edb3a496f692886fb9519ba
    def getAddList(self, raw_input):
        addList = []
        try:
<<<<<<< HEAD
           addList.append(raw_input())
           return addList
        except:
            return "Failed"
        
=======
           addList = addList.append(raw_input())
           return addList
        except:
            return "Failed"

>>>>>>> 0ba22edb0243ccb11edb3a496f692886fb9519ba
    def getRmList(self, raw_input):
        rmList = ["fb","mail"]
        try:
            rmList.remove(raw_input())
            return rmList
        except:
            return "failed"
            

    def getSmList(self,raw_input):
         try:
            smList= raw_input()
            return smList
         except:
            return "Failed"

    def isInSmList(self,raw_input):
        try:
            smName = raw_input()
            smObject = socialMediaControl.socialMediaController()
            boolValue = smObject.isSmAvailable(smName)
            if boolValue == True:
                return True
            else:
                return False
        except Exception as excpt:
            return False

    def getAvailableSmList(self):
        try:
            smObject = socialMediaControl.socialMediaController()
            smList = smObject.displaySm()
            return smList
        except:
            return []
