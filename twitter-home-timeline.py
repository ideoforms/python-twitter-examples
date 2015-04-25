#!/usr/bin/python

#-----------------------------------------------------------------------
# twitter-oauth-timeline:
#  - uses the Twitter API and OAuth to log in as your username,
#    and lists the latest 50 tweets from your feed.
#-----------------------------------------------------------------------

from twitter import *

# these tokens are necessary for user authentication
# (created within the twitter developer API pages)
consumer_key = "XxXxXxxXXXxxxxXXXxXX"
consumer_secret = "xXXXXXXXXxxxxXxXXxxXxxXXxXxXxxxxXxXXxxxXXx"
access_key = "XXXXXXXX-xxXXxXXxxXxxxXxXXxXxXxXxxxXxxxxXxXXxXxxXX"
access_secret = "XxXXXXXXXXxxxXXXxXXxXxXxxXXXXXxXxxXXXXx"

# create twitter API object
auth = OAuth(access_key, access_secret, consumer_key, consumer_secret)
twitter = Twitter(auth = auth)

# request my home timeline
# twitter API docs: https://dev.twitter.com/docs/api/1/get/statuses/home_timeline
statuses = twitter.statuses.home_timeline(count = 50)

# loop through each of my statuses, and print its content
for status in statuses:
	print "(%s) @%s %s" % (status["created_at"], status["user"]["screen_name"], status["text"])
