from os import environ
from flask import Flask
from flask_marshmallow import Marshmallow
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import DeclarativeBase
from dotenv import load_dotenv
from flask_jwt_extended import JWTManager
from flask_bcrypt import Bcrypt


class Base(DeclarativeBase):
    pass

# Load environment variables from .env file
load_dotenv()

# Define the Flask application
app = Flask(__name__)

# Define configs
app.config["SQLALCHEMY_DATABASE_URI"] = environ.get("DB_URI")
app.config['JWT_SECRET_KEY'] = environ.get('JWT_KEY')

# Initialize the database
db = SQLAlchemy(app, model_class=Base)
ma = Marshmallow(app)
# db.init_app(app)
jwt = JWTManager(app)
bcrypt = Bcrypt(app)
