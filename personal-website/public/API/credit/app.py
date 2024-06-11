from flask import Flask, render_template, request, session
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

    credit_card = request.form.get("credit_card")

    if not credit_card:
        return 404
    
    try:
        credit_card = int(credit_card)
    except ValueError:
        return 404

    if credit_card <= 0:
        return 404

    if not checksum(credit_card):
        return 404

    card_type = card_type(credit_card)

    user_id = session["user_id"]
    if user_id:
        db = sqlite3.connect
        cursor = db.cursor()
        db.execute("INSERT INTO credit_log (user_id, credit_card, card_type) VALUES (?, ?, ?)", user_id, int(credit_card), card_type)
        db.commit()
        db.close

    return 200
    

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000)