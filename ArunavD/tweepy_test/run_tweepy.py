

import tweepy
import json


# Consumer keys and access tokens, used for OAuth
API_KEY = '< >'
API_SECRET='< >'
ACCESS_TOKEN='< >'
ACCESS_TOKEN_SECRET='< >'


# OAuth process, using the keys and tokens
auth = tweepy.OAuthHandler(API_KEY, API_SECRET)
auth.set_access_token(ACCESS_TOKEN, ACCESS_TOKEN_SECRET)

# Creation of the actual interface, using authentication
api = tweepy.API(auth)
'''
results = api.update_(screen_name='ArunavDas123')
print json.dumps(results._json)
'''
api.update_profile_image('unnamed.jpg')
