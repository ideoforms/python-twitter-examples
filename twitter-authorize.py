#!/usr/bin/python

#-----------------------------------------------------------------------
# twitter-authorize:
#  - step through the process of creating and authorization a
#    Twitter application.
#-----------------------------------------------------------------------

import twitter
import time

print "1. Create a new Twitter application here: https://apps.twitter.com"
print "When you have created the application, enter:"
print "   your application name: ",
app_name = raw_input()

print "   your consumer key: ",
consumer_key = raw_input()

print "   your consumer secret: ",
consumer_secret = raw_input()

print "2. Now, authorize this application."
print "You'll be forwarded to a web browser in two seconds."
print

time.sleep(2)

access_key, access_secret = twitter.oauth_dance(app_name, consumer_key, consumer_secret)

print "Done."
print
print "Now, replace the credentials in config.py with the below:"
print
print "consumer_key = '%s'" % consumer_key
print "consumer_secret = '%s'" % consumer_secret
print "access_key = '%s'" % access_key
print "access_secret = '%s'" % access_secret
