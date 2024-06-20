from datetime import date
from init import app


@app.route('/')
def hello_world():
    return 'Welcome to the Marketplace API!'

@app.route("/time")
def time():
    return {"time": date.today()}