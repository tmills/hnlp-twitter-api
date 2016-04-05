#!/usr/bin/env python
# 
# This example is taken from here:
# http://tweepy.readthedocs.org/en/v3.5.0/getting_started.html
# and added the utility to read credentials into a map.

import tweepy

from credentials import get_credentials

creds = get_credentials()
auth = tweepy.OAuthHandler(creds.get('consumer_key'), creds.get('consumer_secret'))
auth.set_access_token(creds.get('access_token'), creds.get('access_token_secret'))

api = tweepy.API(auth)

public_tweets = api.home_timeline()
for tweet in public_tweets:
    print tweet.text