import tweepy

import fasttext

import datetime

import nltk

import numpy as np

import pickle

from application import app
# import matplotlib.pyplot as plt
def moving_average(a, n=3):
	"""Calculates the moving (running) average of a numpy vector.
	This function is useful in case we want to "smooth" time series.
	Args:
		a (numpy.array): Input numpy vector.
		n (int, optional): Width of the moving average window. Defaults to 3.
	Returns:
		numpy.array: Moving average of the input vector with width "n".
	"""	
	ret = np.cumsum(a, dtype=float)
	ret[n:] = ret[n:] - ret[:-n]
	return ret[n - 1:]/n

class SentimentAnalyzer():
	def __init__(self, tokenizerFilename='application/sentiment/tokenizer.pickle', modelFilename='application/sentiment/model_sentiment_2.ftz'):
		"""Constructor of the SentimentAnalyzer class.
		Requires a trained fasttext supervised model and a numpy tokenizer.
		Args:
			tokenizerFilename (str): Path for loading tokenizer.
			modelFilename (str): Path for loading model.
		"""
		# Load NLTK tokenizer model.
		with open(tokenizerFilename, 'rb') as handle:
			self.tokenizer = pickle.load(handle)

		# Load fasttext classifier model.
		self.model = fasttext.load_model(modelFilename)

		# Connecting to the Twitter API
		self.auth = tweepy.AppAuthHandler(app.config.get('TWITTER_OAUTH_CLIENT_KEY'), \
			app.config.get('TWITTER_OAUTH_CLIENT_SECRET'))
		self.api = tweepy.API(self.auth)
	
	def calculateSentimentCoeff(self,n, twitterHandle='@adityaoberai1', api=None):
		"""Calculates the sentiment coefficient given a Twitter handle
		and a number of tweets (n) using the days as the time unit.
		Args:
			twitterHandle (str): Handle of the person to analyze.
			n (int): Number of tweets to take into consideration.
			api (tweepy.API): Instance of tweepy's API to connect to Twitter.
		Returns:
			float: Average of the sentiment of the last activity days.
		"""
		# Check if an API object is provided
		if not api:
			api = self.api

		# Initialize auxiliar variables.
		ts = np.array([], dtype="float")
		dates = {}

		# Retrieve tweets and store them by date
		for tweet in tweepy.Cursor(api.user_timeline, screen_name=twitterHandle, count=n).items(n):
			dates[tweet.created_at.date()] = dates.get(tweet.created_at.date(), "") + tweet.text.replace("\n", " ")

		# For every date, split the tweets by sentence and accumulate
		# and average their score. We end up with a k length vector, 
		# being k the number of days that the retieved tweets span.
		for k in sorted(dates.keys()):
			aux = 0
			n = 0
			for sent in self.tokenizer.tokenize(dates[k]):
				
				# Here we would need to check if the sentence is
				# in English. And in the case that it is not,
				# we should translate it to English.

				pred = self.model.predict(sent)
				aux += (1 if pred[0][0] == '__label__4' else -1)*pred[1][0]
				n += 1
			ts = np.append(ts, [aux/n], axis=None)
		
		plt.plot(list(sorted(dates.keys())),ts)
		# Return the average of the coefficients of the retrieved dates.
		return np.average(ts)

		# This is in case we want to plot the data for debug purposes.
	
