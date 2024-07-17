from datetime import date
from flask import Blueprint
from init import db, bcrypt
from models.user import User
from models.item import Item
from models.inventory import Inventory
from models.listing import Listing
# from models.transaction import Transaction


db_commands = Blueprint('db', __name__)

# Create the database
@db_commands.cli.command("create")
def create_db():
    db.drop_all()
    db.create_all()
    print("Database created")

    # Create sample data
    users = [
        User(
            email="admin@spam.com",
            username="Admin",
            password=bcrypt.generate_password_hash("secretpassword").decode("utf-8"),
            created_at=date.today(),
            is_admin=True
            ),
        User(
            email="reguser@spam.com",
            username="John Smith",
            password=bcrypt.generate_password_hash("randompassword").decode("utf-8"),
            created_at=date.today(),
            ),
        User(
            email="helloworld@random.com",
            username="Hello World",
            password=bcrypt.generate_password_hash("protocol_alpha").decode("utf-8"),
            created_at=date.today()
        ),
        User(
            email="randomuserthefourth@random.com",
            username="Random User IV",
            password=bcrypt.generate_password_hash("password123").decode("utf-8"),
            created_at=date.today()
        ),
        User(
            email="userthefifth@random.com",
            username="User V",
            password=bcrypt.generate_password_hash("password123").decode("utf-8"),
            created_at=date.today()
        ),
        User(
            email="randomuser2342@mail.com",
            username="Random User 2342",
            password=bcrypt.generate_password_hash("password123").decode("utf-8"),
            created_at=date.today()
        )
    ]

    items = [
        Item(
            name="Holy Grail",
            description="A sacred relic that grants eternal life",
            category="Artifact",
            rarity="Legendary",
            price=1000000.00,
            created_at=date.today(), 
            ),
        Item(
            name="Excalibur",
            description="A legendary sword wielded by King Arthur",
            category="Weapon",
            rarity="Legendary",
            price=500000.00,
            created_at=date.today(),
            ),
        Item(
            name="Mjolnir",
            description="The hammer of Thor, the Norse god of thunder",
            category="Weapon",
            rarity="Legendary",
            price=500000.00,
            created_at=date.today(),
        ),
        Item(
            name="Dragon's Breath",
            description="A powerful potion that grants the user the ability to breathe fire",
            category="Consumable",
            rarity="Epic",
            price=100000.00,
            created_at=date.today(),
        ),
        Item(
            name="Phoenix Down",
            description="A feather from a phoenix that can revive the dead",
            category="Consumable",
            rarity="Rare",
            price=50000.00,
            created_at=date.today(),
        ),
        Item(
            name="Elixir",
            description="A magical potion that restores health and mana",
            category="Consumable",
            rarity="Common",
            price=10000.00,
            created_at=date.today(),
        ),
        Item(
            name="Potion",
            description="A basic potion that restores health",
            category="Consumable",
            rarity="Common",
            price=1000.00,
            created_at=date.today
        ),
        Item(
            name="Antidote",
            description="A potion that cures poison",
            category="Consumable",
            rarity="Common",
            price=1000.00,
            created_at=date.today()
        )
    ]

    inventories = [
        Inventory(
            user_id=1,
            item_id=1,
            quantity=1,
            ),
        Inventory(
            user_id=2,
            item_id=2,
            quantity=1,
            ),
        Inventory(
            user_id=3,
            item_id=3,
            quantity=1,
            ),
        Inventory(
            user_id=4,
            item_id=4,
            quantity=1,
            )
    ]

    listings = [
        Listing(
            item_id=1,
            seller_id=1,
            price=1000000.00,
            quantity=1,
            status="active",
            created_at=date.today(),
            ),
        Listing(
            item_id=2,
            seller_id=2,
            price=500000.00,
            quantity=1,
            status="active",
            created_at=date.today(),
            ),
        Listing(
            item_id=3,
            seller_id=3,
            price=500000.00,
            quantity=1,
            status="active",
            created_at=date.today(),
            ),
    ]

    transactions = [
    ]

    db.session.add_all(users + items + inventories + listings + transactions)
    db.session.commit()
    print("Tables created")