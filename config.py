import os
from dotenv import load_dotenv

load_dotenv()
basedir = os.path.abspath(os.path.dirname(__file__))


class Configs(object):
    #its a key used as a signature key used to make sure the content sent isnt intercepted
    SECRET_KEY = os.environ.get('SECRET_KEY') or "secret_string"
    ENV = os.environ.get('FLASK_ENV', default='production')
    DEBUG = ENV == 'development'
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or  'sqlite:///' + os.path.join(basedir, 'app.db')
    SQLALCHEMY_TRACK_MODIFICATIONS = True
    TWITTER_OAUTH_CLIENT_KEY = os.environ.get('TWITTER_OAUTH_CLIENT_KEY', default='TWITTER CONSUMER KEY')
    TWITTER_OAUTH_CLIENT_SECRET = os.environ.get('TWITTER_OAUTH_CLIENT_SECRET', default='ENTER TWITTER CONSUMER SECRET')
    bot_secret = os.environ.get('bot_secret')
