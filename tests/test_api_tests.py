import unittest
import json
import re

from application import create_app, db

class TestApi(unittest.TestCase):

    def setUp(self):
        self.app = create_app('testing')
        self.app_context = self.app.app_context()
        self.app_context.push()
        with self.app.app_context():
            db.create_all()
        self.client = self.app.test_client()

    def tearDown(self):
        db.session.remove()
        db.drop_all()
        self.app_context.pop()

    def get_api_headers(self):
        return {
            'Accept': 'application/json',
            'Content-Type': 'application/json'
        }

    # 404 
    def test_404(self):
        response = self.client.get(
            '/wrong/url',
            headers=self.get_api_headers())
        self.assertTrue(response.status_code == 200) # fiksaa tähän 404 kun virheenkäsittely tehty

    # vinkkilistaus toimii 
    def test_tip_listing(self):
        response = self.client.get('/api/tips')
        self.assertTrue(response.status_code == 200) # kun ei autentikoitunut

    # vinkin luominen onnistuu kun otsikko ja url
    def test_tip_create_new(self):
        response = self.client.post(
            '/api/tips',
            headers=self.get_api_headers(),
            data=json.dumps({'title': 'joku vinkki', 'url': 'joku url'})
        )
        self.assertTrue(response.status_code == 200) # 201 created ehkä parempi?
    
    # vinkin luominen onnistuu kun pelkkä otsikko
    def test_tip_create_new_only_title(self):
        # response = self.client.post(
        #     '/api/tips',
        #     headers=self.get_api_headers(),
        #     data=json.dumps({'title': 'vinkin otsikko'})
        # )
        self.assertTrue(True == True) # tee testi loppuun
