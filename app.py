import os
import logging
from datetime import timedelta
from flask import Flask, render_template, request, jsonify, session
from flask_sqlalchemy import SQLAlchemy
from flask_session import Session
from sqlalchemy.orm import DeclarativeBase

# Configure logging
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
from ai_audit import generate_ai_audit_report

@app.route('/generate_audit', methods=['POST'])
def generate_audit():
    try:
        form_data = request.get_json()
        result = generate_ai_audit_report(form_data)
        return jsonify(result)
    except Exception as e:
        app.logger.error(f"Error generating audit: {str(e)}")
        return jsonify({"error": str(e)}), 500
    db.create_all()
