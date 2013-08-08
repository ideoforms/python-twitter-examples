#!/usr/bin/python

#-----------------------------------------------------------------------
# twitter-search
#  - performs a basic keyword search for tweets containing the keywords
#    "lazy" and "dog"
#-----------------------------------------------------------------------

from twitter import *
from datetime import datetime

created_at_format = "%a, %d %b %Y %H:%M:%S +0000"

# create twitter API object
twitter = Twitter()

# perform a basic search 
# twitter API docs: https://dev.twitter.com/docs/api/1/get/search
terms = "pink elephants"
query = twitter.search(q = terms)
num_results = len(query["results"])
                  
# make a list of the differences between the time-stamps of each tweet
t_diffs = []
for i in range(0, num_results, 2):
    if i < num_results - 1:
        this_result = query["results"][i]
        next_result = query["results"][i + 1]

        this_result_timestamp = datetime.strptime(this_result["created_at"], created_at_format)
        next_result_timestamp = datetime.strptime(next_result["created_at"], created_at_format)

        diff = this_result_timestamp - next_result_timestamp
        
        t_diffs.append(diff.total_seconds())

# print the average of the differences
print "Average tweeting rate for '%s' between %s and %s: %.3fs" %\
      (terms,
       query["results"][num_results - 1]["created_at"],
       query["results"][0]["created_at"],
       float(sum(t_diffs)) / float(len(t_diffs)))
