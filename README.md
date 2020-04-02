# lukuvinkkikirjasto


## Linkit

- [Backlog](https://docs.google.com/spreadsheets/d/1IS_yv30a5yUQ6J1LMNpbrXzmWxI1I0-6cgwT6GnvXSs/edit?usp=sharing)
- [CircleCI](#)

## Resursseja

### CircleCi

- [CircleCi: Flask+Heroku konffit](https://github.com/CircleCI-Public/circleci-demo-python-flask/tree/master/.circleci)
- [CircleCI: React konffit](https://medium.com/@eferhatg/create-react-app-continuous-integration-config-with-circleci-and-aws-2b0238cde169)
- [CircleCi: getting started](https://docs.cypress.io/guides/guides/continuous-integration.html#Setting-up-CI)
- [CircleCi: E2E with cypress](https://circleci.com/orbs/registry/orb/cypress-io/cypress)

### E2E

- [Cypress-testaus fullstack-kurssilla](https://fullstackopen.com/osa5/end_to_end_testaus)
- [React unit testing - React ja jest fullstack-kurssilla](https://fullstackopen.com/osa5/react_sovellusten_testaaminen)


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
