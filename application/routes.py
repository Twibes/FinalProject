import os
from flask import render_template, redirect, flash, url_for, request
from application import app
from .UserDAC import db
from .model.models import User
from .forms import LoginForm, RegistrationForm
from werkzeug.urls import url_parse
from flask_dance.contrib.twitter import twitter
import json
from .sentiment.prediction import SentimentAnalyzer

@app.route('/')
def redir():
    return redirect('/index')

@app.route("/twitterlogin")
def login():
        return redirect(url_for("twitter.login"))
@app.route("/logged")
def twitter_login():
    if not twitter.authorized:
        return redirect(url_for("twitter.login"))
    resp = twitter.get("account/settings.json")
    if resp.ok:
        return render_template('index.html', twitter=twitter, tweets=resp.json()['screen_name'], status='Out')
    return '<h1> Oops request failed </h1>'

@app.route("/index")
@app.route("/home")
def index():
    return render_template('index.html', twitter = twitter, Status='In')

# @app.route('/logout')
# def logout():
#     logout_user()
#     return redirect(url_for('index'))

@app.route('/userval')
def sentiment():
    #resp = twitter.get("account/settings.json")
    #if resp.ok:
    USERNAME = 'adityaoberai1'
    predict = SentimentAnalyzer()
    variable = predict.calculateSentimentCoeff('@'+USERNAME, 50)
    return render_template('xyz.html', variable=variable)

@app.route('/bot')
def bot():
    key=os.environ.get('bot_secret')
    return render_template('bot.html',secret = key) 
@app.route('/blog')
def blog():
    return render_template('blog.html')