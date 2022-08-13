import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_login import LoginManager
from flask_mail import Mail
import pathlib
import os


def get_root_path():
    return str(pathlib.Path(__file__).parent.parent.parent)


def get_template_folder():
    return os.path.join(get_root_path(), '_templates')

def get_static_folder():
    return os.path.join(get_root_path(), '_static')

app = Flask("client",
            template_folder=get_template_folder(),
            static_folder=get_static_folder(),
            instance_relative_config=True)
app.config['SECRET_KEY'] = '1111628bb0b13ce0c676dfde280ba245'
app.config['REMEMBER_COOKIE_PATH'] = '/hexagon'
file_path = os.path.dirname(os.path.abspath(__file__))
head = os.path.split(file_path)[0]
head = os.path.split(head)[0]
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + head + "/site.db"
db = SQLAlchemy(app)
bcrypt = Bcrypt(app)
login_manager = LoginManager(app)
login_manager.login_view = 'login'
login_manager.login_message_category = 'info'
app.config['MAIL_SERVER'] = 'smtp.googlemail.com'
app.config['MAIL_PORT'] = 587
app.config['MAIL_USE_TLS'] = True
app.config['MAIL_USERNAME'] = os.environ.get('EMAIL_USER')
app.config['MAIL_PASSWORD'] = os.environ.get('EMAIL_PASS')
mail = Mail(app)

from flaskblog import routes
