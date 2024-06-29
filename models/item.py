from init import db, ma
from datetime import date
from typing import Optional
from sqlalchemy.orm import Mapped, mapped_column

# Define the Item model
class Item(db.Model):

    __tablename__ = "items"

    # id = db.Column(db.Integer, primary_key=True)
    id: Mapped[int] = mapped_column(db.Integer, primary_key=True, autoincrement=True)

    # title = db.Column(db.String(100), unique=True, nullable=False)
    name: Mapped[str] = mapped_column(db.String(100), unique=True, nullable=False)
    # description = db.Column(db.Text(), unique=False, nullable=True)
    description: Mapped[Optional[str]] = mapped_column(db.Text())
    # category = db.Column(db.String(100), unique=False, nullable=True)
    category: Mapped[Optional[str]] = mapped_column(db.String(100))
    # rarity = db.Column(db.String(100), unique=False, nullable=True)
    rarity: Mapped[Optional[str]] = mapped_column(db.String(100))
    # price = db.Column(db.Float(), unique=False, nullable=True)
    price: Mapped[Optional[float]] = mapped_column(db.Float())
    # created_at = db.Column(db.Date(), nullable=False)
    created_at: Mapped[date] = mapped_column(db.Date(), nullable=False, default=date.today())

# Define the Item schema
class ItemSchema(ma.Schema):
    class Meta:
        model = Item
        fields = ["id", "name", "description", "category", "rarity", "price"]