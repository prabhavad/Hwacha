# App controller layer
from socialMediaControl import socialMediaControl
from broadcast import broadcast
from socialMediaControl import key_file 

class appController(object): # concrete class

    def getSmName(self,smName):
        try:
            return smName
        except:
            return "Failed"

    def getSmUserName(self,smUserName):
        try:
            return smUserName
        except:
            return "Failed"

    def getSmUserPasswd(self,smPwd):
         try:
            return smPwd
         except:
            return "Failed"

    def getMessage(self,smMsg):
        try:
            return smMsg
        except:
            return "Failed"


    def getAddList(self, smName):
        addList = []
        try:
           addList.append(smName)
           return addList
        except:
            return "Failed"

    def getRmList(self, smName):
       
        rmList = []
        
        try:
            rmList.append(smName)
            return rmList
        except:
            return "Failed"
            

    def getSmList(self, smList):
         try:
            return smList
         except:
            return "Failed"

    def isInSmList(self,smName):
        try:
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
            broadcastStatus = broadcast.broadcastmessage(message,smList,key)
            return broadcastStatus
        except:
            # return empty Dict is adding as a convension for failure. Reason for making  as convension is broadcastStatus will always be a list
            return {}

