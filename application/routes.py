from flask import render_template, redirect, flash, url_for, request
from flask_login import current_user, login_user, logout_user
from application import app
from .UserDAC import db
from .forms import LoginForm, RegistrationForm
from werkzeug.urls import url_parse
from flask_dance.contrib.twitter import twitter
import json


@app.route('/')
def redir():
    return redirect('/index')
@app.route("/tlogin")
def tweet():
    return redirect(url_for("twitter.login"))

@app.route("/index")
@app.route("/home")
def index():
    if not twitter.authorized:
        return redirect(url_for("twitter.login"))
    resp = twitter.get("account/verify_credentials.json")
    print(twitter)
    assert resp.ok
    tweets=resp.json()["screen_name"]
    return render_template('index.html', tweets=tweets)



'''
@app.route('/logins', methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('index'))
    form = LoginForm()
    if form.validate_on_submit():
        print(form.username.data)
        user = User.query.filter_by(username=form.username.data).first()
        if user is None or not user.check_password(form.password.data):
            flash('Invalid username or password')
            return redirect(url_for('logins'))
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

'''