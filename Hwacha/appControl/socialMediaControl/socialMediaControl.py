# Social media controller layer

import json,os


class SocialMediaError(Exception):
    pass

class socialMediaController(object): # concrete class
   
    def addSm(self,addList):
        smList=self.displaySm()
        for i in addList:
            if i not in smList:
                smList.append(i)
        
       

        try:
            default_file = './appControl/socialMediaControl/smName.txt'
            if os.path.isfile(default_file):
                with open(default_file,'w') as outfile:
                        json.dump(smList,outfile)
                        return True
            else:
                with open('smName.txt','w') as outfile:
                        json.dump(smList,outfile)
                        return True

        except: 
            raise SocialMediaError()

    
    def rmSm(self,rmList):
        smList=self.displaySm()
        try:
            for i in rmList:
                smList.remove(i)
            default_file = './appControl/socialMediaControl/smName.txt'    
            if os.path.isfile(default_file):
                with open(default_file,'w') as outfile:
                        json.dump(smList,outfile)
                        return True
            else:
                with open('smName.txt','w') as outfile:
                        json.dump(smList,outfile)
                        return True

        except: 
            raise SocialMediaError()
       

    def dropSm(self,rmList):
        data=[]
        try:
            with open('smName.txt','w') as outfile:
                json.dump(data,outfile)
            return True 
        except:
            raise SocialMediaError()



    def displaySm(self):

        default_file = './appControl/socialMediaControl/smName.txt'
        try:
            if os.path.isfile(default_file):
                with open('./appControl/socialMediaControl/smName.txt')as infile:
                   return json.load(infile)
            else:
                with open('smName.txt')as infile:
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


