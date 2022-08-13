import sys
import pathlib

# I really don't limke this hack
sys.path.insert(0, str(pathlib.Path(__file__).parent))
sys.path.insert(0, str(pathlib.Path(__file__).parent) + '/Build')

import os
import secrets
from PIL import Image
from flask import render_template, url_for, flash, redirect, request, abort, send_from_directory, jsonify, send_file
from flaskblog import app



@app.route("/")
@app.route("/home")
def home():
    return render_template('index.html')

from flask import send_from_directory

@app.route('/<path:path>')
def send_report(path):
    print("HELLO!")
    print(send_file(str(pathlib.Path(__file__).parent), path))
    return send_file(str(pathlib.Path(__file__).parent), path)