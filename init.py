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

load_dotenv()
app = Flask(__name__)

app.config["SQLALCHEMY_DATABASE_URI"] = environ.get("DB_URI")
app.config['JWT_SECRET_KEY'] = environ.get('JWT_KEY')

db = SQLAlchemy(app, model_class=Base)
ma = Marshmallow(app)
# db.init_app(app)
jwt = JWTManager(app)
bcrypt = Bcrypt(app)

# from models.user import User
# from models.items import Item

