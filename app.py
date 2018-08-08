from flask import Flask, render_template
from flask_menu import Menu, register_menu


app = Flask(__name__)
Menu(app=app)


@app.route('/home')
@app.route('/')
@register_menu(app, 'home', 'Home', order=0)
def home():
    return render_template('home.html')


@app.route('/track')
@register_menu(app, 'track', 'Tracking', order=1)
def track():
    return render_template('track.html')


@app.route('/account')
@register_menu(app, 'account', 'My Account', order=2)
def account():
    return render_template('account.html')


if __name__ == '__main__':
    app.run(debug=True)
