from os import environ
from flask import Flask
from flask_marshmallow import Marshmallow
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import DeclarativeBase
from dotenv import load_dotenv

class Base(DeclarativeBase):
    pass

load_dotenv()
app = Flask(__name__)

app.config["SQLALCHEMY_DATABASE_URI"] = environ.get("DB_URI")

db = SQLAlchemy(app, model_class=Base)
ma = Marshmallow(app)
# db.init_app(app)

