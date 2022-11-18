#!/usr/bin/env python3

#-----------------------------------------------------------------------
# twitter-user-timeline
#  - displays a user's current timeline.
#-----------------------------------------------------------------------
from twitter import *
import sys

#-----------------------------------------------------------------------
# load our API credentials
#-----------------------------------------------------------------------
sys.path.append(".")
import config

#-----------------------------------------------------------------------
# create twitter API object
#-----------------------------------------------------------------------
twitter = Twitter(auth=OAuth(config.access_key,
                             config.access_secret,
                             config.consumer_key,
                             config.consumer_secret))

#-----------------------------------------------------------------------
# this is the user we're going to query.
#-----------------------------------------------------------------------
user = "ideoforms"

#-----------------------------------------------------------------------
# query the user timeline.
# twitter API docs:
# https://dev.twitter.com/rest/reference/get/statuses/user_timeline
#-----------------------------------------------------------------------
results = twitter.statuses.user_timeline(screen_name=user, count=100)
while True:
    #-----------------------------------------------------------------------
    # loop through each status item, and print its content.
    #-----------------------------------------------------------------------
    for status in results:
        print("(%s) %s" % (status["created_at"], status["text"]))

    results = twitter.statuses.user_timeline(screen_name=user,
                                             count=100,
                                             max_id=results[-1]["id"] - 1)

    if len(results) == 0:
        break