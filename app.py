from flask import Flask, render_template, request, session, jsonify, redirect
from jinja2 import FileSystemLoader
from jinja2.environment import Environment
from helpers import checksum, card_type, db_init, insert_recorder, generate_user_id
from werkzeug.security import generate_password_hash
import os

app = Flask(__name__, template_folder='templates', static_folder='static')

app.secret_key = os.urandom(24)

# Configure Jinja2 to load templates from both 'templates' and 'public' directories
template_loader = FileSystemLoader(['templates'])
app.jinja_loader = template_loader


# Initialize the database
db_init()

@app.route("/")
def home():
    return render_template('index.html')

# (WORK LATER): include a LinkedIn API
@app.route("/hackathon")
def hackathon():
    return redirect("https://www.linkedin.com/feed/update/urn:li:activity:6947073917517733888/")


@app.route("/credit-card", methods=["GET", "POST"])
def credit():
    if request.method == "GET":
        return render_template("credit.html")

    if 'user_id' not in session:
        session['user_id'] = generate_user_id()

    user_id = session['user_id']

    data = request.get_json()
    credit_card = data.get("credit_card")

    if not credit_card:
        return jsonify({'status': 'error', 'message': '*Cannot be empty'}), 400
    
    try:
        credit_card = int(credit_card)
    except ValueError:
        return jsonify({'status': 'error', 'message': '*Numbers must be integers'}), 400    
    if credit_card <= 0:
        return jsonify({'status': 'error', 'message': '*Cannot be negative'}), 400
    if len(str(credit_card)) < 13:
        return jsonify({'status': 'error', 'message': '*Invalid'}), 400
    if not checksum(credit_card):
        return jsonify({'status': 'error', 'message': '*Invalid'}), 400

    credit_card_type = card_type(str(credit_card))

    if not credit_card_type:
        return jsonify({'status': 'error', 'message': '*Card Must be VISA, MASTERCARD, or AMEX'}), 400

    # Encrypts the credit_card number before storing it in the databse
    credit_card_hashed = generate_password_hash(str(credit_card), method='pbkdf2:sha256')

    insert_recorder(user_id, credit_card_hashed, credit_card_type)

    return jsonify({'status': 'success', 'message': 'Valid', 'type': credit_card_type}), 200
    
@app.errorhandler(500)
def internal_error(error):
    return jsonify({'status': 'error', 'message': 'Honey, it is me not you, please do not take this seriously'}), 500

@app.errorhandler(404)
def not_found(error):
    return jsonify({'status': 'error', 'message': 'So, you entered the backrooms in the hope of finding a story to tell? Not today, the page is not found'}), 404

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000)