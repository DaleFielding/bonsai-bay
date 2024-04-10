from flask import render_template, request, redirect, url_for
from bonsai_bay import app, db
from bonsai_bay.models import Listing, User, Seller, SavedItem
import base64


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
     # Query the database to retrieve all listings
    all_listings = Listing.query.all()
    
    # Iterate over each listing to encode its image
    for listing in all_listings:
        if listing.image:
            # Encode image data to Base64
            listing.encoded_image = base64.b64encode(listing.image).decode('utf-8')
        else:
            listing.encoded_image = None
    
    # Render account page and pass listings to the template
    return render_template("account.html", listings=all_listings)


# Create Listing
@app.route("/create_listing", methods=["GET", "POST"])
def create_listing():
    if request.method == "POST":
        # Adding to help with determining issue with database
        app.logger.info("Form data received: %s", request.form)
        
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
            image=image_data
        )
        db.session.add(listing)
        db.session.commit()
        
        return redirect(url_for("account"))

    return render_template("account.html")


# Only for testing. Not needed in final version
# @app.route("/404")
# def errorpage():
#     return render_template("404.html")

