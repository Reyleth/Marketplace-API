from functools import wraps
from flask_jwt_extended import get_jwt, jwt_required


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