# App controller layer

import sys, os
myPath = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, myPath + '/socialMediaControl/' + '/broadcast/')

#import socialMediaControl


class appController(object): # concrete class

    def getSmName(self,raw_input):
        try:
            smName = raw_input()
            return smName
        except:
            return "Failed"

    def getSmUserName(self,raw_input):
        try:
            smUserName= raw_input()
            return smUserName
        except:
            return "Failed"

    def getSmUserPasswd(self,raw_input):
         try:
            smPwd= raw_input()
            return smPwd
         except:
            return "Failed"

    def getMessage(self,raw_input):
        try:
            smMsg= raw_input()
            return smMsg
        except:
            return error

    def getSmList(self,raw_input):
         try:
            smList= raw_input()
            return smList
         except:
            return error



#    def isInSmList(self,raw_input):
#        try:
#            smName = raw_input()
#            boolValue = socialMediaController.isSmAvailable(smName)
#            if boolValue == True:
#                return True
#            else:
#                return False
#        except:
#            return False

    def isInSmList(self,smedia):
        try:
            if smedia in smList :
                return True
            else :
                return False
        except:
            return False
        

