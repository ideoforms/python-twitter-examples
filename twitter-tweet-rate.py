#!/usr/bin/python

#-----------------------------------------------------------------------
# twitter-tweet-rate
#-----------------------------------------------------------------------

from twitter import *
from datetime import datetime

created_at_format = '%a %b %d %H:%M:%S +0000 %Y'

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
# twitter API docs: https://dev.twitter.com/rest/reference/get/search/tweets
#-----------------------------------------------------------------------
terms = "pink elephants"
query = twitter.search.tweets(q = terms)
results = query["statuses"]
                  
#-----------------------------------------------------------------------
# take the timestamp of the first and last tweets in these results,
# and calculate the average time between tweets.
#-----------------------------------------------------------------------
first_timestamp = datetime.strptime(results[0]["created_at"], created_at_format)
last_timestamp = datetime.strptime(results[-1]["created_at"], created_at_format)
total_dt = (first_timestamp - last_timestamp).total_seconds()
mean_dt = total_dt / len(results)

#-----------------------------------------------------------------------
# print the average of the differences
#-----------------------------------------------------------------------
print "Average tweeting rate for '%s' between %s and %s: %.3fs" % (terms, results[-1]["created_at"], results[ 0]["created_at"], mean_dt)

