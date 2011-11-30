#!/usr/bin/python

#-----------------------------------------------------------------------
# twitter-stream-responder
#  - will respond to any tweet that mentions me.
#-----------------------------------------------------------------------

from twitter import *
import time

# this is the tag we're matching
username = "puncstats"

# sleep for this number of seconds between tweets, to ensure we
# don't flood
sleep_time = 1

# these tokens are necessary for user authentication
# (created within the twitter developer API pages)
consumer_key = "XXXxXxXxXXXXxxXxXXxXX"
consumer_secret = "xXXXXxxXxXXXXxXxXXXxxXxxXxxxxXXXXXxxxXxxxX"
access_key = "XXXXXXXXX-XXXXxXxxXXXXxXXXXxXXXXxXXxxxXXXXXXXXxXXX"
access_secret = "XXXXxXXXXxXxXxxxxXxXXXxXxxxxXxXXxXXXxX"

# create twitter API object
auth = OAuth(access_key, access_secret, consumer_key, consumer_secret)
twitter = Twitter(auth = auth)
stream = TwitterStream(domain = "userstream.twitter.com", auth = auth, api_version = 2, secure = True)

# iterate over tweets matching this filter text
# IMPORTANT! this is not quite the same as a standard twitter search
#  - see https://dev.twitter.com/docs/streaming-api
tweet_iter = stream.user()

for tweet in tweet_iter:
	# check whether this is a valid tweet
	if tweet.get('text'):

		# are we mentioned within this tweet?
		mentions = tweet["entities"]["user_mentions"]
		mentioned_users = [ mention["screen_name"] for mention in mentions ]

		if username in mentioned_users:
			print "thanking @%s for the mention" % tweet["user"]["screen_name"]

			# update our status with a thank you message directed at the source.
			# use try/except to catch potential failures.
			status = "@%s thanks for the mention" % tweet["user"]["screen_name"]
			try:
				twitter.statuses.update(status = status)
			except Exception, e:
				print " - failed (maybe a duplicate?)"
		time.sleep(sleep_time)

