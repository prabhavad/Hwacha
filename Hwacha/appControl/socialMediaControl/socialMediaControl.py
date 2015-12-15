# Social media controller layer

import json


class socialMediaController(object): # concrete class
   
    def addSm(self):
        smList=self.displaySm()
        smList.append(results.addList)
        try:
            with open('smName.txt','w') as outfile:
                json.dump(smList,outfile)
            return True
        except: 
            return False
    
    def rmSm(self):
        smList=self.displaySm()
        try:
            smList.remove(results.rmList)
            with open('smName.txt','w') as outfile:
                json.dump(smList,outfile)
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
        """ countSm() returns the number of social medias inside social media controller"""
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


