from flask import render_template, request, redirect, url_for, flash, jsonify
from bonsai_bay import app, db
from bonsai_bay.models import Listing, User
from flask_login import login_user, login_required, current_user, logout_user
from datetime import datetime
import base64

# Temporary, I will include within the appropriate route once I set up registration and login.
@app.context_processor
def inject_user_data():
    users = User.query.all()
    return dict(users=users)


# Homepage
@app.route("/")
def home():
    # Query the database to retrieve all listings
    listings = Listing.query.all()
    
    # Iterate over each listing and encode the image
    for listing in listings:
        if listing.image:
            listing.encoded_image = base64.b64encode(listing.image).decode('utf-8')
        else:
            listing.encoded_image = None
    
    # Render homepage page and pass listings to the template so that they can be displayed
    return render_template("index.html", listings=listings)


# Homepage, scrolled to browse_bonsai id
@app.route("/")
def browse_bonsai():
    return render_template("index.html", scroll_to="browse-bonsai")


# Item Page for styling
@app.route("/item")
def item():
    return render_template("item.html")


# Item Page with listing id passed in
@app.route("/item/<int:listing_id>")
def listed_item(listing_id):
    # Query the database to obtain the listing_id or display 404
    listing = Listing.query.get_or_404(listing_id)
    
    # Encode image if found
    if listing.image:
        listing.encoded_image = base64.b64encode(listing.image).decode('utf-8')
    else:
        listing.encoded_image = None
    
    # Render the item page and pass listings to the template so that they can be displayed
    return render_template("item.html", listing=listing)


# Register User
@app.route("/register", methods=["POST"])
def register():
    username = request.form.get("username")
    email = request.form.get("email")
    password = request.form.get("password")
    location = request.form.get("location")

    # Check if the user already exists
    if User.query.filter_by(username=username).first() or User.query.filter_by(email=email).first():
        return jsonify({"success": False, "message": "User already exists, please login if this is you."})

    # Create a new user object and save it to the database
    new_user = User(username=username, email=email, location=location)
    new_user.password = password 
    db.session.add(new_user)
    db.session.commit()

    return jsonify({"success": True, "message": "Registration was successful."})


# User Login
@app.route("/login", methods=["POST"])
def login():
    username_or_email = request.form.get("username_or_email")
    password = request.form.get("password")

    # Check if a user with the provided username or email exists
    user = User.query.filter(
        (User.username == username_or_email) | (User.email == username_or_email)
    ).first()

    if user and user.verify_password(password):
        login_user(user)

        flash("Login successful", "success")
        # Redirect to the account page upon successful login
        return redirect(url_for("account"))
    else:
        # If the user doesn't exist or the password is incorrect, show an error message
        flash("Invalid username/email or password. Please try again.", "error")
        # You may want to redirect back to the login page or render the base template again
        # For now, let's redirect to the home page
        return redirect(url_for("home"))


# Account Page
@app.route("/account")
@login_required
def account():
    user = current_user
    if user:
        # Query the database to retrieve all listings for the current user
        listings = Listing.query.filter_by(user_id=user.id).all()

        # Iterate over each listing and encode the image
        for listing in listings:
            if listing.image:
                listing.encoded_image = base64.b64encode(listing.image).decode('utf-8')
            else:
                listing.encoded_image = None

        # Render account page and pass listings to the template so that they can be displayed
        return render_template("account.html", listings=listings, user=user)
    else:
        flash("User not found", "error")
        return redirect(url_for("home"))


@app.route("/create_listing", methods=["GET", "POST"])
@login_required
def create_listing():
    if request.method == "POST":
        user = current_user 

        # To handle the uploaded files
        image_file = request.files['image']
        if image_file:
            image_data = image_file.read()
            encoded_image = base64.b64encode(image_data).decode('utf-8')
        else:
            image_data = None
            encoded_image = None

        # Create new listing object using my form data
        listing = Listing(
            title=request.form.get("title"),
            species=request.form.get("species"),
            tree_type=request.form.get("tree_type"),
            indoor_outdoor=request.form.get("indoor_outdoor"),
            description=request.form.get("description"),
            height=request.form.get("height"),
            price=request.form.get("price"),
            care_tips=request.form.get("care_tips"),
            image=image_data,
            user_id=user.id  # Assign the user_id of the current user
        )

        listing.date_added = datetime.now()

        db.session.add(listing)
        db.session.commit()

        return redirect(url_for("account"))
    return render_template("account.html")


# Delete Listing
@app.route("/delete_listing/<int:listing_id>")
def delete_listing(listing_id):
    # Query the database to obtain the listing_id or display 404
    listing = Listing.query.get_or_404(listing_id)
    # Delete the relevant listing
    db.session.delete(listing)
    db.session.commit()
    # Redirect to account template
    return redirect(url_for("account"))

    
# Only for testing. Not needed in final version
# @app.route("/404")
# def errorpage():
#     return render_template("404.html")