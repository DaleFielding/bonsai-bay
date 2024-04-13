from bonsai_bay import db

# table schemas:

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(25), unique=True, nullable=False)
    email = db.Column(db.String(100), unique=True, nullable=False)
    password_hashed = db.Column(db.String(25), nullable=False)
    location = db.Column(db.String(100), nullable=False)
    saved_item_id = db.Column(db.Integer, db.ForeignKey("saved_item.id", ondelete="CASCADE"), nullable=False)

    def __repr__(self):
        return self.username

class Listing(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(25), nullable=False)
    species = db.Column(db.String(50), nullable=False)
    tree_type = db.Column(db.String(25), nullable=False)
    indoor_outdoor = db.Column(db.String(7), nullable=False)
    description = db.Column(db.Text, nullable=False)
    height = db.Column(db.Numeric(precision=5), nullable=False) 
    price = db.Column(db.Numeric(precision=10, scale=2), nullable=False)
    care_tips = db.Column(db.String(200), nullable=False)
    image = db.Column(db.LargeBinary, nullable=False)
    date_added = db.Column(db.Date, nullable=False)
    seller_id = db.Column(db.Integer, db.ForeignKey("seller.id", ondelete="CASCADE"), nullable=False)
    seller = db.relationship("Seller", backref="listings") 

class Seller(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey("user.id", ondelete="CASCADE"), nullable=False)
    user = db.relationship("User", backref="seller") 

class SavedItem(db.Model): 
    id = db.Column(db.Integer, primary_key=True)
    listing_id = db.Column(db.Integer, db.ForeignKey("listing.id", ondelete="CASCADE"), nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey("user.id", ondelete="CASCADE"), nullable=False)
