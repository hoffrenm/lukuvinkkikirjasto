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
            db.session.add(Tip("First!", "Here should be url"))
            db.session.add(Tip("Another tip", "Imagine url here too"))
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

    # 404 
    def test_404(self):
        response = self.client.get(
            '/wrong/url',
            headers=self.get_api_headers())
        self.assertTrue(response.status_code == 200) # fiksaa tähän 404 kun virheenkäsittely tehty

    # vinkkilistaus toimii 
    def test_tip_listing(self):
        response = self.client.get('/api/tips')
        data = response.get_json()

        self.assertTrue(response.status_code == 200)
        self.assertTrue(any(tip['title'] == 'First!' for tip in data))
        self.assertTrue(any(tip['url'] == 'Imagine url here too' for tip in data))

    # vinkin luominen onnistuu kun otsikko ja url
    def test_tip_create_new(self):
        response = self.client.post(
            '/api/tips',
            headers=self.get_api_headers(),
            data=json.dumps({'title': 'joku vinkki', 'url': 'joku url'})
        )

        data = response.get_json()

        self.assertTrue(response.status_code == 201)
        self.assertTrue(data['title'] == 'joku vinkki')
        self.assertTrue(data['url'] == 'joku url')
    
    # vinkin luominen onnistuu kun pelkkä otsikko
    def test_tip_create_new_only_title(self):
        response = self.client.post(
            '/api/tips',
            headers=self.get_api_headers(),
            data=json.dumps({'title': 'vinkin otsikko', 'url': ''})
        )

        data = response.get_json()

        self.assertTrue(response.status_code == 201)
        self.assertTrue(data['url'] == '')

    def test_tip_cannot_be_created_without_title(self):
        response = self.client.post(
            '/api/tips',
            headers=self.get_api_headers(),
            data=json.dumps({'url': 'Testing url'})
        )

        self.assertTrue(response.status_code == 400)

    def test_tip_can_be_found_by_id(self):
        response = self.client.get('/api/tips/1')
        data = response.get_json()

        self.assertTrue(response.status_code == 200)
        self.assertTrue(data['title'] == 'First!')
        self.assertTrue(isinstance(data['tags'], list))
        self.assertFalse(data['title'] == 'Another tip')

    def test_tip_has_correct_fields(self):
        response = self.client.get('/api/tips/1')
        
        fields = response.get_json().keys()

        self.assertTrue(response.status_code == 200)
        self.assertTrue("title" in fields)
        self.assertTrue("url" in fields)
        self.assertTrue("read" in fields)
        self.assertTrue("createdAt" in fields)
        self.assertTrue("tags" in fields)

    def test_invalid_id_finds_no_tip(self):
        response = self.client.get('/api/tips/jhfk781')

        self.assertTrue(response.status_code == 404)

    def test_tags_are_added_to_tip(self):
        response = self.client.post(
            '/api/tips',
            headers=self.get_api_headers(),
            data=json.dumps({'title': 'Does adding tags really work?', 'url': 'mysterious url', 'tags': ['Blog', 'Video']})
        )

        data = response.get_json()

        print(data)

        self.assertTrue(response.status_code == 201)
        self.assertTrue(any(tag == 'Blog' for tag in data['tags']))
        self.assertTrue(any(tag == 'Video' for tag in data['tags']))

    def test_tags_are_only_added_once(self):
        response = self.client.post(
            '/api/tips',
            headers=self.get_api_headers(),
            data=json.dumps({'title': 'Multiple same tags', 'url': '', 'tags': ['Blog', 'Blog', 'Blog']})
        )

        self.assertTrue(response.status_code == 201)

        response_tags = self.client.get('/api/tags')

        tags = response_tags.get_json()

        self.assertTrue(response_tags.status_code == 200)
        self.assertTrue(len(tags) == 1)

    def test_tip_can_be_deleted_by_valid_id(self):
        response = self.client.delete('/api/tips/1')

        self.assertTrue(response.status_code == 204)

        response_tips = self.client.get('/api/tips')
        data = response_tips.get_json()

        print(type(data))

        self.assertTrue(response_tips.status_code == 200)
        self.assertTrue(len(data) == 1)
        self.assertFalse(any(tip['title'] == "First!" for tip in data))

    def test_no_tip_is_deleted_by_invalid_id(self):
        response = self.client.delete('/api/tips/999')

        self.assertTrue(response.status_code == 404)

        response_tips = self.client.get('/api/tips')
        data = response_tips.get_json()

        self.assertTrue(response_tips.status_code == 200)
        self.assertTrue(len(data) == 2)
