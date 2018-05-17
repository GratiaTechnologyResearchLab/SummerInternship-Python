import requests
from bs4 import BeautifulSoup
import re
import configparser

# Read username and password from config file

configFile = "/home/priyom/webscrapping/config.txt"
config = configparser.ConfigParser()
config.readfp(open(configFile))

# Fill in your details here to be posted to the login form.

datas = {
    'username': config.get('Credentials', 'username'),
    'pass': config.get('Credentials', 'password')
}


print("****** YOULIKEHITS PARSER WORKING ******")


with requests.Session() as s:
    
	p = s.post('<URL>', data=datas, verify=False)

	retweetPageContent = s.get("<URL>").content

    # Find all iframes in the web page
	soup = BeautifulSoup(retweetPageContent, 'html.parser')
	tag = soup.find_all('iframe')


    # Get URLs of retweets
	URLs = []
	for items in tag:
		soup = BeautifulSoup(str(items), 'html.parser')
		tag1 = soup.find_all('iframe')[0]
		URLs.append(tag1['src'])

print(URLs)


