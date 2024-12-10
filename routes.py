from flask import render_template, request, redirect, url_for, flash
from app import app, db
from models import BlogPost, Contact, Appointment
from datetime import datetime

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

@app.route('/contact', methods=['GET', 'POST'])
def contact():
    if request.method == 'POST':
        contact = Contact(
            name=request.form['name'],
            email=request.form['email'],
            message=request.form['message']
        )
        db.session.add(contact)
        db.session.commit()
        flash('Thank you for your message! We will get back to you soon.')
        return redirect(url_for('contact'))
    return render_template('contact.html')

@app.route('/blog')
def blog():
    posts = BlogPost.query.order_by(BlogPost.created_at.desc()).all()
    return render_template('blog.html', posts=posts)

@app.route('/formulaire')
def formulaire():
    return render_template('formulaire.html')
@app.route('/ebook')
def ebook():
    return render_template('ebook.html')


@app.route('/book-appointment', methods=['POST'])
def book_appointment():
    if request.method == 'POST':
        appointment = Appointment(
            name=request.form['name'],
            email=request.form['email'],
            date=datetime.strptime(request.form['date'], '%Y-%m-%d'),
            service_type=request.form['service_type'],
            notes=request.form['notes']
        )
        db.session.add(appointment)
        db.session.commit()
        flash('Appointment booked successfully!')
        return redirect(url_for('index'))
