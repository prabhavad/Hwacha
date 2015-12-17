# Hwacha Command Line Interface
import argparse
import sys
import appControl

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

parse=display()
results=parse.parse_args()
appObject=appControl.appController()



if results.message:
    if not results.smList:
        sys.exit("Exiting. Please select social media using '-b' option")
    else:
       print  appObject.broadcastMessage(results.message,results.smList)



if results.addList:
    
    currentList=appObject.getAvailableSmList()
    inputList=results.addList[:]
    
    for i in results.addList:
        
        if i in currentList:
            print "'%s' already in social Media List" %(i)
            inputList.remove(i)
    
    if appObject.addSm(inputList):
        print '\n'
        for i in inputList:
            print "Adding '%s' to Social Media list" %(i)


    print  '\nAvailable Social Media'
    print  20*'*'
    for i in appObject.getAvailableSmList():
        print i
    


if results.rmList:
    if appObject.removeSm(results.rmList):
        for i in results.rmList:
            print "Removing '%s' from Social Media list" %(i)
    print  'Available Social Media'+ appObject.getAvailableSmList()
    





