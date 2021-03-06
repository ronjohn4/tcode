from datetime import datetime

from flask import render_template, flash, redirect, url_for, request
from flask_login import current_user, login_user, logout_user, login_required
from werkzeug.urls import url_parse

from app import app, db
from app.models import User, Snippet
from app.forms import LoginForm, RegistrationForm, EditProfileForm, EditSnippetForm


@app.route('/index', methods=['GET', 'POST'])
@app.route('/', methods=['GET', 'POST'])
def index():

    if current_user.is_authenticated:
        snippets = [
            {'id': 1, 'snippetname': 'Snippet 1', 'snippet': '', 'timestamp':'', 'user': 'Ron J'},
            {'id': 2, 'snippetname': 'Code Gode', 'snippet': '', 'timestamp': '', 'user': 'Ron J'},
            {'id': 3, 'snippetname': 'Something happened here', 'snippet': '', 'timestamp': '', 'user': 'Ron J'}
        ]
    else:
        snippets = []

    return render_template('index.html', snippets=snippets)


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
@app.route('/profile/<username>')
@app.route('/profile/')
@app.route('/profile')
@login_required
def profile(username):
    user = User.query.filter_by(username=username).first_or_404()
    snippets = [
        {'name': 'Snippet 1', 'snippet': '', 'timestamp':'', 'user': 'Ron J'},
        {'name': 'Code Gode', 'snippet': '', 'timestamp': '', 'user': 'Ron J'},
        {'name': 'Something happened here', 'snippet': '', 'timestamp': '', 'user': 'Ron J'}
    ]
    return render_template('profile.html', user=user, snippets=snippets)


@app.route('/snippet/<id>')
@app.route('/snippet/')
@app.route('/snippet')
@login_required
def snippet(id):
    snippet = Snippet.query.filter_by(id=id).first_or_404()
    return render_template('snippet.html', snippet=snippet)


@app.route('/add_snippet', methods=['GET', 'POST'])
def add_snippet():
    form = EditSnippetForm()
    if form.validate_on_submit():
        snippet = Snippet(snippetname=form.snippetname.data, snippet=form.snippet.data, use_count=0)
        db.session.add(snippet)
        db.session.commit()
        flash('Snippet added')
        return redirect(url_for('index'))
    return render_template('snippet.html', title='Add Snippet', form=form)


@app.before_request
def before_request():
    if current_user.is_authenticated:
        current_user.last_seen = datetime.utcnow()
        db.session.commit()


@app.route('/edit_profile', methods=['GET', 'POST'])
@login_required
def edit_profile():
    form = EditProfileForm(current_user.username)
    if form.validate_on_submit():
        current_user.username = form.username.data
        db.session.commit()
        flash('Your changes have been saved.')
        return redirect(url_for('edit_profile'))
    elif request.method == 'GET':
        form.username.data = current_user.username
    return render_template('edit_profile.html', title='Edit Profile', form=form)