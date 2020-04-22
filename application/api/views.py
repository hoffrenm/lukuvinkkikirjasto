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
    
    if 'tags' in data: # käsitellään tagit vain jos attribuutti "tags" datassa
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
@api.route("/tips/<tip_id>", methods = ["DELETE"]) # metodi DELETE ja REST-käytännön mukaan kutsun route: /api/tips/{tip_id}
def tip_remove(tip_id):

    tip = Tip.query.get_or_404(tip_id) # sama kuin get, mutta palauttaa 404 jos tietuetta ei löydy
    db.session().delete(tip)
    db.session().commit()

    return Response(status=204)

#Tag-taulun testaamista varten tehty metodi
@api.route('/tags', methods=['GET'])
def tag_listing():
    tags = Tag.query.all()
    return Response(json.dumps([tag.serialize for tag in tags]), status=200, mimetype='application/json; charset=utf-8')

#22.4, 3. sprintti
#Tipit yhden tagin perusteella
#Ymmärsin että yhden tagin perusteella, mutta tajusin vasta myöhemmin, että pitikö tämän olla monella tagilla toimiva, eli pitäisikö tag_id:stä olla lista.
@api.route('tags/<tag_name>', methods=['GET'])
def tips_for_tag(tag_name):

    tag = Tag.query.filter(Tag.name==tag_name).first()
    # koska relaatio on backreffillä olemassa tietokannassa, pitäisi olla mahdollista hakea
    # tags = tip.tags ja vastaavasti:
    tips = tag.tips
 
    return Response(json.dumps([tip.serialize for tip in tips]), status=200, mimetype='application/json; charset=utf-8')

#22.4 3.sprintti
#Vinkit, joita ei ole vielä luettu
@api.route('tips/nonread', methods=['GET'])
def tips_non_read():

    tips = Tip.query.filter(Tip.read==False).all()

    return Response(json.dumps([tip.serialize for tip in tips]), status=200, mimetype='application/json; charset=utf-8')