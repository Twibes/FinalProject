from flask import render_template, redirect, flash, url_for, request
from flask_login import current_user, login_user, logout_user
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

def twitter_login():
    if not twitter.authorized:
        return redirect(url_for("twitter.login"))
    resp = twitter.get("account/settings.json")
    if resp.ok:
        return render_template('index.html', twitter=twitter, tweets=resp.json()['screen_name'])
    return '<h1> Oops request failed </h1>'

@app.route("/index")
@app.route("/home")
def index():
    return render_template('index.html', twitter=twitter)

@app.route('/login', methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('index'))
    form = LoginForm()
    if form.validate_on_submit():
        print(form.username.data)
        user = User.query.filter_by(username=form.username.data).first()
        if user is None or not user.check_password(form.password.data):
            flash('Invalid username or password')
            return redirect(url_for('login'))
        login_user(user, remember=form.remember_me.data)
        next_page = request.args.get('next')
        if not next_page or url_parse(next_page).netloc != '':
            next_page = url_for('index')
        return redirect(next_page)
    return render_template('login.html', title='Sign In', form=form)


@app.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('index'))


@app.route('/register', methods=['GET', 'POST'])
def register():
    if current_user.is_authenticated:
        return redirect(url_for('index'))
    form = RegistrationForm()
    if form.validate_on_submit():
        user = User(username=form.username.data, email=form.email.data)
        user.set_password(form.password.data)
        db.session.add(user)
        db.session.commit()
        flash('Congratulations, you are now a registered user!')
        return redirect(url_for('login'))
    return render_template('register.html', title='Register', form=form)

@app.route('/userval')
def sentiment():
    resp = twitter.get("account/settings.json")
    if resp.ok:
        USERNAME = resp.json()['screen_name']
        predict = SentimentAnalyzer()
        #predict.calculateSentimentCoeff('@'+USERNAME, 50)
    variable = 1
    return render_template ('xyz.html', vari=variable)
