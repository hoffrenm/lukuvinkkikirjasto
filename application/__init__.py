#Flaskin käyttöönotto
import os
from flask import Flask, render_template, send_from_directory
app = Flask(__name__, static_folder="../build/static", template_folder="../build")

#SQLAlchemyn käyttöönotto
from flask_sqlalchemy import SQLAlchemy

# otetaan käyttöön "tips" niminen tietokanta
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///tips.db"

# pyydetään SQL-Alchemya tekemään kaikki sql-kyselyt
app.config["SQLALCHEMY_ECHO"] = True

# kutsutaan db:tä

db = SQLAlchemy(app)

# apille menevät kutsut tulee importata ennen viimeistä routea, 
# joka lähettää reactin koodin selaimelle
from application.tips import models, views

#taulujen luonti
db.create_all()

@app.route('/', defaults={'path': ''})
@app.route('/<path:path>')
def index(path):
    return render_template('index.html')
