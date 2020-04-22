from . import db

#yhdistetaulu tipeistä ja tageista. Huomio itselleni ja miksei muillekin:
# Jotta Tip-luokassa voidaan viitata tähän yhteystauluun, yhteystaulun täytyy olla jo luotuna. Järjestyksellä on merkitystä ja sen
# takia tämä tiptags-taulu on ylimpänä. Yhteystaulun voi siis luoda ennen classeja, mutta ei toisinpäin.
tiptags = db.Table('tiptags',
    db.Column('tag_id', db.Integer, db.ForeignKey('tag.id'), primary_key=True),
    db.Column('tip_id', db.Integer, db.ForeignKey('tip.id'), primary_key=True)
)

class Tip(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    # Halutaanko näitä allaolevia hakutuloksia somistamaan? 
    date_created = db.Column(db.DateTime, default=db.func.current_timestamp())
    date_modified = db.Column(db.DateTime, default=db.func.current_timestamp(),
    onupdate=db.func.current_timestamp())
    #vinkin nimi ja linkki on String-muodossa
    title = db.Column(db.String(144), nullable=False)
    url = db.Column(db.String(144), nullable=True)
    # puhetta oli, että lukuvinkin voisi merkitä myös luetuksi.
    read = db.Column(db.Boolean, default=False, nullable=False)
    #Tipin viittaus yhteystauluun. Viittauksen sijainti on Tipissä, koska tipin perusteella tagien näyttäminen on todennäköisempää kuin toisinpäin
    tags = db.relationship("Tag", secondary = tiptags, lazy = 'subquery',
    backref = db.backref('tips', lazy = True))

    def __init__(self, title, url):
        self.title = title
        self.url = url
        self.read = False

    @property
    def serialize(self):
        return {
            'id' : self.id,
            'title' : self.title,
            'url' : self.url,
            'read' : self.read,
            'tags' : [tag.name for tag in self.tags],
            'createdAt': self.date_created,
            'read':self.read
        }    

# uusi tag-luokka. Täytyy tarkistaa, kuuluiko tagillekin aikaleima
class Tag(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(144), nullable=False)
    

    #Tagillekin init-metodi
    def __init__(self, name):
        self.name = name    

    #serialize-metodi tagille
    @property
    def serialize(self):
        return {
            'id' : self.id,
            'name' : self.name
        }
	