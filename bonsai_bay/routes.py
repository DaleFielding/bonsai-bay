from flask import render_template
from bonsai_bay import app, db

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/account")
def account():
    return render_template("account.html")

@app.route("/")
def browse_bonsai():
    return render_template("index.html", scroll_to="browse-bonsai")

# Only for testing. Not needed in final version
# @app.route("/404")
# def errorpage():
#     return render_template("404.html")

