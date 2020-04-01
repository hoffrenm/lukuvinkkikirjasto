from application import db


class Tip(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    # Halutaanko näitä allaolevia hakutuloksia somistamaan? 
    date_created = db.Column(db.DateTime, default=db.func.current_timestamp())
    date_modified = db.Column(db.DateTime, default=db.func.current_timestamp(),
    onupdate=db.func.current_timestamp())
    #vinkin nimi ja linkki on String-muodossa
    name = db.Column(db.String(144), nullable=False)
    link = db.Column(db.String(144), nullable=False)
    # puhetta oli, että lukuvinkin voisi merkitä myös luetuksi.
    read = db.Column(db.Boolean, nullable=False)
    
    #Tagit voi toteuttaa joko monen suhde moneen tai 1 suhde moneen tauluna. Monen suhde moneen mallissa tag ei ole tässä taulussa vaan on olemassa erillinen 
    #linkkitaulu niille. 

    def __init__(self, name, link):
        self.name = name
        self.link = link
        self.read = False

    @property
    def serialize(self):
        return {
            'id' : self.id,
            'name' : self.name,
            'link' : self.link,
            'read' : self.read
        }    
