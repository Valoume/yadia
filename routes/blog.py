from flask import Blueprint, render_template, abort
from models.blog import BlogPost
from sqlalchemy import desc

blog = Blueprint('blog', __name__)

@blog.route('/blog')
def blog_index():
    """Page principale du blog avec liste des articles"""
    posts = BlogPost.query.order_by(desc(BlogPost.created_at)).all()
    # Grouper les articles par secteur
    posts_by_sector = {}
    for post in posts:
        if post.sector not in posts_by_sector:
            posts_by_sector[post.sector] = []
        posts_by_sector[post.sector].append(post)
    
    return render_template('blog/index.html', posts_by_sector=posts_by_sector)

@blog.route('/blog/<string:slug>')
def blog_post(slug):
    """Page d'un article individuel"""
    post = BlogPost.query.filter_by(slug=slug).first_or_404()
    # Trouver des articles reliés dans le même secteur
    related_posts = BlogPost.query.filter(
        BlogPost.sector == post.sector,
        BlogPost.id != post.id
    ).limit(3).all()
    
    return render_template('blog/post.html', post=post, related_posts=related_posts)
