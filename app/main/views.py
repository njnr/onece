# coding: utf-8

from flask import render_template, session, redirect, url_for, current_app
from .. import db
from ..models import User, Permission
from ..email import send_email
from . import main
from .forms import NameForm
from ..decorators import admin_required, permission_required
from flask.ext.login import login_required


@main.route('/', methods=['GET', 'POST'])
def index():
    form = NameForm()
    if form.validate_on_submit():
        user = User.query.filter_by(username=form.name.data).first()
        if user is None:
            user = User(username=form.name.data)
            db.session.add(user)
            session['known'] = False
            """
            if current_app.config['FLASKY_ADMIN']:
               send_email(current_app.config['FLASK_ADMIN'], 'New User',
                           'mail/new_user', user=user) """
        else:
            session['known'] = True
        session['name'] = form.name.data
        return redirect(url_for('.index'))
    return render_template('index.html',
                           form=form, name=session.get('name'),
                           known=session.get('known', False))

@main.route('/user/<username>')
def user(username):
    user = User.query.filter_by(username=username).first_or_404()
    return render_template('user.html', user = user)

@main.route('/read')
def read():
    return "这是我女儿11天的时候拍的照片，小脚丫超级可爱呀！"



@main.route('/admin')
@login_required
@admin_required
def for_admins_only():
    return "for administrators!"

@main.route('/moderator')
@login_required
@permission_required(Permission.MODERATE_COMMENTS)
def for_moderators_only():
    return "for comment moderators!"
