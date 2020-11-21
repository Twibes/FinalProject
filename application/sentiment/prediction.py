import tweepy

import fasttext

import config

import pandas

import sklearn
from sklearn.model_selection import train_test_split

from matplotlib import pyplot as plt

import datetime

import nltk

import numpy as np

import pickle

def moving_average(a, n=3) :
    ret = np.cumsum(a, dtype=float)
    ret[n:] = ret[n:] - ret[:-n]
    return ret[n - 1:] / n

class SentimentAnalyzer():
	def __init__(self, tokenizerFilename, modelFilename):
		"""Constructor of the SentimentAnalyzer class.
		Requires a trained fasttext supervised model and a numpy tokenizer.

		Args:
			tokenizerFilename (str): Path for loading tokenizer.
			modelFilename (str): Path for loading model.
		"""		
		with open(tokenizerFilename, 'rb') as handle:
			self.tokenizer = pickle.load(handle)
		self.model = fasttext.load_model(modelFilename)
	
	def calculateSentimentCoeff(self, twitterHandle, n, api):
		"""Calculates the sentiment coefficient given a Twitter handle
		and a number of tweets (n) using the days as the time unit.

		Args:
			twitterHandle (str): Handle of the person to analyze.
			n (int): Number of tweets to take into consideration.
			api (tweepy.API): Instance of tweepy's API to connect to Twitter.

		Returns:
			float: Average of the sentiment of the last activity days.
		"""		
		ts = np.array([], dtype="float")
		dates = {}

		for tweet in tweepy.Cursor(api.user_timeline, screen_name=twitterHandle, count=n).items(n):
			dates[tweet.created_at.date()] = dates.get(tweet.created_at.date(), "") + tweet.text.replace("\n", " ")

		for k in sorted(dates.keys()):
			aux = 0
			n = 0
			for sent in self.tokenizer.tokenize(dates[k]):
				pred = self.model.predict(sent)
				aux += (1 if pred[0][0] == '__label__4' else -1)*pred[1][0]
				n += 1
			ts = np.append(ts, [aux/n], axis=None)
		
		return np.average(ts)
		#plt.plot(list(sorted(dates.keys())),ts)
	

