from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from application import appp

db = SQLAlchemy(appp)

migrate = Migrate(app = appp, db = db)


