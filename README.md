# Lukuvinkkikirjasto [![CircleCI](https://circleci.com/gh/hoffrenm/lukuvinkkikirjasto.svg?style=svg)](https://circleci.com/gh/hoffrenm/lukuvinkkikirjasto)

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
