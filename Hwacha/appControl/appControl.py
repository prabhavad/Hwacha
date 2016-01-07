# App controller layer
from socialMediaControl import socialMediaControl
from broadcast import broadcast
from socialMediaControl import key_file 

class appController(object): # concrete class

    

    def isInSmList(self,smName):
        smObject = socialMediaControl.socialMediaController()
        boolValue = smObject.isSmAvailable(smName)
        if boolValue == True:
            return True
        else:
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


