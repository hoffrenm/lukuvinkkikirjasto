#Flaskin käyttöönotto
from flask import Flask
app = Flask(__name__)

#SQLAlchemyn käyttöönotto
from flask_sqlalchemy import SQLAlchemy

# otetaan käyttöön "tips" niminen tietokanta
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///tips.db"

# pyydetään SQL-Alchemya tekemään kaikki sql-kyselyt
app.config["SQLALCHEMY_ECHO"] = True

# kutsutaan db:tä

db = SQLAlchemy(app)

# roudataan kamaa sovelluksen sisältä
from application.tips import models
from application import views

#taulujen luonti
db.create_all()
