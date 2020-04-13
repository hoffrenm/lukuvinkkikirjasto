import unittest
import json
from application.models import Tip, Tag

from application import create_app, db

class TestApi(unittest.TestCase):

    def setUp(self):
        self.app = create_app('testing')
        self.app_context = self.app.app_context()
        self.app_context.push()
        with self.app.app_context():
            db.create_all()
            db.session.add(Tag("Book"))
            db.session.add(Tag("Blog"))
            db.session.commit()
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

    def test_tag_listing(self):
        response = self.client.get('/api/tags')
        data = response.get_json()
        
        self.assertTrue(response.status_code == 200)
        self.assertTrue(tag.name == "Book" for tag in data)
        self.assertTrue(tag.name == "Blog" for tag in data)
