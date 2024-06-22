from datetime import date
from flask import Blueprint
from init import db, bcrypt
from models.user import User
from models.item import Item


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

    items = [
        Item(
            name="Holy Grail",
            description="A sacred relic that grants eternal life",
            category="Artifact",
            rarity="Legendary",
            price=1000000.00,
            created_at=date.today(),
            owner_id=1  
            ),
        Item(
            name="Excalibur",
            description="A legendary sword wielded by King Arthur",
            category="Weapon",
            rarity="Legendary",
            price=500000.00,
            created_at=date.today(),
            owner_id=2
            ),
    ]

    db.session.add_all(users + items)
    db.session.commit()
    print("Tables created")