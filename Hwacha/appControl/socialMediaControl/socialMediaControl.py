# Social media controller layer

import json

class socialMediaController(object): # concrete class
   
    def addSm(self,addList):
        smList=self.displaySm()
        for i in addList:
            if i not in smList:
                smList.append(i)
        try:
            with open('smName.txt','w') as outfile:
                json.dump(smList,outfile)
            return True
        except: 
            return False
    
    def rmSm(self,rmList):
        smList=self.displaySm()
        try:
            for i in rmList:
                smList.remove(i)


            with open('smName.txt','w') as outfile:
                json.dump(smList,outfile)
            return True    
        except:
            return False
        
    def dropSm(self,rmList):
        data=[]
        try:
            with open('smName.txt','w') as outfile:
                json.dump(data,outfile)
            return True    
        except:
            return False



    def displaySm(self):
       try:
           with open('smName.txt')as infile:
               return json.load(infile)
       except:
           return []

    def countSm(self):
        """ countSm() returns the number of social medias
        inside social media controller"""
        return len(self.displaySm())

    def isSmAvailable(self,smedia):
        try:
            with open('smName.txt') as infile:
                if (smedia in self.displaySm()):
                    return True
                else:
                    return False
        except:
            return False


