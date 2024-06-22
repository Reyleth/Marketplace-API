from flask import Blueprint, request
from init import db
from models.item import Item, ItemSchema
from auth import admin_only

	# Items Endpoints
	# •	GET /items
	# •	POST /items
	# •	GET /items/{id}
	# •	PUT /items/{id}
	# •	DELETE /items/{id}

items_bp = Blueprint('items', __name__, url_prefix='/items') # Blueprint for items

    # •	GET /items
@items_bp.route('/')
def get_all_items():
    stmt = db.select(Item)
    items_var = db.session.scalars(stmt).all()
    return ItemSchema(many=True, only=["id", "name", "description", "category", "rarity", "price"]).dump(items_var)

    # •	GET /items/{id}
@items_bp.route('/<int:id>')
def get_item(item_id):
    item_var = db.get_or_404(Item, item_id)
    return ItemSchema().dump(item_var)

    # •	POST /items
@items_bp.route('/create', methods=['POST'])
@admin_only
def create_item():
    new_item = ItemSchema().load(request.json)
    db.session.add(new_item)
    db.session.commit()
    return ItemSchema().dump(new_item)

	# •	PUT /items/{id}
@items_bp.route('/<int:item_id>', methods=['PUT'])
@admin_only
def update_item(item_id):
    item_var = db.get_or_404(Item, item_id)
    item_var = ItemSchema().load(request.json, partial=True)
    db.session.commit()
    return ItemSchema().dump(item_var)

    # •	DELETE /items/{id}
@items_bp.route('/<int:id>', methods=['DELETE'])
@admin_only
def delete_item(item_id):
    item_var = db.get_or_404(Item, item_id)
    db.session.delete(item_var)
    db.session.commit()
    return {"message": "Item deleted successfully"}
