from flask import render_template, request, redirect, url_for
from bonsai_bay import app, db
from bonsai_bay.models import Tree

# Homepage
@app.route("/")
def home():
    return render_template("index.html")

# Homepage - scrolled to browse_bonsai id
@app.route("/")
def browse_bonsai():
    return render_template("index.html", scroll_to="browse-bonsai")


# Account Page
@app.route("/account")
def account():
    return render_template("account.html")

# Create Listing
@app.route("/create_listing", methods=["GET", "POST"])
def create_listing():
    if request.method == "POST":
        tree = Tree (
            title=request.form.get("title"),
            species=request.form.get("species"),
            tree_type=request.form.get("tree_type"),
            indoor_outdoor=request.form.get("indoor_outdoor"),
            description=request.form.get("description"),
            height=request.form.get("height"),
            price=request.form.get("price"),
            care_tips=request.form.get("care_tips"),
            image=request.form.get("image"),
        )
        db.session.add(tree)
        db.session.commit()
        return redirect(url_for("accounts"))
    return render_template("account.html")


# Only for testing. Not needed in final version
# @app.route("/404")
# def errorpage():
#     return render_template("404.html")

