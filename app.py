from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

from config import SQLALCHEMY_DATABASE_URI

app = Flask(__name__)
app.config.from_object('config')

app.config["SQLALCHEMY_DATABASE_URI"] = SQLALCHEMY_DATABASE_URI

db = SQLAlchemy(app)
migrate = Migrate(app, db)


from models import process_model

from controllers import process_controller

if __name__ == '__main__':
    app.run()
