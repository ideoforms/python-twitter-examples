#!/usr/bin/python

#-----------------------------------------------------------------------
# twitter-search-geo
#  - performs a search for tweets close to New Cross, and outputs
#    them to a CSV file.
#-----------------------------------------------------------------------

from twitter import *

import sys
import csv

# create twitter API object
twitter = Twitter()

# open a file to write (mode "w"), and create a CSV writer object
csvfile = file("output.csv", "w")
csvwriter = csv.writer(csvfile)

# add headings to our CSV file
row = [ "user", "text", "latitude", "longitude" ]
csvwriter.writerow(row)

# the twitter API only allows us to query up to 100 tweets at a time.
# to search for more, we will break our search up into 10 "pages", each
# of which will include 100 matching tweets.
for pagenum in range(1, 11):

	# perform a search based on latitude and longitude
	# twitter API docs: https://dev.twitter.com/docs/api/1/get/search
	query = twitter.search(q = "", geocode = "51.474144,-0.035401,1km", rpp = 100, page = pagenum)

	for result in query["results"]:
		# only process a result if it has a geolocation
		if result["geo"]:
			user = result["from_user"]
			text = result["text"]
			text = text.encode('ascii', 'replace')
			latitude = result["geo"]["coordinates"][0]
			longitude = result["geo"]["coordinates"][1]

			# now write this row to our CSV file
			row = [ user, text, latitude, longitude ]
			csvwriter.writerow(row)

	# let the user know where we're up to
	print "done page: %d" % (pagenum)

# we're all finished, clean up and go home.
csvfile.close()
