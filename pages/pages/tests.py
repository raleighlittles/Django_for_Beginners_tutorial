# pages/tests.py
from django.test import TestCase, SimpleTestCase

# Create your tests here.

class SimpleTests(SimpleTestCase): # use SimpleTestCase instead of TestCase since we're not using a database
    def test_home_page_status_code(self):
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)

    def test_about_page_status_code(self):
        response = self.client.get('/about/')
        self.assertEqual(response.status_code, 200)