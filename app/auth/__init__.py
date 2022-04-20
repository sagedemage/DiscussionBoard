# -*- coding: utf-8 -*-
"""
Created on Tue Apr 19 21:47:46 2022

@author: salsa
"""

from flask import Blueprint, render_template, abort
from jinja2 import TemplateNotFound

auth = Blueprint('auth', __name__,
                         template_folder='templates')

@auth.route('/register')
def register():
    try:
        return render_template('register.html')
    except:
        abort(404)
@auth.route('/login')
def login():
    try:
        return render_template('login.html')
    except:
        abort(404)