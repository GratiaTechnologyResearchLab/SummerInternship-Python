import tweepy
import json

# Consumer keys and access tokens, used for OAuth
API_KEY = 'oNlx4TCw5YcykzZCNaQei0w8x'
API_SECRET='PDzXBJiS3DwMc2YCHl6remkN0z2mAERxPJP1ArLYBovjXDYZzO'
ACCESS_TOKEN='958211334486704128-uT4IU8dB4a408ewYLUXvppERD4KCTyH'
ACCESS_TOKEN_SECRET='g3MKPwwO1ZstBOMgfjmVIym9VaEhtL1LP2Yf82lQWEne9'


# OAuth process, using the keys and tokens
auth=tweepy.OAuthHandler(API_KEY, API_SECRET)
auth.set_access_token(ACCESS_TOKEN, ACCESS_TOKEN_SECRET)

# Creation of the actual interface, using authentication
api = tweepy.API(auth)

#user= api.get_user(screen_name='Priyom16')
#api.get_user(screen_name='Priyom16')
api.update_profile_image('ok.jpg')

#printing the details of the user

#getting user data(here profile picture)
