import os
import logging
from flask import Flask, session
from flask_sqlalchemy import SQLAlchemy
from flask_session import Session
from sqlalchemy.orm import DeclarativeBase
from datetime import timedelta

logging.basicConfig(level=logging.DEBUG)

class Base(DeclarativeBase):
    pass

db = SQLAlchemy(model_class=Base)
app = Flask(__name__, static_url_path='/static', static_folder='static')

# Configuration
app.secret_key = os.environ.get("FLASK_SECRET_KEY") or "yadia_secret_key_2024"
app.config["SQLALCHEMY_DATABASE_URI"] = os.environ.get("DATABASE_URL") or "sqlite:///yadia.db"
app.config["SQLALCHEMY_ENGINE_OPTIONS"] = {
    "pool_recycle": 300,
    "pool_pre_ping": True,
}
app.config["SESSION_TYPE"] = "filesystem"
app.config["PERMANENT_SESSION_LIFETIME"] = timedelta(minutes=30)
app.config["SESSION_FILE_DIR"] = "./.flask_session/"

# Ensure the session directory exists
os.makedirs(app.config["SESSION_FILE_DIR"], exist_ok=True)

# Initialize Flask-Session
Session(app)

db.init_app(app)

with app.app_context():
    import models
    import routes
    db.create_all()
