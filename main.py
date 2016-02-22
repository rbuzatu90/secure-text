"""`main` is the top level module for your Flask application."""

# Import the Flask Framework
from my_db import Employee
from encrypt import encrypt_text, generate_key
from flask import Flask, render_template, request, url_for
app = Flask(__name__)
# Note: We don't need to call run() since our application is embedded within
# the App Engine WSGI application server.


@app.route('/')
def hello():
    """Return a friendly HTTP greeting."""
    x = Employee(name="John", role="manager")
    # x= "lol"
    # print x
    return render_template("welcome.html", user=x)

@app.route('/encrypt', methods=['POST', 'GET'])
def encrypt():
    """Return a friendly HTTP greeting."""
    if request.method == 'POST':
        text = request.form['text']
        key_id = request.form['key_id']
        x = encrypt_text(text, key_id)

        return render_template("encrypt.html", msg=x)

    # encrypt_text(text, key)
    return render_template("encrypt.html")

@app.route('/generate_keys', methods=['POST', 'GET'])
def generate_keys():
    if request.method == 'POST':
        key_id=request.form['key_id']
        bits=request.form['bits']
        x = generate_key(key_id, bits)
        return render_template('generate_keys.html', msg=x)
    else:
        x = "lol"
        return render_template("generate_keys.html")

@app.errorhandler(404)
def page_not_found(e):
    """Return a custom 404 error."""
    return 'Sorry, Nothing at this URL.', 404


@app.errorhandler(500)
def application_error(e):
    """Return a custom 500 error."""
    return 'Sorry, unexpected error: {}'.format(e), 500
