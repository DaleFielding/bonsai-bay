from flask import render_template, request, redirect, url_for
from bonsai_bay import app, db
from bonsai_bay.models import Listing, User, Seller, SavedItem
import base64


# Homepage
@app.route("/")
def home():
    return render_template("index.html")


# Homepage, scrolled to browse_bonsai id
@app.route("/")
def browse_bonsai():
    return render_template("index.html", scroll_to="browse-bonsai")


# Account Page
@app.route("/account")
def account():
     # Query the database to retrieve all listings
    listings = Listing.query.all()
    
    # Iterate over each listing and encode the image
    for listing in listings:
        if listing.image:
            listing.encoded_image = base64.b64encode(listing.image).decode('utf-8')
        else:
            listing.encoded_image = None
    
    # Render account page and pass listings to the template so that they can be displayed
    return render_template("account.html", listings=listings)


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

