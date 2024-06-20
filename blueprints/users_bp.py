from datetime import timedelta
from flask import Blueprint
from flask import request
from flask_jwt_extended import create_access_token
from models.user import User
from init import bcrypt, db

users_bp = Blueprint("users", __name__, url_prefix="/users")


@users_bp.route("/login", methods=["POST"])
def login():
    # get the email and password from the request
    email = request.json["email"]
    password = request.json["password"]
    # compare email and password to the database
    stmt = db.select(User).where(User.email == email)
    user = db.session.scalar(stmt)
    if user and bcrypt.check_password_hash(user.password, password):
        # Generate the JWT token
        print("User is logged in")
        token = create_access_token(
            identity=user.id,
            additional_claims={"is_admin": user.is_admin},
            expires_delta=timedelta(hours=1),
        )
        # return the token
        return {"token": token}

    else:
        return {"error": "Invalid email or password"}, 401
    # error if not found