# Hwacha Command Line Interface
import argparse
import sys


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
print 'message =',results.message
print 'smList =',results.smList
print 'addList =',results.addList
print 'rmList =',results.rmList





