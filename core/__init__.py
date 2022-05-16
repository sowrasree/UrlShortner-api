from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_cors import CORS

from .config import Config

app = Flask(__name__)
CORS(app)

app.config['SQLALCHEMY_DATABASE_URI'] = Config.DB_DATABASE_URI
app.config['SQLALCHEMY_ECHO'] = False
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)
migrate = Migrate(app, db)

# app.test_client()
