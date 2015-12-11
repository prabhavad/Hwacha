import json
# Social media controller layer


class socialMediaController(object): # concrete class

    # Constructor
   
    def addSm(self,smName):
        smList=self.displaySm()
        smList.append(smName)
        with open('smName.txt','w') as outfile:
            json.dump(smList,outfile)
    
    def rmSm(self,smName):
        smList=self.displaySm()
        smList.remove(smName)
        with open('smName.txt','w') as outfile:
            json.dump(smList,outfile)
        

    def displaySm(self):
       try:
           with open('smName.txt')as infile:
               return json.load(infile)
       except:
           return []

    def countSm(self):
        """ countSm() returns the number of social medias inside social media controller"""
        return len(self.display())



# a=socialMediaController()
# print type(a)
# a.addSm('mail')
# print a.displaySm()
# a.addSm('twitter')
# print a.displaySm()
# a.rmSm('mail')
# print a.displaySm()
