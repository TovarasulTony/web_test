import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_login import LoginManager
from flask_mail import Mail
import pathlib
import sys
import os


def get_root_path():
    return str(pathlib.Path(__file__).parent)


def get_template_folder():
	return_path = str(pathlib.Path(__file__).parent)
	#return_path+='/TemplateData'
	print(return_path)
	return return_path

def get_static_folder():
    return str(pathlib.Path(__file__).parent)

app = Flask("client",
            template_folder=get_template_folder(),
            static_folder=get_static_folder(),
            instance_relative_config=True)
app.config['SECRET_KEY'] = '1111628bb0b13ce0c676dfde280ba245'
app.config['REMEMBER_COOKIE_PATH'] = '/hexagon'



from flaskblog import routes
