# Curl-testaus

Osa views.py-dokkarien metodeista on testattu manuaalisesti curlilla ennen githubille pushausta. Tarkoituksena on ollut selvittää se, että metodi palauttaa sitä, mitä se vaikuttaisi palauttavan. Tällä testauksella on pyritty saavuttamaan se, ettei front-puolen kehitystyössä kulu aikaa kyseisen metodin väärän toiminnan selvittämiseen. Tässä testidokumentissa on kuvattu kunkin viikon tärkeimmät testit.

## viikko 1. 

Uuden lukuvinkin tallennus POST  osoitteeseen http://localhost:5000/api/tips

Tallennusta on testattu alla olevalla kahteen otteeseen tietokannan muutosten takia:


curl -d '{"name": "Testinimi", "link": "http://www.google.com"}' -H "Content-Type: application/json" http://localhost:5000/api/tips


curl -d '{"title": "Testinimi", "url": "http://www.google.com"}' -H "Content-Type: application/json" http://localhost:5000/api/tips

curl -d '{"title": "Testinimi", "url": "http://www.google.com", "tags": ["kissa","cat","feline"]}' -H "Content-Type: application/json" http://localhost:5000/api/tips