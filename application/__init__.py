from flask import Flask
from config import Config
from flask_login import LoginManager

# this is a special variable named to indentify the current application that is being rendered or passed to flask
appp = Flask(__name__)
appp.config.from_object(Config)
login = LoginManager(appp)
login.login_view = 'login'

from . import routes
from .model import models


@appp.shell_context_processor
def make_shell_context():
    from .UserDAC import db
    return{'db': db, 'User': models.User}