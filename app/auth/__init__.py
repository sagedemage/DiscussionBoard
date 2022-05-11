"""
Authentication pages
"""

from flask import Blueprint, render_template, redirect, url_for, flash
from flask_login import login_user, login_required, logout_user, current_user
from werkzeug.security import generate_password_hash

from app.auth.decorators import admin_required
from app.auth.forms import register_form, login_form
from app.db import db
from app.db.models import User

auth = Blueprint('auth', __name__, template_folder='templates')

from flask import current_app


@auth.route('/register', methods=['POST', 'GET'])
def register():
    """ Register the user """
    if current_user.is_authenticated:
        return redirect(url_for('auth.dashboard'))
    form = register_form()
    if form.validate_on_submit():
        user = User.query.filter_by(email=form.email.data).first()
        if user is None:
            user = User(email=form.email.data, password=generate_password_hash(password=form.password.data))
            db.session.add(user)
            db.session.commit()
            if user.id == 1:
                user.is_admin = 1
                db.session.add(user)
                db.session.commit()
            flash('Congratulations, you are a registered user', "success")
            return redirect(url_for('auth.login'), 302)
        else:
            flash('Already Registered')
            return redirect(url_for('auth.login'), 302)
    return render_template('register.html', form=form)


@auth.route('/login', methods=['GET', 'POST'])
def login():
    """ Logged in the user """
    form = login_form()
    if current_user.is_authenticated:
        return redirect(url_for('auth.dashboard'))
    # flash(form.errors)
    if form.validate_on_submit():
        user = User.query.filter_by(email=form.email.data).first()
        if user is None or not user.check_password(form.password.data):
            flash('Invalid email or password', 'error')
            return redirect(url_for('auth.login'))
        else:
            user.authenticated = True
            db.session.add(user)
            db.session.commit()
            login_user(user)
            flash("Welcome to the dashboard", 'success')
            return redirect(url_for('auth.dashboard'))
    return render_template('login.html', form=form)


@auth.route('/logout')
@login_required
def logout():
    """ Logout the current user """
    user = current_user
    user.authenticated = False
    db.session.add(user)
    db.session.commit()
    logout_user()
    return redirect(url_for('auth.login'))


@auth.route('/dashboard')
@login_required
def dashboard():
    """ Dashboard page """
    return render_template('dashboard.html')

"""
@auth.route('/profile')
@login_required
def edit_profile():
    return render_template('profile_edit.html')


@auth.route('/account')
@login_required
def edit_account():
    return render_template('manage_account.html')
"""

