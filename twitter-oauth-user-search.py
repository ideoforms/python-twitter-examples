#!/usr/bin/python

#-----------------------------------------------------------------------
# twitter-oauth-user-search
#  - performs a search for users matching a certain query
#-----------------------------------------------------------------------

from twitter import *

# these tokens are necessary for user authentication
consumer_key = "XxXxXxxXXXxxxxXXXxXX"
consumer_secret = "xXXXXXXXXxxxxXxXXxxXxxXXxXxXxxxxXxXXxxxXXx"
access_key = "XXXXXXXX-xxXXxXXxxXxxxXxXXxXxXxXxxxXxxxxXxXXxXxxXX"
access_secret = "XxXXXXXXXXxxxXXXxXXxXxXxxXXXXXxXxxXXXXx"

# create twitter API object
auth = OAuth(access_key, access_secret, consumer_key, consumer_secret)
twitter = Twitter(auth = auth)

# perform a user search 
# twitter API docs: https://dev.twitter.com/docs/api/1/get/users/search
results = twitter.users.search(q = '"New Cross"')

# loop through each of the users, and print their details
for user in results:
	print "@%s (%s): %s" % (user["screen_name"], user["name"], user["location"])
