import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
from flask_compress import Compress

# env imported if the os can find an existing filepath for the env.py file
if os.path.exists("env.py"):
    import env

# Create instance of the imported flask class, store in a variable called app
app = Flask(__name__)
app.config["SECRET_KEY"] = os.environ.get("SECRET_KEY")

if os.environ.get("DEVELOPMENT") == "True":
    app.config["SQLALCHEMY_DATABASE_URI"] = os.environ.get("DB_URL")
else:
    uri = os.environ.get("DATABASE_URL")
    if uri.startswith("postgres://"):
        uri = uri.replace("postgres://", "postgresql://", 1)
    app.config["SQLALCHEMY_DATABASE_URI"] = uri

db = SQLAlchemy(app)
login_manager = LoginManager(app)


# The below loads a user from the database from their ID.
@login_manager.user_loader
def load_user(user_id):
    from bonsai_bay.models import User
    return User.query.get(int(user_id))


# Only seems to work if placed here and not at the top of the file
from bonsai_bay import routes
