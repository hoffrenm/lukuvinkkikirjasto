# lukuvinkkikirjasto

Toteutetut apit:

## 1. Lukuvinkkien listaus GET

http://localhost:5000/api/tips


## 2. Yhden lukuvinkin haku GET

http://localhost:5000/api/tips/<tip_id>


## 3. Uuden lukuvinkin tallennus POST
http://localhost:5000/api/tips

Tallennusta on testattu alla olevalla...
Esim:
curl -d '{"name": "Testinimi", "link": "http://www.google.com"}' -H "Content-Type: application/json" http://localhost:5000/api/tips

## Sovelluksen kokeileminen:
Sovelluksen voi käynnistää komentoriviltä kahdella komennolla. Sovelluksen käynnistämiseksi pitää ajaa ensin pythonin virtuaaliympäristön(venv) käynnistävä komento:

source venv/bin/activate

Seuraavaksi pitää ajaa komento : python run.py

Kirjoittamalla vain python run.py saa virheilmoituksen. 