import sys
import pathlib

# I really don't limke this hack
sys.path.insert(0, str(pathlib.Path(__file__).parent))

import os
import secrets
from PIL import Image
from flask import render_template, url_for, flash, redirect, request, abort, send_from_directory, jsonify
from flaskblog import app



@app.route("/")
@app.route("/home")
def home():
    return render_template('index_2.html')