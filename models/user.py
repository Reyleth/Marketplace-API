from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy import String, Boolean
from typing import Optional
from marshmallow import fields
from marshmallow.validate import Length
from init import db, ma

# Define the User model
class User(db.Model):
    __tablename__ = "users"

    id: Mapped[int] = mapped_column(primary_key=True)
    email: Mapped[str] = mapped_column(String(200), unique=True)
    username: Mapped[Optional[str]] = mapped_column(String(100))
    password: Mapped[str] = mapped_column(String(200))
    created_at: Mapped[Optional[str]] = mapped_column(db.DateTime)
    is_admin: Mapped[bool] = mapped_column(Boolean(), server_default="false")

# Define the User schema
class UserSchema(ma.Schema):
    email = fields.Email(required=True)
    password = fields.String(validate=Length(min=8, error='Password must be at least 8 characters long'), required=True)

    class Meta:
        fields = ("id", "email", "name", "password", "is_admin")