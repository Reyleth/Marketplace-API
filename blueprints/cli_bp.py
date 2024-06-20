from datetime import date
from flask import Blueprint
from init import db, bcrypt
from models.user import User


db_commands = Blueprint('db', __name__)

@db_commands.cli.command("create")
def create_db():
    db.drop_all()
    db.create_all()
    print("Database created")

    users = [
        User(
            email="admin@spam.com",
            username="Admin",
            password=bcrypt.generate_password_hash("spinynorman").decode("utf-8"),
            created_at=date.today(),
            is_admin=True
            ),
        User(
            email="reguser@spam.com",
            username="John Cleese",
            password=bcrypt.generate_password_hash("tisbutascratch").decode("utf-8"),
            created_at=date.today(),
            ),
    ]

    db.session.add_all(users)
    db.session.commit()
    print("Tables created")