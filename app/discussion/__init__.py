from flask import Blueprint, render_template, abort, url_for, current_app, flash
from flask_login import current_user, login_required
from app.auth.decorators import admin_required
from jinja2 import TemplateNotFound

from app.db import db
from app.db.models import Posts
from app.discussion.forms import add_post_form, edit_post_form
from werkzeug.utils import secure_filename, redirect

discussion = Blueprint('discussion', __name__,
                  template_folder='templates')


@discussion.route('/discussions', methods=['GET'])
@login_required
def browse_posts():
    data = Posts.query.all()
    edit_url = ('discussion.edit_post', [('post_id', ':id')])
    # add_url = url_for('discussion.add_post')
    delete_url = ('discussion.delete_post', [('post_id', ':id')])
    try:
        return render_template('browse_posts.html', data=data, edit_url=edit_url,
                               delete_url=delete_url, Posts=Posts, record_style="Posts")
    except TemplateNotFound:
        abort(404)


@discussion.route('/discussions/new', methods=['GET', 'POST'])
@login_required
def add_post():
    form = add_post_form()
    if form.validate_on_submit():
        post = Posts(title=form.title.data, description=form.description.data)
        db.session.add(post)
        current_user.posts.append(post)
        db.session.commit()
        flash('Congratulations, you added a post', 'success')
        return redirect(url_for('discussion.browse_posts'))
    return render_template('new_post.html', form=form)


@discussion.route('/discussions/<int:post_id>/edit', methods=['POST', 'GET'])
@login_required
def edit_post(post_id):
    post = Posts.query.get(post_id)
    form = edit_post_form(obj=post)
    if form.validate_on_submit():
        post.title = form.title.data
        post.description = form.description.data
        db.session.add(post)
        db.session.commit()
        flash('Post edited successfully', 'success')
        current_app.logger.info("edited post")
        return redirect(url_for('discussion.browse_posts'))
    return render_template('edit_post.html', form=form)


@discussion.route('/discussions/<int:post_id>/delete', methods=['POST'])
@login_required
def delete_post(post_id):
    post = Posts.query.get(post_id)
    db.session.delete(post)
    db.session.commit()
    flash('Post deleted', 'success')
    return redirect(url_for('discussion.browse_posts'), 302)







