# Social media controller layer

class socialMediaController(object): # concrete class

    # Constructor
    def __init__(self):
        self.socialMediaDetail = []

    def addSm(self):
        pass

    def rmSm(self):
        pass

    def displaySm(self):
        return self.socialMediaDetail

    def countSm(self):
        """ countSm() returns the number of social medias inside social media controller"""
        self.count=0
        for item in self.socialMediaDetail:
            self.count = self.count + 1
        return self.count

    def isSmAvailable(self):
        pass
