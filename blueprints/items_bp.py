from flask import Blueprint, request
from init import db
from models.items import Item, ItemSchema

items_bp = Blueprint('items', __name__, url_prefix='/items') # Blueprint for items

@items_bp.route('/')
def get_all_items():
    stmt = db.select(Item)
    items_var = db.session.scalars(stmt).all()
    return ItemSchema(many=True, only=["id", "title", "description", "date_created"]).dump(items_var)

@items_bp.route('/<int:id>')
def get_item(id):
    card_var = db.get_or_404(Item, id)
    return ItemSchema().dump(card_var)

@items_bp.route('/create', methods=['POST'])
# admin only
def create_item():
    new_item = ItemSchema().load(request.json)
    db.session.add(new_item)
    db.session.commit()
    return ItemSchema().dump(new_item)
