from flask import render_template, flash, redirect, url_for, request
from flask_login import current_user, login_user, logout_user, login_required
from werkzeug.urls import url_parse

from app import app, db
from app.models import User
from app.forms import LoginForm, ShirtForm, RegistrationForm


@app.route('/index', methods=['GET', 'POST'])
@app.route('/', methods=['GET', 'POST'])
def index():
    form = ShirtForm()
    form.shirt = 'form1 shirt'

    if form.validate_on_submit():
        flash('Save shirt')

    if current_user.is_authenticated:
        snippets = [
            {'name': 'Snippet 1', 'snippet': '', 'timestamp':'', 'user': 'Ron J'},
            {'name': 'Code Gode', 'snippet': '', 'timestamp': '', 'user': 'Ron J'},
            {'name': 'Something happened here', 'snippet': '', 'timestamp': '', 'user': 'Ron J'}
        ]
    else:
        snippets = []

    return render_template('index.html', form=form, snippets=snippets)


@app.route('/login', methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('index'))
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(username=form.username.data).first()
        if user is None or not user.check_password(form.password.data):
            flash('Invalid username or password')
            return redirect(url_for('login'))
        login_user(user, remember=form.remember_me.data)
        next_page = request.args.get('next')
        print('next_page:', next_page)
        if not next_page or url_parse(next_page).netloc != '':
            next_page = url_for('index')
        return redirect(next_page)
    return render_template('login.html', title='Sign In', form=form)


@app.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('index'))


@app.route('/register', methods=['GET', 'POST'])
def register():
    if current_user.is_authenticated:
        return redirect(url_for('index'))
    form = RegistrationForm()
    if form.validate_on_submit():
        user = User(username=form.username.data, email=form.email.data)
        user.set_password(form.password.data)
        db.session.add(user)
        db.session.commit()
        flash('Congratulations, you are now a registered user!')
        return redirect(url_for('login'))
    return render_template('register.html', title='Register', form=form)


# ToDo - reroute from authentication doesn't pass in username
@app.route('/user/<username>')
@app.route('/user/')
@app.route('/user')
@login_required
def user(username):
    user = User.query.filter_by(username=username).first_or_404()
    snippets = [
        {'name': 'Snippet 1', 'snippet': '', 'timestamp':'', 'user': 'Ron J'},
        {'name': 'Code Gode', 'snippet': '', 'timestamp': '', 'user': 'Ron J'},
        {'name': 'Something happened here', 'snippet': '', 'timestamp': '', 'user': 'Ron J'}
    ]

    return render_template('user.html', user=user, snippets=snippets)
