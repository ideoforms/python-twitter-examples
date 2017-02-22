#!/usr/bin/python

#-----------------------------------------------------------------------
# twitter-search-geo
#  - performs a search for tweets close to New Cross, London,
#    and outputs them to a CSV file.
#-----------------------------------------------------------------------

from twitter import *

import sys
import csv

latitude = 51.474144	# geographical centre of search
longitude = -0.035401	# geographical centre of search
max_range = 1 			# search range in kilometres
num_results = 50		# minimum results to obtain
outfile = "output.csv"

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
# open a file to write (mode "w"), and create a CSV writer object
#-----------------------------------------------------------------------
csvfile = file(outfile, "w")
csvwriter = csv.writer(csvfile)

#-----------------------------------------------------------------------
# add headings to our CSV file
#-----------------------------------------------------------------------
row = [ "user", "text", "latitude", "longitude" ]
csvwriter.writerow(row)

#-----------------------------------------------------------------------
# the twitter API only allows us to query up to 100 tweets at a time.
# to search for more, we will break our search up into 10 "pages", each
# of which will include 100 matching tweets.
#-----------------------------------------------------------------------
result_count = 0
last_id = None
while result_count <  num_results:
	#-----------------------------------------------------------------------
	# perform a search based on latitude and longitude
	# twitter API docs: https://dev.twitter.com/rest/reference/get/search/tweets
	#-----------------------------------------------------------------------
	query = twitter.search.tweets(q = "", geocode = "%f,%f,%dkm" % (latitude, longitude, max_range), count = 100, max_id = last_id)

	for result in query["statuses"]:
		#-----------------------------------------------------------------------
		# only process a result if it has a geolocation
		#-----------------------------------------------------------------------
		if result["geo"]:
			user = result["user"]["screen_name"]
			text = result["text"]
			text = text.encode('ascii', 'replace')
			latitude = result["geo"]["coordinates"][0]
			longitude = result["geo"]["coordinates"][1]

			#-----------------------------------------------------------------------
			# now write this row to our CSV file
			#-----------------------------------------------------------------------
			row = [ user, text, latitude, longitude ]
			csvwriter.writerow(row)
			result_count += 1
		last_id = result["id"]

	#-----------------------------------------------------------------------
	# let the user know where we're up to
	#-----------------------------------------------------------------------
	print "got %d results" % result_count

#-----------------------------------------------------------------------
# we're all finished, clean up and go home.
#-----------------------------------------------------------------------
csvfile.close()

print "written to %s" % outfile

