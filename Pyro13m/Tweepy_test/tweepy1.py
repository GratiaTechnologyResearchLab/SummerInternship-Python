#UPDATING TWITTER USER  DISPLAY PICTURE 


import tweepy

# Consumer keys and access tokens, used for OAuth

API_KEY = '<API_KEY>'
API_SECRET ='<API_SECRET_KEY>'
ACCESS_TOKEN = <'ACCESS_TOKEN>'
ACCESS_TOKEN_SECRET = <'ACCESS_TOKEN_SECRET'>


# OAuth process, using the keys and tokens

auth=tweepy.OAuthHandler(API_KEY, API_SECRET)
auth.set_access_token(ACCESS_TOKEN, ACCESS_TOKEN_SECRET)

# Creation of the actual interface, using authentication

api = tweepy.API(auth)

#UPDATING THE PROFILE IMAGE OF THE TWITTER ACCOUNT

api.update_profile_image('<image_name.typ>')

