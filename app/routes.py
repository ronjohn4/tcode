from app import app
from flask_menu import Menu, register_menu
from app.forms import LoginForm, ShirtForm
from flask import render_template, flash, redirect, url_for


@app.route('/home', methods=['GET', 'POST'])
@app.route('/', methods=['GET', 'POST'])
@register_menu(app, 'home', 'Home', order=0)
def home():
    form = ShirtForm()
    form.shirt = 'form1 shirt'

    if form.validate_on_submit():
        flash('Save shirt')

    return render_template('home.html', form=form)


@app.route('/login', methods=['GET', 'POST'])
@register_menu(app, 'login', 'Login', order=3)
def login():
    form = LoginForm()

    if form.validate_on_submit():
        flash('Login requested for user {}, remember_me={}'.format(
            form.username.data, form.remember_me.data))
        return redirect('/home')

    return render_template('login.html', form=form)


@app.route('/track', methods=['GET'])
@register_menu(app, 'track', 'Tracking', order=1)
def track_get():
    text = "not defined"
    return render_template('track.html', SubmittedValue=text)


@app.route('/track', methods=['POST'])
@register_menu(app, 'track', 'Tracking', order=1)
def track():
    text = 'not defined'
    return render_template('track.html', SubmittedValue=text)


@app.route('/account')
@register_menu(app, 'account', 'My Account', order=2)
def account():
    return render_template('account.html')
