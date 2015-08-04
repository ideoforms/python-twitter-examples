#!/usr/bin/python

#-----------------------------------------------------------------------
# twitter-user-timeline
#  - displays a user's current timeline.
#-----------------------------------------------------------------------

from twitter import *

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
# this is the user we're going to query.
#-----------------------------------------------------------------------
user = "ideoforms"

#-----------------------------------------------------------------------
# query the user timeline.
# twitter API docs:
# https://dev.twitter.com/rest/reference/get/statuses/user_timeline
#-----------------------------------------------------------------------
results = twitter.statuses.user_timeline(screen_name = user)

#-----------------------------------------------------------------------
# loop through each status item, and print its content.
#-----------------------------------------------------------------------
for status in results:
	print "(%s) %s" % (status["created_at"], status["text"].encode("ascii", "ignore"))
