from flask import Blueprint, request
from init import db
from models.transaction import Transaction, TransactionSchema
from auth import admin_only

transactions_bp = Blueprint("transactions", __name__, url_prefix="/transactions")  # Blueprint for transactions

# •	POST /transactions
# 	•	GET /transactions/{id}
# 	•	GET /users/{id}/transactions

# •	POST /transactions
@transactions_bp.route("/create", methods=["POST"])
@admin_only
def create_transaction():
    transaction_data = TransactionSchema().load(request.json)
    # Convert the dictionary to an Transaction model instance
    new_transaction = Transaction(**transaction_data)
    db.session.add(new_transaction)
    db.session.commit()
    return TransactionSchema().dump(new_transaction)

# 	•	GET /transactions/{id}
@transactions_bp.route("/<int:transaction_id>")
def get_transaction(transaction_id):
    transaction_var = db.get_or_404(Transaction, transaction_id)
    return TransactionSchema().dump(transaction_var)

# 	•	GET /users/{id}/transactions
@transactions_bp.route("/<int:user_id>/transactions")
def get_user_transactions(user_id):
    stmt = db.select(Transaction).where(Transaction.buyer_id == user_id)
    transactions_var = db.session.scalars(stmt).all()
    return TransactionSchema(many=True).dump(transactions_var)

# 	•	PUT /transactions/{id}
# @transactions_bp.route("/<int:transaction_id>", methods=["PUT"])
# @admin_only
# def update_transaction(transaction_id):
#     transaction_var = db.get_or_404(Transaction, transaction_id)
#     transaction_data = TransactionSchema().load(request.json)
#     for key, value in transaction_data.items():
#         setattr(transaction_var, key, value)
#     db.session.commit()
#     return TransactionSchema().dump(transaction_var)