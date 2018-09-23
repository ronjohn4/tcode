from flask import Flask
from flask_menu import Menu
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager

from config import Config

# # mandatory
# CODEMIRROR_LANGUAGES = ['python', 'html']
# # optional
# CODEMIRROR_THEME = '3024-day'
# # CODEMIRROR_ADDONS = (
# #             ('ADDON_DIR','ADDON_NAME'),


app = Flask(__name__)
login = LoginManager(app)
login.login_view = 'login'
app.config.from_object(Config)

Menu(app=app)
# db = DB('tcode.db')

db = SQLAlchemy(app)
migrate = Migrate(app, db)

from app import routes, models
