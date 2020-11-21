import os
from flask import Flask, redirect, url_for
from flask_login import LoginManager
from flask_dance.contrib.twitter import make_twitter_blueprint, twitter
from config import Configs

app = Flask(__name__)
app.config.from_object(Configs)
twitter_bp = make_twitter_blueprint()
app.register_blueprint(twitter_bp, url_prefix="/twlogin")
login = LoginManager(app)
login.login_view = 'login'
from . import routes
from .model import models

@app.shell_context_processor
def make_shell_context():
    from .UserDAC import db
    return{'db': db, 'User': models.User}