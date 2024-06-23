from flask import Blueprint, request, jsonify
from flask_jwt_extended import jwt_required, get_jwt_identity
from marshmallow import ValidationError
from init import db
from models.user import User
from models.listing import Listing, ListingSchema
from auth import seller_only

listings_bp = Blueprint(
    "listings", __name__, url_prefix="/listings"
)  # Blueprint for listings

# • GET /listings
# •	POST /listings
# •	GET /listings/{id}
# •	PUT /listings/{id}
# •	DELETE /listings/{id}


# • GET /listings
@listings_bp.route("/")
def get_all_listings():
    stmt = db.select(Listing)
    listings_var = db.session.scalars(stmt).all()
    return ListingSchema(many=True).dump(listings_var)

    # • GET /listings/{id}


@listings_bp.route("/<int:listing_id>")
def get_listing(listing_id):
    listing_var = db.get_or_404(Listing, listing_id)
    return ListingSchema().dump(listing_var)

    # • POST /listings

@listings_bp.route("/create", methods=["POST"])
@jwt_required()  # Ensure that this route requires authentication
def create_listing():
    current_user_id = get_jwt_identity()
    user = User.query.get(current_user_id)
    if not user:
        return jsonify({"message": "User not found"}), 403

    new_listing_data = request.get_json()
    new_listing_data['seller_id'] = user.id

    # Use ListingSchema to load the data, ensuring it matches the Listing model
    try:
        new_listing = ListingSchema().load(new_listing_data)
    except ValidationError as err:
        return jsonify(err.messages), 400

    db.session.add(new_listing)
    db.session.commit()

    return ListingSchema().dump(new_listing), 201

    # • PUT /listings/{id}


@listings_bp.route("/<int:listing_id>", methods=["PUT"])
@seller_only
def update_listing(listing_id):
    db.get_or_404(Listing, listing_id)
    try:
        updated_listing = ListingSchema().load(request.json, partial=True)
    except ValidationError as err:
        return jsonify(err.messages), 400

    db.session.commit()
    return ListingSchema().dump(updated_listing), 200

    # • DELETE /listings/{id}


@listings_bp.route("/<int:listing_id>", methods=["DELETE"])
@seller_only
def delete_listing(listing_id):
    listing_var = db.get_or_404(Listing, listing_id)
    db.session.delete(listing_var)
    db.session.commit()
    return {"message": "Listing deleted successfully"}
