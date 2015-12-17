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
       
        rmList = []
        
        try:
            rmList.append(raw_input())
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
            smName = raw_input
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
            # return empty list is adding as a convension for failure. Reason for making [] as convension is broadcastStatus will always be a list
            return []

