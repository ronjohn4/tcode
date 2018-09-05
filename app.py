from flask import Flask, render_template, request
from flask_menu import Menu, register_menu
# from flask.ext.codemirror import CodeMirror

# mandatory
CODEMIRROR_LANGUAGES = ['python', 'html']
# optional
CODEMIRROR_THEME = '3024-day'
# CODEMIRROR_ADDONS = (
#             ('ADDON_DIR','ADDON_NAME'),


app = Flask(__name__)
Menu(app=app)


@app.route('/home')
@app.route('/')
@register_menu(app, 'home', 'Home', order=0)
def home():
    return render_template('home.html')


@app.route('/track', methods=['GET'])
@register_menu(app, 'track', 'Tracking', order=1)
def track_get():
    text = "not defined"
    return render_template('track.html', SubmittedValue=text)


@app.route('/track', methods=['POST'])
@register_menu(app, 'track', 'Tracking', order=1)
def track():
    text = request.form['text']
    return render_template('track.html', SubmittedValue=text)


@app.route('/account')
@register_menu(app, 'account', 'My Account', order=2)
def account():
    return render_template('account.html')


if __name__ == '__main__':
    app.run(debug=True)
