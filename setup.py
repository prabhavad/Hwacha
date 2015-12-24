from setuptools import setup

setup( name ='Hwacha',
       version = '0.1',
       description = ' Message broadcasting system',
       url ='https://github.com/shamlikt/Hwacha',
       author = 'Team Hwacha',
       author_email='Hwacha_11@gmail.com',
       license='BSD',
       packages=['Hwacha'],
       install_requires=['tweepy','pytest','mock','python-wordpress-xmlrpc'],
       zip_safe=False
       )
