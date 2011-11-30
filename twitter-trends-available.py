#!/usr/bin/python

#-----------------------------------------------------------------------
# twitter-trends-available
#  - prints applicable location IDs (WOE IDs) for localised trend
#    tracking
#-----------------------------------------------------------------------

from twitter import *

# create twitter API object
twitter = Twitter()

# retrieve applicable trend locations.
# twitter API docs: https://dev.twitter.com/docs/api/1/get/trends/available
results = twitter.trends.available()

for location in results:
	name = location["name"].encode('ascii', 'replace')
	print "(%d) %s" % (location["woeid"], name)
