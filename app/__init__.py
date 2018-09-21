from flask import Flask
from config import Config
from flask_menu import Menu

# # mandatory
# CODEMIRROR_LANGUAGES = ['python', 'html']
# # optional
# CODEMIRROR_THEME = '3024-day'
# # CODEMIRROR_ADDONS = (
# #             ('ADDON_DIR','ADDON_NAME'),


app = Flask(__name__)
app.config.from_object(Config)

Menu(app=app)
# db = DB('tcode.db')

from app import routes
