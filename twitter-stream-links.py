#!/usr/bin/python

#-----------------------------------------------------------------------
# twitter-stream:
#  - ultra-real-time stream of twitter's public timeline
#    prints live results containing a URL link and the #OWS tag
#-----------------------------------------------------------------------

from twitter import *

# these tokens are necessary for user authentication
consumer_key = "XxXxXxxXXXxxxxXXXxXX"
consumer_secret = "xXXXXXXXXxxxxXxXXxxXxxXXxXxXxxxxXxXXxxxXXx"
access_key = "XXXXXXXX-xxXXxXXxxXxxxXxXXxXxXxXxxxXxxxxXxXXxXxxXX"
access_secret = "XxXXXXXXXXxxxXXXxXXxXxXxxXXXXXxXxxXXXXx"

# create twitter API object
auth = OAuth(access_key, access_secret, consumer_key, consumer_secret)
stream = TwitterStream(auth = auth, secure = True)

# iterate over tweets matching this filter text
# IMPORTANT! this is not quite the same as a standard twitter search
#  - see https://dev.twitter.com/docs/streaming-api
tweet_iter = stream.statuses.filter(track = "social")

for tweet in tweet_iter:
	# check whether this is a valid tweet
	if tweet.get('text'):
		# yes it is! print out the contents, and any URLs found inside
		print "(%s) @%s %s" % (tweet["created_at"], tweet["user"]["screen_name"], tweet["text"])
		for url in tweet["entities"]["urls"]:
			print " - found URL: %s" % url["expanded_url"]
