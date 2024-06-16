from init import app


@app.route('/')
def hello_world():
    return 'Welcome to the Marketplace API!'

@app.route('/login')
def login():
    return 'Login'