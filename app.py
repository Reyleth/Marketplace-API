from datetime import datetime
from init import app
from blueprints.cli_bp import db_commands
from blueprints.users_bp import users_bp
from blueprints.items_bp import items_bp
from blueprints.listings_bp import listings_bp
# from blueprints.transactions_bp import transactions_bp

app.register_blueprint(db_commands)
app.register_blueprint(users_bp)
app.register_blueprint(items_bp)
app.register_blueprint(listings_bp)
# app.register_blueprint(transactions_bp)


@app.route('/')
def hello_world():
    return 'Welcome to the Marketplace API!'

@app.route("/time")
def time():
    return {"time": datetime.now().strftime("%Y-%m-%d %H:%M")}