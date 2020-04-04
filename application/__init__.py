
#Flaskin käyttöönotto
import os
from flask import Flask, render_template, send_from_directory
from flask_sqlalchemy import SQLAlchemy
from config import config

db = SQLAlchemy() # luodaan db:n instanssi ensin ja konffataan create_app -funkkarissa ks. alla

def create_app(config_name):
    app = Flask(__name__, static_folder="../build/static", template_folder="../build") 
    app.config.from_object(config[config_name]) # juurikansiossa config.py:ssä on "testing", "development" ja "production" objektit - parametri config_name on joku näistä
    
    with app.app_context(): # ilman tätä applikaation instanssi ei pääse käsiksi tietokantaan ks. https://flask.palletsprojects.com/en/1.0.x/appcontext/#manually-push-a-context
        db.init_app(app)

        from .models import Tip 
        db.create_all()

    ## blueprinteistä täällä: https://flask.palletsprojects.com/en/1.1.x/blueprints/
    from .api import api as api_blueprint, views # porttaa apin blueprint nimellä api_blueprint ja porttaa ./api/views, jossa routet määritelty
    app.register_blueprint(api_blueprint, url_prefix='/api/') # rekisteröi blueprint ja prefixaa "/api/", jolloin apin routteihin ei tarvitse lisätä "/api/""

    from .main import main as main_blueprint, views # porttaa etusivun blueprint nimellä main_blueprint ja views = etusivu
    app.register_blueprint(main_blueprint) # rekisteröi blueprint

    return app
