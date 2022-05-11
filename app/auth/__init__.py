# -*- coding: utf-8 -*-
"""
Created on Tue Apr 19 21:47:46 2022

@author: salsa
"""

from flask import Blueprint, render_template, abort, request, redirect, url_for, flash
from flask_login import logout_user, login_user, login_required
from jinja2 import TemplateNotFound
from app.auth.forms import RegisterForm, LoginForm
from app.db import db
from app.db.models import User

auth = Blueprint('auth', __name__,
                         template_folder='templates')


@auth.route('/register', methods=['GET', 'POST'])
def register():
    form = RegisterForm(request.form)
    try:
        if request.method == 'POST':
            user = User(form.email.data, form.password.data)
            db.session.add(user)
            db.session.commit()
            flash('User Registered', 'success')
            return redirect(url_for('auth.login'))
        return render_template('register.html', form=form)
    except:
        abort(404)


@auth.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm(request.form)

    # login_user(user)
    flash('Logined in' 'success')


    """
    try:
        return render_template('login.html')
    except:
        abort(404)
    """

@auth.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('auth.login'))