from init import db, ma
from sqlalchemy.orm import Mapped, mapped_column

class Inventory(db.Model):

    __tablename__ = "inventory"

    # id = db.Column(db.Integer, primary_key=True)
    id: Mapped[int] = mapped_column(primary_key=True)

    user_id: Mapped[int] = mapped_column(db.Integer, db.ForeignKey('users.id'), nullable=False)

    item_id: Mapped[int] = mapped_column(db.Integer, db.ForeignKey('items.id'), nullable=False)

    quantity: Mapped[int] = mapped_column(db.Integer, nullable=False)

class InventorySchema(ma.Schema):
    class Meta:
        model = Inventory
        fields = ["id", "player_id", "item_id", "quantity"]
