# pages/test.py

from django.test import TestCase, SimpleTestCase
from django.urls import reverse
from django.contrib.auth import get_user_model

# Create your tests here.


class HomePageTests(SimpleTestCase):
    valid_response_code = 200
    home_page_url_name = reverse('home')

    def test_home_page_status_code(self):
        response = self.client.get('/')
        self.assertEqual(response.status_code, self.valid_response_code)

    def test_view_url_by_name(self):
        response = self.client.get(self.home_page_url_name)
        self.assertEqual(response.status_code, self.valid_response_code)

    def test_view_uses_correct_template(self):
        response = self.client.get(self.home_page_url_name)
        self.assertTemplateUsed(response, 'home.html')


class SignupPageTests(TestCase):

    username = 'newuser'
    email = 'newuser@gmail.com'
    valid_response_code = 200
    signup_page_url_name = reverse('signup')

    def test_signup_page_status_code(self):
        response = self.client.get('/users/signup')
        self.assertEqual(response.status_code, self.valid_response_code)

    def test_view_url_by_name(self):
        response = self.client.get(self.signup_page_url_name)
        self.assertEqual(response.status_code, self.valid_response_code)

    def test_view_uses_correct_template(self):
        response = self.client.get(self.signup_page_url_name)
        self.assertTemplateUsed(response, 'signup.html')

    def test_signup_form(self):
        new_user = get_user_model().objects.create_user(self.username, self.email)
        self.assertEqual(get_user_model().objects.all().count(), 1) # test that only 1 valid user is created

        # test that the user model created has the same username and password as our sample user
        self.assertEqual(get_user_model().objects.all()[0].username, self.username)
        self.assertEqual(get_user_model().objects.all()[0].email, self.email)
