from encrypt import encrypt_text, generate_key, load_public_key, encrypt_text_with_key, decrypt_text_with_key
from flask import Flask, render_template, request, url_for
app = Flask(__name__)


@app.route('/')
def hello():
    return render_template("welcome.html")

@app.route('/encrypt', methods=['POST', 'GET'])
def encrypt():
    if request.method == 'POST':
        text = request.form['text']
        key_id = request.form['key_id']
        x = encrypt_text(text, key_id)
        return render_template("encrypt.html", msg=x)

    return render_template("encrypt.html")

@app.route('/encrypt_with_key', methods=['POST', 'GET'])
def encrypt_with_key():
    if request.method == 'POST':
        text = request.form['text']
        password = request.form['pass']
        x = encrypt_text_with_key(text, password)
        return render_template("encrypt_with_key.html", msg=x)

    return render_template("encrypt_with_key.html")


@app.route('/decrypt_with_key', methods=['POST', 'GET'])
def decrypt_with_key():
    if request.method == 'POST':
        text = request.form['text']
        password = request.form['pass']
        x = decrypt_text_with_key(text, password)
        return render_template("decrypt_with_key.html", msg=x)

    return render_template("decrypt_with_key.html")


@app.route('/decrypt', methods=['POST', 'GET'])
def decrypt():
    if request.method == 'POST':
        text = request.form['text']
        key_id = request.form['key_id']
        x = encrypt_text(text, key_id)
        return render_template("decrypt.html", msg=x)

    return render_template("decrypt.html")

@app.route('/generate_keys', methods=['POST', 'GET'])
def generate_keys():
    if request.method == 'POST':
        key_id=request.form['key_id']
        bits=request.form['bits']
        x = generate_key(key_id, bits)
        return render_template('generate_keys.html', msg=x)
    else:
        return render_template("generate_keys.html")

@app.route('/load_key', methods=['POST', 'GET'])
def load_key():
    # clear_db()
    if request.method == 'POST':
        public_part = request.form['text']
        key_id = request.form['key_id']
        return_msg = load_public_key(key_id, public_part)
        return render_template("load_key.html", msg=return_msg)
    return_msg = 'GET req'
    return render_template("load_key.html", msg=return_msg)

@app.errorhandler(404)
def page_not_found(e):
    """Return a custom 404 error."""
    return 'Sorry, Nothing at this URL.', 404


@app.errorhandler(500)
def application_error(e):
    """Return a custom 500 error."""
    return 'Sorry, unexpected error: {}'.format(e), 500
