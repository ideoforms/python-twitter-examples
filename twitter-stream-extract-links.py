#!/usr/bin/python

#-----------------------------------------------------------------------
# twitter-stream:
#  - ultra-real-time stream of twitter's public timeline
#    prints live results containing a URL link and the #OWS tag
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
auth = OAuth(config["access_key"], config["access_secret"], config["consumer_key"], config["consumer_secret"])
stream = TwitterStream(auth = auth, secure = True)

#-----------------------------------------------------------------------
# iterate over tweets matching this filter text
# IMPORTANT! this is not quite the same as a standard twitter search
#  - see https://dev.twitter.com/streaming/overview
#-----------------------------------------------------------------------
tweet_iter = stream.statuses.filter(track = "social")

for tweet in tweet_iter:
	#-----------------------------------------------------------------------
	# print out the contents, and any URLs found inside
	#-----------------------------------------------------------------------
	print "(%s) @%s %s" % (tweet["created_at"], tweet["user"]["screen_name"], tweet["text"])
	for url in tweet["entities"]["urls"]:
		print " - found URL: %s" % url["expanded_url"]
