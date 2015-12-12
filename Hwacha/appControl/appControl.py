# App controller layer

class appController(object): # concrete class

    def getSmName(self,raw_input):
        smName = raw_input()
        return smName

    def getSmUserName(self,raw_input):
        try:
            smUserName= raw_input()
            return smUserName
        except:
            return error

    def getSmUserPasswd(self,raw_input):
         try:
            smPwd= raw_input()
            return smPwd
         except:
            return error

    def getMessage(self,raw_input):
        try:
            smMsg= raw_input()
            return smMsg
        except:
            return error

    def getSmList(self):
         try:
            smPwd= raw_input()
            return smPwd
         except:
            return error

    def isInSmList(self):
        pass
