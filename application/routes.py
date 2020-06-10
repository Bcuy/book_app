from flask import session, render_template, flash, redirect, url_for
from application.forms import RegistrationForm, LoginForm
from application.models import User, Review
from application import app, db, bcrypt

@app.route("/")
@app.route("/home")
def home():
    return render_template('home.html')

@app.route("/finder")
def finder():
    return render_template('finder.html')

@app.route("/register", methods=['GET', 'POST'])
def register():
    form = RegistrationForm()
    if form.validate_on_submit():
        hashed_password = bcrypt.generate_password_hash(form.password.data).decode('utf-8')
        user = User(username=form.username.data, email=form.email.data, password=hashed_password)
        db.session.add(user)
        db.session.commit()
        flash(f'Account created for {form.username.data}. You can now login.', 'success')
        return redirect(url_for('login'))
    return render_template('register.html', form=form)

@app.route("/login", methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        if form.email.data == 'bcuy@usc.edu' and form.password.data == 'password':
            flash('You have been logged in', 'success')
            return redirect(url_for('home'))
        else:
            flash('Login unsuccessful. Please check email and password', 'danger')
    return render_template('login.html', form=form)
