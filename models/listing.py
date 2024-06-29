from datetime import date
from sqlalchemy.orm import Mapped, mapped_column
from init import db
from marshmallow_sqlalchemy import SQLAlchemyAutoSchema

# Define the Listing model
class Listing(db.Model):
    __tablename__ = "listings"

    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)

    item_id: Mapped[int] = mapped_column(db.Integer, db.ForeignKey('items.id'), nullable=False)

    seller_id: Mapped[int] = mapped_column(db.Integer, db.ForeignKey('users.id'), nullable=False)

    price: Mapped[float] = mapped_column(db.Float(), nullable=False)

    quantity: Mapped[int] = mapped_column(db.Integer, nullable=False, default=1)

    status: Mapped[str] = mapped_column(db.String, nullable=False, default="active")

    created_at: Mapped[date] = mapped_column(db.Date(), nullable=False, default=date.today())

# Define the Listing schema
class ListingSchema(SQLAlchemyAutoSchema):
    class Meta:
        model = Listing
        sqla_session = db.session
        load_instance = True
        include_fk = True
        fields = ["id", "item_id", "seller_id", "price", "quantity", "status", "created_at"]
