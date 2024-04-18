from flask import render_template, request, redirect, url_for, flash, jsonify, Response
from bonsai_bay import app, db
from bonsai_bay.models import Listing, User, SavedItem
from flask_login import login_user, login_required, current_user, logout_user
from datetime import datetime
import base64, os, requests

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
@app.route("/scroll_to")
def browse_bonsai():
     # Query the database to retrieve all listings
    listings = Listing.query.all()
    
    # Iterate over each listing and encode the image
    for listing in listings:
        if listing.image:
            listing.encoded_image = base64.b64encode(listing.image).decode('utf-8')
        else:
            listing.encoded_image = None
    
    # Render homepage page and pass listings to the template so that they can be displayed
    return render_template("index.html", listings=listings, scroll_to="browse-bonsai")


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

    # Check if user exists and the password is correct, 
    # Log user in if so
    if user and user.verify_password(password):
        login_user(user)
        # Return JSON success response with a message
        return jsonify({"success": True, "message": "Login successful"})
    else:
        # Return JSOn unsuccesful response with message
        return jsonify({"success": False, "message": "Invalid username/email/password. Please try again."})


# Check if logged in
@app.route("/is_logged_in")
def is_logged_in():
    return jsonify({"logged_in": current_user.is_authenticated})


# Logout User
@app.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('home'))


# Account Page
@app.route("/account")
@login_required
def account():
    user = current_user
    if user:
        # Query all listings for the current user
        user_listings = Listing.query.filter_by(user_id=user.id).all()

        # query all saved items for the current user
        saved_items = SavedItem.query.filter_by(user_id=user.id).all()

        # create empty lists for listings and save_listings
        listings = []
        saved_listings = []

        # Iterate over each listing and encode the image
        for listing in user_listings:
            if listing.image:
                listing.encoded_image = base64.b64encode(listing.image).decode('utf-8')
            else:
                listing.encoded_image = None
            # Append to the listings list
            listings.append(listing)

        for saved_item in saved_items:
            listing = Listing.query.get(saved_item.listing_id)
            if listing:
                if listing.image:
                    listing.encoded_image = base64.b64encode(listing.image).decode('utf-8')
                else:
                    listing.encoded_image = None
                saved_listings.append(listing)

        # Render account page and pass listings and saved_listings to the template
        return render_template("account.html", listings=listings, saved_listings=saved_listings, user=user)
    else:
        flash("User not found", "error")
        return redirect(url_for("home"))


# Create Listing
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
        # including assign user_id from current user
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
            user_id=user.id  
        )

        listing.date_added = datetime.now()

        db.session.add(listing)
        db.session.commit()

        return redirect(url_for("account"))
    return render_template("account.html")


# Edit Listing
@app.route("/edit_listing/<int:listing_id>", methods=["GET", "POST"])
@login_required
def edit_listing(listing_id):
    listing = Listing.query.get_or_404(listing_id)
    if request.method == "POST":
        # Update listing with the changes
        listing.title = request.form.get("edit_title")
        listing.species = request.form.get("edit_species")
        listing.tree_type = request.form.get("edit_tree_type")
        listing.indoor_outdoor = request.form.get("edit_indoor_outdoor")
        listing.description = request.form.get("edit_description")
        listing.height = request.form.get("edit_height")
        listing.price = request.form.get("edit_price")
        listing.care_tips = request.form.get("edit_care_tips")
        image_file = request.files.get('edit_image')
        if image_file:
            image_data = image_file.read()
            listing.image = image_data

        db.session.commit()

        return redirect(url_for("account"))
    else:
        # Pass the listing object to the account route
        return redirect(url_for("account", listing=listing))


# Delete Listing
@app.route("/delete_listing/<int:listing_id>", methods=["POST"])
def delete_listing(listing_id):
    # Added check for POST to ensure delete only takes place after confirmation/when the form is submitted
    if request.method == "POST":
        # Query the database to obtain the listing_id or display 404
        listing = Listing.query.get_or_404(listing_id)
        # Delete the relevant listing
        db.session.delete(listing)
        db.session.commit()
        # Redirect to account template
        return redirect(url_for("account"))


# Search 
@app.route('/search', methods=['GET'])
def search():
    query = request.args.get('query')  
    results = Listing.query.filter(
        (Listing.title.ilike(f'%{query}%')) |
        (Listing.species.ilike(f'%{query}%')) |
        (Listing.tree_type.ilike(f'%{query}%')) |
        (Listing.indoor_outdoor.ilike(f'%{query}%')) |
        (Listing.description.ilike(f'%{query}%')) |
        (Listing.care_tips.ilike(f'%{query}%'))
    ).all()
    result_list = []
    for listing in results:
        result = {
            'id': listing.id,
            'title': listing.title,
            'price': listing.price
        }
        if listing.image:
            result['image'] = base64.b64encode(listing.image).decode('utf-8')
        else:
            result['image'] = None
        result_list.append(result)
    return jsonify(result_list)


# Save Item
@app.route("/save_item/<int:listing_id>", methods=["POST"])
@login_required
def save_item(listing_id):
    # Check if the item is already saved
    if SavedItem.query.filter_by(user_id=current_user.id, listing_id=listing_id).first():
        flash("Item is already saved", "info")
    else:
        # Save the item for the current user
        saved_item = SavedItem(user_id=current_user.id, listing_id=listing_id)
        db.session.add(saved_item)
        db.session.commit()
        flash("Item saved successfully", "success")
    return redirect(url_for("home")) 
    

# Get City 
@app.route('/get_city/<latitude>/<longitude>')
def get_city(latitude, longitude):
    # gets the api key from env.py
    api_key = os.getenv('LOCATIONIQ_API_KEY')
    # Sends a reuqest to the API with the coords
    response = requests.get(f'https://us1.locationiq.com/v1/reverse.php?key={api_key}&lat=${latitude}&lon=${longitude}&format=json')
    # Parses with JSON
    data = response.json()
    city = data.get('address', {}).get('city', 'City not found')
    # Returns the city as plain text
    return Response(city, mimetype='text/plain')



# Only for testing. Not needed in final version
# @app.route("/404")
# def errorpage():
#     return render_template("404.html")