# App controller layer
from socialMediaControl import socialMediaControl
from broadcast import broadcast
from socialMediaControl import key_file 

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


    def getAddList(self, raw_input):
        addList = []
        try:
           addList.append(raw_input())
           return addList
        except:
            return "Failed"

    def getRmList(self, raw_input):
        # This is temporary, remove this line before using
        rmList = ["fb","mail"]
        # Remove above line before using as an API
        try:
            rmList.remove(raw_input())
            return rmList
        except:
            return "Failed"
            

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

    def addSm(self,smList):
        try:
            smObject = socialMediaControl.socialMediaController()
            smList = smObject.addSm(smList)
            return True
        except:
            return False

    def removeSm(self,smList):
        try:
            smObject = socialMediaControl.socialMediaController()
            smList = smObject.rmSm(smList)
            return True
        except:
            return False

    def broadcastMessage(self,message,smList):
        key=key_file.key
        try:
            bcstatus = broadcast.broadcastmessage(message,smList,key)
            return bcstatus
        except:
            return False
    def broadcaster(self,message,smList,key):
        try:
            retValue = broadcast.broadcastmessage(message,smList,key)
        except:
            retValue = "Failed"
        return retValue

    def getKey(self,raw_input):
        try:
            key = raw_input()
            return key
        except:
            return "Failed"
