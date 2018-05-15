import tweepy
import tempfile
import urllib
from time import sleep
import os

url = 'http://wwc.instacam.com/instacamimg/KDCA/KDCA_l.jpg'

# 
API_KEY='<>'
API_SECRET='<>'
ACCESS_TOKEN='<>'
ACCESS_TOKEN_SECRET='<>'
# The consumer keys can be found on your application's Details
# page located at https://dev.twitter.com/apps (under "OAuth settings")
auth = tweepy.OAuthHandler(API_KEY, API_SECRET)

# The access tokens can be found on your applications's Details
# page located at https://dev.twitter.com/apps (located 
# under "Your access token")
auth.set_access_token(ACCESS_TOKEN, ACCESS_TOKEN_SECRET)

api = tweepy.API(auth)

try:
    (filename, headers) = urllib.urlretrieve(url)
    for attempt in range(10):
        try:
            # The update profile API randomly throws error 131 like half the time
            api.update_profile_background_image(filename, use=1, tile=0)
        except tweepy.error.TweepError as err:
            if err[0][0]['code'] == 131 or err[0][0]['code'] == 130:
                print "attempt %d, resulted in %s" % (attempt, err)
                sleep(1)
                continue
            else:
                raise
        break
finally:
    os.remove(filename)