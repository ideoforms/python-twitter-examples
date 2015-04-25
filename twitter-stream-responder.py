#!/usr/bin/python

#-----------------------------------------------------------------------
# twitter-stream-responder
#  - will respond to any tweet that mentions me.
#-----------------------------------------------------------------------

from twitter import *
import time

#-----------------------------------------------------------------------
# this is the username we're matching against.
#-----------------------------------------------------------------------
username = "nplus7"

#-----------------------------------------------------------------------
# sleep for this number of seconds between tweets, to ensure we
# don't flood
#-----------------------------------------------------------------------
sleep_time = 1

#-----------------------------------------------------------------------
# load our API credentials 
#-----------------------------------------------------------------------
config = {}
execfile("config.py", config)

#-----------------------------------------------------------------------
# create twitter API object
#-----------------------------------------------------------------------
auth = OAuth(config["access_key"], config["access_secret"], config["consumer_key"], config["consumer_secret"])
twitter = Twitter(auth = auth)
stream = TwitterStream(domain = "userstream.twitter.com", auth = auth, secure = True)

#-----------------------------------------------------------------------
# iterate over tweets matching this filter text
#-----------------------------------------------------------------------
tweet_iter = stream.user()

for tweet in tweet_iter:
	#-----------------------------------------------------------------------
	# check whether this is a valid tweet
	#-----------------------------------------------------------------------
	if "entities" not in tweet:
		continue

	#-----------------------------------------------------------------------
	# are we mentioned within this tweet?
	#-----------------------------------------------------------------------
	mentions = tweet["entities"]["user_mentions"]
	mentioned_users = [ mention["screen_name"] for mention in mentions ]

	if username in mentioned_users:
		print "thanking @%s for the mention" % tweet["user"]["screen_name"]

		#-----------------------------------------------------------------------
		# update our status with a thank you message directed at the source.
		# use try/except to catch potential failures.
		#-----------------------------------------------------------------------
		status = "@%s thanks for the mention" % tweet["user"]["screen_name"]
		try:
			twitter.statuses.update(status = status)
		except Exception, e:
			print " - failed (maybe a duplicate?): %s" % e

	time.sleep(sleep_time)

