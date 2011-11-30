#!/usr/bin/python

#-----------------------------------------------------------------------
# twitter-list-lists
#  - lists the lists owned by each of a list of users
#-----------------------------------------------------------------------

# the list of users that we want to examine
users = [ "ideoforms", "GoldsmithsLEU", "mocost" ]

from twitter import *

# create twitter API object
twitter = Twitter()

# for each of our users in turn...
for user in users:
	print "@%s" % (user)

	# ...retrieve all of the lists they own.
	# twitter API docs: https://dev.twitter.com/docs/api/1/get/lists
	result = twitter.lists(screen_name = user)

	# now, print each of these lists, and its member count.
	for list in result["lists"]:
		print " - %s (%d members)" % (list["name"], list["member_count"])
