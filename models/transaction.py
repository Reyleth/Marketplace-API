from datetime import date
from init import db, ma
from typing import Optional
from sqlalchemy.orm import Mapped, mapped_column

class Transaction(db.Model):

    __tablename__ = "transactions"

    id: Mapped[int] = mapped_column(primary_key=True)

    buyer_id: Mapped[int] = mapped_column(db.Integer, db.ForeignKey('users.id'), nullable=False)

    seller_id: Mapped[int] = mapped_column(db.Integer, db.ForeignKey('users.id'), nullable=False)

    item_id: Mapped[int] = mapped_column(db.Integer, db.ForeignKey('items.id'), nullable=False)

    listing_id: Mapped[int] = mapped_column(db.Integer, db.ForeignKey('listings.id'), nullable=False)

    price: Mapped[float] = mapped_column(db.Float(), nullable=False)

    quantity: Mapped[int] = mapped_column(db.Integer, nullable=False)

    status: Mapped[Optional[str]] = mapped_column(db.String(100), nullable=False)

    created_at: Mapped[date] = mapped_column(db.Date(), nullable=False)
