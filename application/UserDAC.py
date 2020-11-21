from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from application import app

db = SQLAlchemy(app)

migrate = Migrate(app = app, db = db)


