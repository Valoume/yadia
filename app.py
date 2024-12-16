import os
import logging
from datetime import timedelta
from flask import Flask, render_template, request, jsonify, session, redirect, url_for
from flask_session import Session
from flask_migrate import Migrate
from models import db

# Configure logging
logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger(__name__)

app = Flask(__name__)

# Configure app
app.config.update(
    SECRET_KEY=os.urandom(24),
    SESSION_TYPE='filesystem',
    SQLALCHEMY_DATABASE_URI=os.environ.get('DATABASE_URL'),
    SQLALCHEMY_TRACK_MODIFICATIONS=False,
    PERMANENT_SESSION_LIFETIME=timedelta(minutes=30)
)

# Initialize Flask-Session
Session(app)

# Initialize database and migrations
db.init_app(app)
migrate = Migrate(app, db)

# Register blueprints
from routes.blog import blog
app.register_blueprint(blog)
from ai_audit import generate_ai_audit_report

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/services')
def services():
    return render_template('services.html')

@app.route('/faq')
def faq():
    return render_template('faq.html')

@app.route('/formulaire')
def formulaire():
    return render_template('formulaire.html')

@app.route('/contact')
def contact():
    return render_template('contact.html')

@app.route('/blog')
def blog():
    return redirect(url_for('blog.blog_index'))

@app.route('/ebook')
def ebook():
    return render_template('ebook.html')

@app.route('/generate_audit', methods=['POST'])
def generate_audit():
    try:
        form_data = request.get_json()
        result = generate_ai_audit_report(form_data)
        return jsonify(result)
    except Exception as e:
        app.logger.error(f"Error generating audit: {str(e)}")
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    with app.app_context():
        try:
            db.create_all()
            app.logger.info("Database tables created successfully")
        except Exception as e:
            app.logger.error(f"Error creating database tables: {str(e)}")
    
    app.run(host='0.0.0.0', port=5000, debug=True)
