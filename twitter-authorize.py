#!/usr/bin/env python

#-----------------------------------------------------------------------
# twitter-authorize:
#  - step through the process of creating and authorization a
#    Twitter application.
#-----------------------------------------------------------------------

import twitter
import time

print("1. Create a new Twitter application at: https://apps.twitter.com\n")

print("2. When you have created the application, enter:")
print("   your application name:", end=' ')
app_name = input()

print("   your consumer key:", end=' ')
consumer_key = input()

print("   your consumer secret:", end=' ')
consumer_secret = input()

print()
print("3. Now, we need to authorize this application.")
print("   You'll be forwarded to a web browser in two seconds.\n")

time.sleep(2)

access_key, access_secret = twitter.oauth_dance(app_name, consumer_key, consumer_secret)

print()
print("4. Now, replace the credentials in config.py with the below:\n")

print("consumer_key = '%s'" % consumer_key)
print("consumer_secret = '%s'" % consumer_secret)
print("access_key = '%s'" % access_key)
print("access_secret = '%s'" % access_secret)
