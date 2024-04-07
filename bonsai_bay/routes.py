from flask import render_template
from bonsai_bay import app, db

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/account")
def account():
    return render_template("account.html")

