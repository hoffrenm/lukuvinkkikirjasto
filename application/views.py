import flask
from flask import request, jsonify, redirect, url_for  #requestin tarpeesta en tiedä, jsonify:n pitäisi tehdä json
from application import app
from application.tips.models import Tip
from application import db

@app.route('/api/tips', methods=['GET'])
def tip_listing():
    tips = Tip.query.all()
    return jsonify(json_list = [tip.serialize for tip in tips])

@app.route('/api/tips/<tip_id>', methods = ['GET'])
def tip_get_one(tip_id):
    tip = Tip.query.get(tip_id)
    return jsonify(tip.serialize)

@app.route('/api/tips', methods = ['POST'])
def tip_create_new():
    if not request.json:
        abort(400)  
    tip = Tip(request.json['name'], request.json['link'])    
    db.session().add(tip)
    db.session().commit()
    return redirect(url_for('tip_get_one', tip_id=tip.id)) 





    