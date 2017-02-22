#!/usr/bin/python

#-----------------------------------------------------------------------
# twitter-retweets
#  - print who has retweeted tweets from a given user's timeline
#-----------------------------------------------------------------------

from twitter import *

user = "ideoforms"

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
# perform a basic search 
# twitter API docs: https://dev.twitter.com/rest/reference/get/statuses/user_timeline
#-----------------------------------------------------------------------
results = twitter.statuses.user_timeline(screen_name = user)

#-----------------------------------------------------------------------
# loop through each of my statuses, and print its content
#-----------------------------------------------------------------------
for status in results:
	print "@%s %s" % (user, status["text"])

	#-----------------------------------------------------------------------
	# do a new query: who has RT'd this tweet?
	#-----------------------------------------------------------------------
	retweets = twitter.statuses.retweets._id(_id = status["id"])
	for retweet in retweets:
		print " - retweeted by %s" % (retweet["user"]["screen_name"])
