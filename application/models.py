from . import db


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
    
    #Tagit voi toteuttaa joko monen suhde moneen tai 1 suhde moneen tauluna. Monen suhde moneen mallissa tag ei ole tässä taulussa vaan on olemassa erillinen 
    #linkkitaulu niille. 

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
            'read' : self.read
        }    

# uusi tag-luokka. Täytyy tarkistaa, kuuluiko tagillekin aikaleima
class Tag(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(144), nullable=False)	
	
    
#yhdistetaulu tipeistä ja tageista.
tiptags = db.Table('tiptags',
    db.Column('tag_id', db.Integer, db.ForeignKey('tag.id'), primary_key=True),
    db.Column('tip_id', db.Integer, db.ForeignKey('tip.id'), primary_key=True)
)