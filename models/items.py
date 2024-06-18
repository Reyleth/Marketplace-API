from init import db, ma
from datetime import date
from typing import Optional
from sqlalchemy.orm import Mapped, mapped_column

class Item(db.Model):

    __tablename__ = "items"

    # id = db.Column(db.Integer, primary_key=True)
    id: Mapped[int] = mapped_column(primary_key=True)

    # title = db.Column(db.String(100), unique=True, nullable=False)
    title: Mapped[str] = mapped_column(db.String(100), unique=True, nullable=False)
    # description = db.Column(db.Text(), unique=False, nullable=True)
    description: Mapped[Optional[str]] = mapped_column(db.Text())
    # date_created = db.Column(db.Date(), default=date.today())
    date_created: Mapped[date] = mapped_column(db.Date(), default=date.today())


class ItemSchema(ma.Schema):
    class Meta:
        model = Item
        fields = ["id", "title", "description", "date_created"]