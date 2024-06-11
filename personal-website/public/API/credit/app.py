from flask import Flask, render_template, request, session, jsonify
from jinja2 import FileSystemLoader
from jinja2.environment import Environment
from helpers import checksum, card_type
from waitress import serve
import sqlite3

app = Flask(__name__, template_folder='../../templates', static_folder='../../static')

# Configure Jinja2 to load templates from both 'templates' and 'public' directories
template_loader = FileSystemLoader(['../../templates'])
app.jinja_loader = template_loader


@app.route("/")
def home():
    return render_template('index.html')


@app.route("/credit", methods=["GET", "POST"])
def credit():
    if request.method == "GET":
        return render_template("credit.html")

    data = request.get_json()
    credit_card = data.get("credit_card")

    if not credit_card:
        return jsonify({'status': 'error', 'message': '*Invalid Credit Card'}), 400
    
    try:
        credit_card = int(credit_card)
    except ValueError:
        return jsonify({'status': 'error', 'message': '*Numbers must be integers'}), 400    
    if credit_card <= 0:
        return jsonify({'status': 'error', 'message': '*Cannot be negative'}), 400

    if not checksum(credit_card):
        return jsonify({'status': 'error', 'message': '*Invalid Credit Card'}), 400

    return jsonify({'status': 'success', 'message': 'Valid'}), 200
    

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000)