from bonsai_bay import db
from werkzeug.security import generate_password_hash, check_password_hash
from sqlalchemy.orm import relationship
from flask_login import UserMixin

# table schemas:

class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(25), unique=True, nullable=False)
    email = db.Column(db.String(100), unique=True, nullable=False)
    password_hash = db.Column(db.String(256))
    location = db.Column(db.String(100), nullable=False)
    saved_items = relationship('SavedItem', backref='user', lazy=True)

    @property
    def password(self):
        raise AttributeError('password is not a readable attribute.')

    @password.setter
    def password(self, password):
        # Generate password hash from the padssword
        self.password_hash = generate_password_hash(password)

    def verify_password(self, password):
        return check_password_hash(self.password_hash, password)

    def __repr__(self):
        return '<Name %r>' % self.username

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
    user_id = db.Column(db.Integer, db.ForeignKey("user.id", ondelete="CASCADE"), nullable=False)

class SavedItem(db.Model): 
    id = db.Column(db.Integer, primary_key=True)
    listing_id = db.Column(db.Integer, db.ForeignKey("listing.id", ondelete="CASCADE"), nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey("user.id", ondelete="CASCADE"), nullable=False)
