# Lukuvinkkikirjasto [![CircleCI](https://circleci.com/gh/hoffrenm/lukuvinkkikirjasto.svg?style=shield)](https://circleci.com/gh/hoffrenm/lukuvinkkikirjasto) [![codecov](https://codecov.io/gh/hoffrenm/lukuvinkkikirjasto/branch/master/graph/badge.svg)](https://codecov.io/gh/hoffrenm/lukuvinkkikirjasto)

# [Lukuvinkkikirjaston frontend](https://github.com/hoffrenm/lukuvinkkikirjasto-front) [![CircleCI](https://circleci.com/gh/hoffrenm/lukuvinkkikirjasto-front.svg?style=shield)](https://circleci.com/gh/hoffrenm/lukuvinkkikirjasto-front) [![codecov](https://codecov.io/gh/hoffrenm/lukuvinkkikirjasto-front/branch/master/graph/badge.svg)](https://codecov.io/gh/hoffrenm/lukuvinkkikirjasto-front)



## Linkit

- [Appi herokussa](https://nvinkit.herokuapp.com/)
- [Backlog](https://docs.google.com/spreadsheets/d/1IS_yv30a5yUQ6J1LMNpbrXzmWxI1I0-6cgwT6GnvXSs/edit?usp=sharing)
- [Definition of done](https://github.com/hoffrenm/lukuvinkkikirjasto/blob/master/definitionOfDone.md)

## Suorita testit

### BDD testit
```
pytest tests/step_defs/test_web.py --live-server-port 5000
```
### Integraatiotestit

Alla oleva toimii ainakin Linuxilla (muista aktivoida venv)
```
pytest --cov=./application/api/ --cov-report html
```
Testikattavuusraportti generoituu juurikansioon tiedostoon *htmlcov/index.html*

Kansiossa requests oleva [tip_api.rest](https://github.com/hoffrenm/lukuvinkkikirjasto/blob/master/requests/tip_api.rest) sisältää pyyntöjä joita voi nopeasti suorittaa kehityksen ohessa.

Ohjeet:
1. Asenna Visual Studio Codeen liitännäinen Rest Client (löytyy extensions välilehden kautta)
2. Avaa tip_api.rest tiedosto editorissa
3. Lähetä pyyntö "Send Request" painikkeen avulla, joka on pyynnön yläpuolella
4. Vastaus aukeaa vakiona editoriin uudelle lehdelle

Backendin tulee luonnollisesti olla käynnissä ja pyyntöjä kannattaa toistaa aina kun polkujen logiikkaan tekee muutoksia, jotta muutoksien vaikutukset näkee välittömästi.

## Resursseja

### CircleCi

- [CircleCi: Flask+Heroku konffit](https://github.com/CircleCI-Public/circleci-demo-python-flask/tree/master/.circleci)
- [CircleCI: React konffit](https://medium.com/@eferhatg/create-react-app-continuous-integration-config-with-circleci-and-aws-2b0238cde169)
- [CircleCi: getting started](https://docs.cypress.io/guides/guides/continuous-integration.html#Setting-up-CI)
- [CircleCi: E2E with cypress](https://circleci.com/orbs/registry/orb/cypress-io/cypress)

### E2E

- [Cypress-testaus fullstack-kurssilla](https://fullstackopen.com/osa5/end_to_end_testaus)
- [React unit testing - React ja jest fullstack-kurssilla](https://fullstackopen.com/osa5/react_sovellusten_testaaminen)


## Sovelluksen paikallinen asennus 

1. Asenna sovelluksen käyttöön virtuaaliympäristö
```
$ python3 -m venv venv
```

2. Saata virtuaaliympäristö aktiiviseksi
```
$ source venv/bin/activate
```

3. Asenna projektin riippuvuudet
```
(venv) $ pip install -r requirements.txt
```

4. Käynnistä sovellus
```
(venv) $ python run.py
```

Sovellus käynnistyy oletusarvoisesti osoitteeseen http://localhost:5000/

### Tämänhetkiset frontin polut:

http://localhost:5000 (etusivu)

http://localhost:5000/add-tip (vinkin lisäys)

### rest api (kaikki pyynnöt palauttavat JSONia):

**GET** http://localhost:5000/api/tips (kaikki vinkit)

**GET** http://localhost:5000/api/tips/<tip_id> (yksittäinen vinkki)

**POST** http://localhost:5000/api/tips ottaa {"title":"abc, "url":"123"}, palauttaa {title, url, id, read}


## HUOM

Tietokantamodelin muuttuessa tietokanta (tips.db) pitää poistaa, jotta sqlalchemy luo uuden muuttuneilla tiedoilla
