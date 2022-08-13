import sys
import pathlib

# I really don't limke this hack
sys.path.insert(0, str(pathlib.Path(__file__).parent))
sys.path.insert(0, str(pathlib.Path(__file__).parent) + '/Build')

import os
import secrets
from PIL import Image
from flask import render_template, url_for, flash, redirect, request, abort, send_from_directory, jsonify
from flaskblog import app



@app.route("/")
@app.route("/home")
def home():
    return render_template('index.html')

from flask import send_from_directory

@app.route('/<path:path>')
def send_report(path):
    print("HELLO!")
    print(path)
    print(send_from_directory(str(pathlib.Path(__file__).parent), path))
    return send_from_directory(str(pathlib.Path(__file__).parent), path)