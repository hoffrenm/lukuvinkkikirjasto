from flask import Response, request, json, jsonify, redirect, url_for, abort, current_app
from ..models import Tip, Tag
from application import db
from . import api # tämä on blueprint ks https://flask.palletsprojects.com/en/1.1.x/blueprints/

@api.route('/tips', methods=['GET'])
def tip_listing():
    tips = Tip.query.all()
    return Response(json.dumps([tip.serialize for tip in tips]), status=200, mimetype='application/json; charset=utf-8')

@api.route('/tips/<tip_id>', methods = ['GET'])
def tip_get_one(tip_id):
    tip = Tip.query.get(tip_id)

    if tip is None:
        abort(404)

    return jsonify(tip.serialize)

@api.route('/tips', methods = ['POST'])
def tip_create_new():
    data = request.get_json()

    if "title" not in data or not data["title"]:
        return Response(json.dumps({'error': 'title must be provided'}), status=400, mimetype='application/json')

    tip = Tip(data["title"].strip(), data["url"].strip())
    
    for tagName in data["tags"]:
        # oletus että front palauttaa tagin nimen tagina
        tag = Tag.query.filter(Tag.name == tagName).first()
        if tag is None:
            tag = Tag(tagName)
            db.session().add(tag)
        tip.tags.append(tag)

    db.session().add(tip)
    db.session().commit()

    return Response(json.dumps(tip.serialize), status=201, mimetype='application/json')


#metodi vinkin poistamiseen. Laitoin redirectin listaukseen. Sitä tietenkin voi miettiä, mihin sen deletoinnin jälkeen 
#haluaa vievän. Päällepäin tämä näytti toimivan.
@api.route("/tips/<tip_id>/remove", methods = ["POST"])
def tip_remove(tip_id):

    tip = Tip.query.get(tip_id)
    db.session().delete(tip)
    db.session().commit()

    return redirect(url_for("tip_listing"))

#Tag-taulun testaamista varten tehty metodi
@api.route('/tags', methods=['GET'])
def tag_listing():
    tags = Tag.query.all()
    return Response(json.dumps([tag.serialize for tag in tags]), status=200, mimetype='application/json; charset=utf-8')

