from flask import request, json, jsonify, redirect, url_for, abort, current_app
from ..models import Tip
from application import db
from . import api # tämä on blueprint ks https://flask.palletsprojects.com/en/1.1.x/blueprints/

@api.route('/tips', methods=['GET'])
def tip_listing():
    tips = Tip.query.all()
    return jsonify([tip.serialize for tip in tips])

@api.route('/tips/<tip_id>', methods = ['GET'])
def tip_get_one(tip_id):
    tip = Tip.query.get(tip_id)
    if tip is None:
        abort(404)


    return jsonify(tip.serialize)

@api.route('/tips', methods = ['POST'])
def tip_create_new():
    if not request.json:
        abort(400)  

    data = request.get_json()

    if "title" not in data:
        abort(400)

    tip = Tip(data["title"].strip(), data["url"].strip())

    db.session().add(tip)
    db.session().commit()

    return jsonify(tip.serialize)