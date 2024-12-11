from flask import render_template, request, redirect, url_for, flash, session
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

from ai_audit import generate_ai_audit_report
from firebase_admin import firestore
from firebase_config import save_form_data, initialize_firebase

# Initialize Firebase
firebase_db = initialize_firebase()

@app.route('/formulaire', methods=['GET', 'POST'])
def formulaire():
    if request.method == 'POST':
        current_time = datetime.utcnow()
        form_data = {
            'industry': request.form.get('industry'),
            'current_tech': request.form.getlist('tech'),
            'challenges': request.form.get('challenges'),
            'goals': request.form.getlist('goals'),
            'company_name': request.form.get('company-name'),
            'contact_name': request.form.get('contact-name'),
            'contact_email': request.form.get('contact-email'),
            'timestamp': firestore.SERVER_TIMESTAMP if firebase_db else current_time
        }
        
        # Generate AI recommendations
        audit_report = generate_ai_audit_report(form_data)
        
        # Store in Firebase
        success, result = save_form_data('form_submissions', {
            **form_data,
            'audit_report': audit_report
        })
        
        if success:
            # Store in session for display
            session['audit_report'] = audit_report
            session['form_data'] = form_data
            flash('Formulaire soumis avec succès!', 'success')
            return redirect(url_for('audit_results'))
        else:
            flash('Erreur lors de la soumission du formulaire. Veuillez réessayer.', 'error')
            return redirect(url_for('formulaire'))
        
    return render_template('formulaire.html')

@app.route('/audit-results')
def audit_results():
    if 'audit_report' not in session:
        return redirect(url_for('formulaire'))
        
    return render_template('audit_results.html',
                         report=session.get('audit_report'),
                         form_data=session.get('form_data'))
@app.route('/ebook', methods=['GET', 'POST'])
def ebook():
    if request.method == 'POST':
        name = request.form.get('name')
        email = request.form.get('email')
        flash('Merci pour votre achat! Vous recevrez votre e-book par email.')
        return redirect(url_for('ebook'))
    return render_template('ebook.html', title="E-book - Yadia AI Solutions")


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
