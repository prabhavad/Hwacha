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
            smMsg = results.message
            return smMsg
        except:
            return error

    def getSmList(self,raw_input):
         try:
            smList= results.smList
            return smList
         except:
            return error

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

            
