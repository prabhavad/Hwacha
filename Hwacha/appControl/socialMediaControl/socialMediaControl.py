# Social media controller layer

import json,os


class SocialMediaError(Exception):
    pass

class socialMediaController(object): # concrete class
   
    def addSm(self,addList):
        try:    
            smList=self.displaySm()
            for i in addList:
                if i not in smList:
                    smList.append(i)

            default_file = './appControl/socialMediaControl/smName.txt'
            outfile =  open(default_file,'w')
            json.dump(smList,outfile)
        except: 
             raise SocialMediaError()

    
    def rmSm(self,rmList):
        smList=self.displaySm()
        try:
            for i in rmList:
                if i in smList:
                    smList.remove(i)
            default_file = './appControl/socialMediaControl/smName.txt'    
            
            outfile = open(default_file,'w')
            json.dump(smList,outfile)
        except: 
            raise SocialMediaError()
       

    def displaySm(self):

        default_file = './appControl/socialMediaControl/smName.txt'
        try:
            infile = open(default_file)
            return json.load(infile)
        except:
           return []

    
    def countSm(self):
        """ countSm() returns the number of social medias inside social media controller"""
        return len(self.displaySm())

    def isSmAvailable(self,smedia):
        try:
            if (smedia in self.displaySm()):
                return True
            else:
                return False
        except:
            raise SocialMediaError()


