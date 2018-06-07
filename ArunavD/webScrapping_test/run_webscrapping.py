
# coding: utf-8

# In[132]:


import requests
from bs4 import BeautifulSoup
import urllib
import re
import ConfigParser
import datetime
import sys

import urllib3
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

# Read username and password from config file
settings_file = "/home/hridoy/Work/youlikehits-scraper/config.txt"
config = ConfigParser.ConfigParser()
config.readfp(open(settings_file))

# Fill in your details here to be posted to the login form.
payload = {
    'username': config.get('Credentials', 'username'),
    'pass': config.get('Credentials', 'password')
}
content = None

import csv 
import sys
import time

f = open('datas/allFiles.csv', 'rb')
reader = csv.reader(f)
existingTweets = []
for row in reader:
    existingTweets.append([int(row[0]),int(row[1])])
f.close()

twtIDs = [x[0] for x in existingTweets]
# print twtIDs

print "****** YOULIKEHITS PARSER WORKING ******"
# Use 'with' to ensure the session context is closed after use.
fw =  open('datas/allFiles_' + datetime.datetime.now().strftime('%Y%m%d%H%M%S') + '.csv','a+')
with requests.Session() as s:
    # login to youlikehits using payload parameters
    p = s.post('https://youlikehits.com/login.php', data=payload, verify=False)
    count = 0
    while count < 999:
        retweetPageContent = s.get("https://youlikehits.com/retweets.php?show=" + str(count)).content

        # Find all tweet points    
        allTweetPoints = re.findall('<b>Points.*<br>',retweetPageContent)
        allTweetPoints = [x[15:-4] for x in allTweetPoints]
        
        # Find all iframes in the web page
        soup = BeautifulSoup(retweetPageContent, 'html.parser')
        tag = soup.find_all('iframe')


        # Get URLs of retweets
        rtURLs = []
        for items in tag:
            soup = BeautifulSoup(str(items), 'html.parser')
            tag1 = soup.find_all('iframe')[0]
            rtURLs.append(tag1['src'])

        # Get BlackMarket Tweet-IDs
        import re

        for i, urls in enumerate(rtURLs):
            iframecontent = s.get("https://youlikehits.com/" + urls).content
            soup = BeautifulSoup(iframecontent, 'html.parser')

            tweetId = str(re.search("(?P<url>https?://[^\s]+)", iframecontent).group("url").split(",")[0][43:-1])
            

            # for valList in existingTweets:

            if int(tweetId) not in twtIDs:
                existingTweets.append([int(tweetId),int(allTweetPoints[i])])
            # Regex for twitter id
            # fw.write(str(re.search("(?P<url>https?://[^\s]+)", iframecontent).group("url").split(",")[0][43:-1]) + "," + str(allTweetPoints[i]) + "\n")
        print len(existingTweets)    
        count += 9

for item in existingTweets:
    fw.write(str(item[0]) + ',' + str(item[1]) + '\n')   


