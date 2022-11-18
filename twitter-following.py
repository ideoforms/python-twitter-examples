#!/usr/bin/env python3

#-----------------------------------------------------------------------
# twitter-following
#  - lists all of the accounts that a given user is following
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
# this is the user whose friends we will list
#-----------------------------------------------------------------------
username = "ideoforms"

#-----------------------------------------------------------------------
# perform a basic search 
# twitter API docs: https://dev.twitter.com/rest/reference/get/friends/ids
#-----------------------------------------------------------------------
query = twitter.friends.ids(screen_name=username)

#-----------------------------------------------------------------------
# tell the user how many friends we've found.
# note that the twitter API will NOT immediately give us any more 
# information about friends except their numeric IDs...
#-----------------------------------------------------------------------
print("Following %d accounts\n" % (len(query["ids"])))

#-----------------------------------------------------------------------
# now we loop through them to pull out more info, in blocks of 100.
#-----------------------------------------------------------------------
for n in range(0, len(query["ids"]), 100):
    ids = query["ids"][n:n + 100]

    #-----------------------------------------------------------------------
    # create a comma-separated string from the ID list
    #-----------------------------------------------------------------------
    ids_string = ",".join(str(id) for id in ids)

    #-----------------------------------------------------------------------
    # create a subquery, looking up information about these users
    # twitter API docs: https://dev.twitter.com/rest/reference/get/users/lookup
    #-----------------------------------------------------------------------
    subquery = twitter.users.lookup(user_id=ids_string)

    for user in subquery:
        #-----------------------------------------------------------------------
        # print out user information
        #-----------------------------------------------------------------------
        print(" - %s (%s)" % (user["screen_name"], user["location"]))
