from datetime import timedelta
from flask import Blueprint
from flask import request
from flask_jwt_extended import create_access_token
from auth import admin_only
from models.user import User
from models.inventory import Inventory
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

# show the user's inventory
@users_bp.route("/<int:user_id>/inventory")
def view_inventory(user_id):
    stmt = db.select(User).where(User.id == user_id)
    user = db.session.scalar(stmt)
    if user:
        inventory = db.select(Inventory).where(Inventory.user_id == user_id)
        items = db.session.execute(inventory).fetchall()
        return {"inventory": items}
    else:
        return {"error": "User not found"}, 404
    
# add an item to the user's inventory
@users_bp.route("/<int:user_id>/inventory/add", methods=["POST"])
@admin_only
def add_to_inventory(user_id):
    stmt = db.select(User).where(User.id == user_id)
    user = db.session.scalar(stmt)
    if user:
        item_data = request.json
        item_data["user_id"] = user_id
        item = Inventory(**item_data)
        db.session.add(item)
        db.session.commit()
        return {"message": "Item added to inventory"}
    else:
        return {"error": "User not found"}, 404