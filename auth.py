from functools import wraps
from flask_jwt_extended import get_jwt, jwt_required

# This decorator will check if the user is an admin
def admin_only(func):
    @wraps(func)
    def inner(*args, **kwargs):
        @jwt_required()
        def check_admin():
            claims = get_jwt()
            if not claims.get("is_admin"):
                return {"error": "Admin only!"}, 403
            return func(*args, **kwargs)
        return check_admin()
    return inner

# This decorator will check if the user is authenticated
def user_auth(func):
    @wraps(func)
    def inner(*args, **kwargs):
        @jwt_required()
        def check_user_auth():
            return func(*args, **kwargs)
        return check_user_auth()
    return inner

# This decorator will check if the user_id in the JWT is the same as the user_id in the URL
def check_user(func):
    @wraps(func)
    def inner(*args, **kwargs):
        @jwt_required()
        def check_user_match():
            claims = get_jwt()
            if claims.get("user_id") != kwargs.get("user_id"):
                return {"error": "Unauthorized"}, 403
            return func(*args, **kwargs)
        return check_user_match()
    return inner

# Decorator to check if the user is the seller of the listing
def seller_only(func):
    @wraps(func)
    def inner(*args, **kwargs):
        @jwt_required()
        def check_seller():
            claims = get_jwt()
            user_id = int(claims.get("user_id", -1))  # Default to -1 if not found
            seller_id = int(kwargs.get("seller_id", -2))  # Default to -2 if not found; ensures mismatch if either is missing
            
            if user_id != seller_id:
                return {"error": "Unauthorized"}, 403
            return func(*args, **kwargs)
        return check_seller()
    return inner

# Decorator to check if the user is a potential buyer of the transaction
def buyer_only(func):
    @wraps(func)
    def inner(*args, **kwargs):
        @jwt_required()
        def check_buyer():
            claims = get_jwt()
            user_id = int(claims.get("user_id", -1))  # Default to -1 if not found
            buyer_id = int(kwargs.get("buyer_id", -2))  # Default to -2 if not found; ensures mismatch if either is missing
            if user_id != buyer_id:
                return {"error": "Unauthorized"}, 403
            return func(*args, **kwargs)
        return check_buyer()
    return inner

