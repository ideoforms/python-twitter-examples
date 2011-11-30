#!/usr/bin/python

#-----------------------------------------------------------------------
# twitter-trends
#  - lists the current global trending topics
#-----------------------------------------------------------------------

from twitter import *

# create twitter API object
twitter = Twitter()

# retrieve global trends.
# other localised trends can be specified by looking up WOE IDs:
#   http://developer.yahoo.com/geo/geoplanet/
# twitter API docs: https://dev.twitter.com/docs/api/1/get/trends/%3Awoeid
results = twitter.trends._woeid(_woeid = 1)

print "GLOBAL TRENDS"

for location in results:
	for trend in location["trends"]:
		print " - %s" % trend["name"]
