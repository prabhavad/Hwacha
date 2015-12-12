# Social media controller layer

import json

class socialMediaController(object): # concrete class
   
    def addSm(self,smName):
        smList=self.displaySm()
        smList.append(smName)
        try:
            with open('smName.txt','w') as outfile:
                json.dump(smList,outfile)
            return "success"
        except: 
            return "failure"
    
    def rmSm(self,smName):
        smList=self.displaySm()
        try:
            smList.remove(smName)
            with open('smName.txt','w') as outfile:
                json.dump(smList,outfile)
            return "success"    
        except:
            return "failure"
        

    def displaySm(self):
       try:
           with open('smName.txt')as infile:
               return json.load(infile)
       except:
           return []

    def countSm(self):
        """ countSm() returns the number of social medias inside social media controller"""
        return len(self.displaySm())

    def isSmAvailable(self,smedia):
       with open('smName.txt')as infile:
           if (smedia in infile):
               return True
           else:
               return False

