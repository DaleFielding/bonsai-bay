from bonsai_bay import db

# table schemas:

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(25), unique=True, nullable=False)
    email = db.Column(db.String(100), unique=True, nullable=False)
    password_hashed = db.Column(db.String(25), nullable=False)
    location = db.Column(db.String(100), nullable=True)
    saved_item_id = db.Column(db.Integer, db.ForeignKey("saved_item.id", ondelete="CASCADE"), nullable=True)

    def __repr__(self):
        return self.username

class Tree(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    species = db.Column(db.String(50), nullable=True)
    tree_type = db.Column(db.String(25), nullable=True)
    indoor_outdoor = db.Column(db.String(7), nullable=True)
    description = db.Column(db.Text, nullable=True)
    height = db.Column(db.Numeric(precision=5), nullable=True) 
    price = db.Column(db.Numeric(precision=10, scale=2), nullable=True)
    care_tips = db.Column(db.String(200), nullable=True)
    image = db.Column(db.LargeBinary, nullable=True)
    date_added = db.Column(db.Date, nullable=True)
    seller_id = db.Column(db.Integer, db.ForeignKey("seller.id", ondelete="CASCADE"), nullable=True)
    seller = db.relationship("Seller", backref="trees") 

class Seller(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey("user.id", ondelete="CASCADE"), nullable=True)
    user = db.relationship("User", backref="seller") 

class SavedItem(db.Model): 
    id = db.Column(db.Integer, primary_key=True)
    tree_id = db.Column(db.Integer, db.ForeignKey("tree.id", ondelete="CASCADE"), nullable=True)
    user_id = db.Column(db.Integer, db.ForeignKey("user.id", ondelete="CASCADE"), nullable=True)
