import tweepy
import json
import os
import sp_test as sp

# Variables that contains the user credentials to access Twitter API 
ACCESS_TOKEN = ''
ACCESS_SECRET = ''
CONSUMER_KEY = ''
CONSUMER_SECRET = ''


# Setup tweepy to authenticate with Twitter credentials:
def authTw():
	sp.speak("authenticating your twitter account")
	auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
	auth.set_access_token(ACCESS_TOKEN, ACCESS_SECRET)
	# Create the api to connect to twitter with your creadentials
	api = tweepy.API(auth, wait_on_rate_limit=False, wait_on_rate_limit_notify=False, compression=False)
	return api

def showTw(api_obj):
	sp.speak("Showing Your Tweets")
	c=''
	import re 

	for status in tweepy.Cursor(api_obj.home_timeline,tweet_mode='extended').items(2):
		b=status._json['user']['name']+' Tweeted '+ status._json['full_text']
		url = re.findall('https://t.co/[a-zA-Z0-9]*',b)
		for item in url:
			b=b.replace(item,'')
		c+=b
		c+='.'
	sp.speak(c)	


def likeTw(api_obj,inputN):
	ids=[]
	names=[]
	for status in tweepy.Cursor(api_obj.home_timeline,tweet_mode='extended').items(2):
		ids.append(str(status._json['id']))
		names.append(status._json['user']['name'].lower())
	i=0
	for item in names:
		if(inputN==item):
			api_obj.create_favorite(ids[i])
		i=i+1

def followTw(api_obj,inputN):
	x=api_obj.search_users(inputN)
	uid=x[0]._json['id']
	api_obj.create_friendship(uid)

def unfollowTw(api_obj,inputN):
	uids = []
	name = []
	for page in tweepy.Cursor(api_obj.followers).items():
		b=page._json
		uids.append(b['id'])
		name.append(b['name'].lower())

	j=0
	for item in name:
		if(item==inputN):
			api_obj.destroy_friendship(uids[j])
		j=j+1

