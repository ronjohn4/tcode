# import logging
# from logging.handlers import SMTPHandler
# from logging.handlers import RotatingFileHandler
# import os

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
db = SQLAlchemy(app)
migrate = Migrate(app, db)


# Run in a terminal window to start the python email catcher
# python -m smtpd -n -c DebuggingServer localhost:8025
#
# log to email
# if not app.debug:
#     if app.config['MAIL_SERVER']:
#         auth = None
#         if app.config['MAIL_USERNAME'] or app.config['MAIL_PASSWORD']:
#             auth = (app.config['MAIL_USERNAME'], app.config['MAIL_PASSWORD'])
#         secure = None
#         if app.config['MAIL_USE_TLS']:
#             secure = ()
#         mail_handler = SMTPHandler(
#             mailhost=(app.config['MAIL_SERVER'], app.config['MAIL_PORT']),
#             fromaddr='no-reply@' + app.config['MAIL_SERVER'],
#             toaddrs=app.config['ADMINS'], subject='Microblog Failure',
#             credentials=auth, secure=secure)
#         mail_handler.setLevel(logging.ERROR)
#         app.logger.addHandler(mail_handler)


# Log to a rotating file
# if not app.debug:
#     if not os.path.exists('logs'):
#         os.mkdir('logs')
#     file_handler = RotatingFileHandler('logs/tcode.log', maxBytes=10240, backupCount=10)
#     file_handler.setFormatter(logging.Formatter('%(asctime)s %(levelname)s: %(message)s [in %(pathname)s:%(lineno)d]'))
#     file_handler.setLevel(logging.INFO)
#     app.logger.addHandler(file_handler)
#     app.logger.setLevel(logging.INFO)
#     app.logger.info('TCode startup')


from app import routes, models, errors
