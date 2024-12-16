import os
import logging
from datetime import timedelta
from flask import Flask, render_template, request, jsonify, session
from flask_session import Session

# Configure logging
logging.basicConfig(level=logging.DEBUG)

# Initialize Flask app
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

with app.app_context():
    from models import db
    db.init_app(app)
    # Create database tables
    db.create_all()
    # Register blueprints after database initialization
    from routes.blog import blog
    app.register_blueprint(blog)
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