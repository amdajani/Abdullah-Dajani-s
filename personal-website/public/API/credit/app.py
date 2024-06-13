from flask import Flask, render_template, request, session, jsonify, redirect
from jinja2 import FileSystemLoader
from jinja2.environment import Environment
from helpers import checksum, card_type, db_init, insert_recorder, generate_user_id
from werkzeug.security import generate_password_hash
from waitress import serve
import os

app = Flask(__name__, template_folder='../../templates', static_folder='../../static')

# Configure Jinja2 to load templates from both 'templates' and 'public' directories
template_loader = FileSystemLoader(['../../templates'])
app.jinja_loader = template_loader

app.secret_key = os.urandom(24)

db_init()

@app.route("/")
def home():
    return render_template('index.html')


@app.route("/hackathon")
def hackathon():
    return redirect("https://www.linkedin.com/feed/update/urn:li:activity:6947073917517733888/")


@app.route("/credit", methods=["GET", "POST"])
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
        return jsonify({'status': 'error', 'message': '*Invalid1'}), 400
    if not checksum(credit_card):
        return jsonify({'status': 'error', 'message': '*Invalid2'}), 400

    credit_card_type = card_type(str(credit_card))

    if not credit_card_type:
        return jsonify({'status': 'error', 'message': '*Card Must be VISA, MASTERCARD, or AMEX'}), 400

    credit_card_hashed = generate_password_hash(str(credit_card), method='pbkdf2:sha256')

    insert_recorder(user_id, credit_card_hashed, credit_card_type)

    return jsonify({'status': 'success', 'message': 'Valid', 'type': credit_card_type}), 200
    

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000)