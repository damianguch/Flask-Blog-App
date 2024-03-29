
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import email_validator

app = Flask(__name__)
app.config['SECRET_KEY'] = '5a67bfd67fea43b949e138e4048bf192'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'

db = SQLAlchemy(app)

from flaskblog import routes
