#!/usr/bin/python

#-----------------------------------------------------------------------
# twitter-friends
#  - lists all of a given user's friends (ie, followees)
#-----------------------------------------------------------------------

from twitter import *

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
# this is the user whose friends we will list
#-----------------------------------------------------------------------
username = "ideoforms"

#-----------------------------------------------------------------------
# perform a basic search 
# twitter API docs: https://dev.twitter.com/rest/reference/get/friends/ids
#-----------------------------------------------------------------------
query = twitter.friends.ids(screen_name = username)

#-----------------------------------------------------------------------
# tell the user how many friends we've found.
# note that the twitter API will NOT immediately give us any more 
# information about friends except their numeric IDs...
#-----------------------------------------------------------------------
print "found %d friends" % (len(query["ids"]))

#-----------------------------------------------------------------------
# now we loop through them to pull out more info, in blocks of 100.
#-----------------------------------------------------------------------
for n in range(0, len(query["ids"]), 100):
	ids = query["ids"][n:n+100]

	#-----------------------------------------------------------------------
	# create a subquery, looking up information about these users
	# twitter API docs: https://dev.twitter.com/rest/reference/get/users/lookup
	#-----------------------------------------------------------------------
	subquery = twitter.users.lookup(user_id = ids)

	for user in subquery:
		#-----------------------------------------------------------------------
		# now print out user info, starring any users that are Verified.
		#-----------------------------------------------------------------------
		print " [%s] %s - %s" % ("*" if user["verified"] else " ", user["screen_name"], user["location"])

