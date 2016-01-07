# Hwacha Command Line Interface
import argparse
import sys
from appControl import appControl


def display():
    try: 
        parse = argparse.ArgumentParser()
        parse.add_argument('-m','--message',action='store',
                           help='Message to broadcast.')
        parse.add_argument('-b','--broadcast',action='append',dest='smList',
                           help = 'Add social media into broadcast list')
        parse.add_argument('-a','--add',action='append',dest='addList',
                           help = 'Add social media to Hwacha')
        parse.add_argument('-r','--remove',action='append',dest='rmList',
                           help = 'Remove social media from Hwacha')
        
        if len(sys.argv) == 1:
           sys.exit(1)
    except:
        parse.print_help()
        sys.exit("Exiting. Read help for further information 'python ui.py --help'") 
    return parse


def addSocialMedia(addList):
    appObject=appControl.appController()
    currentList=appObject.getAvailableSmList()
    inputList=addList[:]
    
    for i in addList:
        if i in currentList:
            print "'%s' already in social Media List" %(i)
            inputList.remove(i)
    
    if inputList:
        appObject.addSm(inputList)
        print '\n'
        for i in inputList:
                print "Adding '%s' to Social Media list" %(i)


    print  '\nAvailable Social Media'
    print  20*'*'
    for i in appObject.getAvailableSmList():
        print i
    


def removeSocialMedia(rmList):    
    appObject=appControl.appController()
    currentList = appObject.getAvailableSmList()
    inputList = rmList[:]
    for i in rmList:
        if i not in currentList:
               print "'%s' not in Social Media list" %(i)
               inputList.remove(i)
       
    if appObject.removeSm(inputList):
        for i in inputList:
            print "Removing '%s' from Social Media list" %(i)
    
    
    print  'Available Social Media' 
    print 20*'*'
    for i in appObject.getAvailableSmList():
        print i


def BroadcastMessage(message,smList):
        appObject=appControl.appController()

        if not smList:
            sys.exit("Exiting. Please select social media using '-b' option")
        else:
           currentList = appObject.getAvailableSmList()
           inputList=smList[:]
           for i in smList:
               if i not in currentList:
                   print "%s not in Social Media List, Please add using '-b' option" %(i)
                   inputList.remove(i)
           
           status= appObject.broadcastMessage(message,inputList)
           print  'Status'
           print 20*'*'
           for key in status:
               print ' %s : %s ' %(key,status[key])






if __name__ == '__main__':

    parse=display()
    results=parse.parse_args()
    appObject=appControl.appController()

    if results.addList:
        addSocialMedia(results.addList)

    if results.rmList:
        removeSocialMedia(results.rmList)

    if results.message:
        BroadcastMessage(results.message,results.smList)







