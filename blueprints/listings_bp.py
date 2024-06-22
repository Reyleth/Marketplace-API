from flask import Blueprint, request
from init import db
from models.listing import Listing, ListingSchema

listings_bp = Blueprint('listings', __name__, url_prefix='/listings') # Blueprint for listings

	# • GET /listings
	# •	POST /listings
	# •	GET /listings/{id}
	# •	PUT /listings/{id}
	# •	DELETE /listings/{id}

    # • GET /listings
@listings_bp.route('/')
def get_all_listings():
    stmt = db.select(Listing)
    listings_var = db.session.scalars(stmt).all()
    return ListingSchema(many=True, only=["id", "item_id", "seller_id", "price", "quantity", "status", "created_at"]).dump(listings_var)

    # • GET /listings/{id}
@listings_bp.route('/<int:id>')
def get_listing(listing_id):
    listing_var = db.get_or_404(Listing, listing_id)
    return ListingSchema().dump(listing_var)

    # • POST /listings
@listings_bp.route('/create', methods=['POST'])
# seller only
def create_listing():
    new_listing = ListingSchema().load(request.json)
    db.session.add(new_listing)
    db.session.commit()
    return ListingSchema().dump(new_listing)

    # • PUT /listings/{id}
@listings_bp.route('/<int:id>', methods=['PUT'])
# seller only
def update_listing(listing_id):
    listing_var = db.get_or_404(Listing, listing_id)
    listing_var = ListingSchema().load(request.json, partial=True)
    db.session.commit()
    return ListingSchema().dump(listing_var)

    # • DELETE /listings/{id}
@listings_bp.route('/<int:id>', methods=['DELETE'])
# seller only
def delete_listing(listing_id):
    listing_var = db.get_or_404(Listing, listing_id)
    db.session.delete(listing_var)
    db.session.commit()
    return {"message": "Listing deleted successfully"}


