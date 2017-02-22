#!/usr/bin/python

#-----------------------------------------------------------------------
# twitter-list-lists
#  - lists the lists owned by each of a list of users
#-----------------------------------------------------------------------

from twitter import *

#-----------------------------------------------------------------------
# the list of users that we want to examine
#-----------------------------------------------------------------------
users = [ "ideoforms", "hrtbps", "mocost" ]

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
# for each of our users in turn...
#-----------------------------------------------------------------------
import pprint
for user in users:
	print "@%s" % (user)

	#-----------------------------------------------------------------------
	# ...retrieve all of the lists they own.
	# twitter API docs: https://dev.twitter.com/rest/reference/get/lists/list
	#-----------------------------------------------------------------------
	result = twitter.lists.list(screen_name = user)
	for list in result:
		print " - %s (%d members)" % (list["name"], list["member_count"])
