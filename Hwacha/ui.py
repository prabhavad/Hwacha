#sample command line ui unit
import argparse


parse = argparse.ArgumentParser()
parse.add_argument('-m','--message',action='store',
                     help='message to broadcast')
parse.add_argument('-b','--broadcast',action='append',dest='smList',
                     help = 'add social media to to braodcast list')
parse.add_argument('-a','--add',action='append',dest='addList',
                      help = 'add social media to Hwatcha')
parse.add_argument('-r','--remove',action='append',dest='rmList',
                      help = 'remove social media from Hwatcha' )


results=parse.parse_args()
print 'message =',results.message
print 'smList =',results.smList
print 'addList =',results.addList
print 'rmList =',results.rmList





