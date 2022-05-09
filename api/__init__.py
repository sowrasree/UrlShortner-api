from flask import Flask
from flask_sqlalchemy import SQLAlchemy

from core.config import Config

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = Config.DB_DATABASE_URI
db = SQLAlchemy(app)

