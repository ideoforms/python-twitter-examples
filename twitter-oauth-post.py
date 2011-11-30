#!/usr/bin/python

#-----------------------------------------------------------------------
# twitter-oauth-post
#  - posts a status message to your timeline
#-----------------------------------------------------------------------

from twitter import *

# what should our new status be?
new_status = "testing testing"

# these tokens are necessary for user authentication
# (created within the twitter developer API pages)
consumer_key = "XXXxXxXxXXXXxxXxXXxXX"
consumer_secret = "xXXXXxxXxXXXXxXxXXXxxXxxXxxxxXXXXXxxxXxxxX"
access_key = "XXXXXXXXX-XXXXxXxxXXXXxXXXXxXXXXxXXxxxXXXXXXXXxXXX"
access_secret = "XXXXxXXXXxXxXxxxxXxXXXxXxxxxXxXXxXXXxX"

# create twitter API object
auth = OAuth(access_key, access_secret, consumer_key, consumer_secret)
twitter = Twitter(auth = auth)

# post a new status
# twitter API docs: https://dev.twitter.com/docs/api/1/post/statuses/update
results = twitter.statuses.update(status = new_status)
print "updated status: %s" % new_status
