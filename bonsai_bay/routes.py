from flask import render_template
from bonsai_bay import app, db

@app.route("/")
def home():
    return render_template("base.html")

