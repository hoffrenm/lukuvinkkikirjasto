import os
from flask import Flask, render_template, send_from_directory
from . import main # tämä on blueprint ks https://flask.palletsprojects.com/en/1.1.x/blueprints/

@main.route('/', defaults={'path': ''})
@main.route('/<path:path>')
def index(path):
   return render_template('index.html')