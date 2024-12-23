from datetime import datetime
from models import db

class BlogPost(db.Model):
    __tablename__ = 'blog_posts'
    
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(200), nullable=False)
    slug = db.Column(db.String(200), unique=True, nullable=False)
    content = db.Column(db.Text, nullable=False)
    sector = db.Column(db.String(50), nullable=False)
    meta_description = db.Column(db.String(500), nullable=False)
    keywords = db.Column(db.String(500))
    created_at = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    updated_at = db.Column(db.DateTime, nullable=False, default=datetime.utcnow, onupdate=datetime.utcnow)
    reading_time = db.Column(db.Integer)  # in minutes
    featured_image = db.Column(db.String(500))
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if not self.reading_time and self.content:
            # Estimate reading time (about 200 words per minute)
            words = len(self.content.split())
            self.reading_time = max(1, round(words / 200))
