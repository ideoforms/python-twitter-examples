#!/usr/bin/python

#-----------------------------------------------------------------------
# twitter-hoome-timeline:
#  - uses the Twitter API and OAuth to log in as your username,
#    and lists the latest 50 tweets from people you are following 
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
# request my home timeline
# twitter API docs: https://dev.twitter.com/rest/reference/get/statuses/home_timeline
#-----------------------------------------------------------------------
statuses = twitter.statuses.home_timeline(count = 50)
print statuses

#-----------------------------------------------------------------------
# loop through each of my statuses, and print its content
#-----------------------------------------------------------------------
for status in statuses:
	print "(%s) @%s %s" % (status["created_at"], status["user"]["screen_name"], status["text"])
