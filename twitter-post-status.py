#!/usr/bin/python

#-----------------------------------------------------------------------
# twitter-post-status
#  - posts a status message to your timeline
#-----------------------------------------------------------------------

from twitter import *

#-----------------------------------------------------------------------
# what should our new status be?
#-----------------------------------------------------------------------
new_status = "testing testing"

#-----------------------------------------------------------------------
# load our API credentials 
#-----------------------------------------------------------------------
config = {}
execfile("config.py", config)

#-----------------------------------------------------------------------
# create twitter API object
#-----------------------------------------------------------------------
twitter = Twitter(
	auth = OAuth(config["access_key"], config["access_secret"], config["consumer_key"], config["consumer_secret"]))

#-----------------------------------------------------------------------
# post a new status
# twitter API docs: https://dev.twitter.com/rest/reference/post/statuses/update
#-----------------------------------------------------------------------
results = twitter.statuses.update(status = new_status)
print "updated status: %s" % new_status
