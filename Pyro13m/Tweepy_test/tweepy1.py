import tweepy
import json

# Consumer keys and access tokens, used for OAuth
API_KEY = 'ylHs9oKHl1El44zspcoV0OyO9'
API_SECRET='IdWdPkgAHuBEeB3lrrdjb8pjXRRk4nZuYPN3eNRuIheAqwuTPb'
ACCESS_TOKEN='903936075118239744-wVXlrfrDpV5NRKoKdOjVLhpAVMJe4Cy'
ACCESS_TOKEN_SECRET='lhjRsJRlSKA3rew1LwWZcKa7NKVbclTlaTNmLO4YNhygq'


# OAuth process, using the keys and tokens
auth = tweepy.OAuthHandler(API_KEY, API_SECRET)
auth.set_access_token(ACCESS_TOKEN, ACCESS_TOKEN_SECRET)

# Creation of the actual interface, using authentication
api = tweepy.API(auth)

api.get_user('Priyom16')
api.update_profile_image('ok.jpg')

#printing the details of the user

#getting user data(here profile picture)



