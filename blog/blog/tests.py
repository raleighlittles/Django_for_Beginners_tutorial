# blog/tests.py
from django.contrib.auth import get_user_model
from django.test import Client, TestCase
from django.urls import reverse

from . models import Post

# Create your tests here.


class BlogTests(TestCase):

    def setUp(self):
        # Set up a testing user model with a corresponding testing post model

        self.user = get_user_model().objects.create_user(
            username='testuser',
            email='test@domain.com',
            password='password'
        )

        self.post = Post.objects.create(
            title='A good title',
            body='Body content goes here',
            author = self.user
        )

    def test_string_representation(self):
        post = Post(title='A good title')
        self.assertEqual(str(post), post.title)

    def test_post_content(self):
        self.assertEqual(f'{self.post.title}', 'A good title')
        self.assertEqual(f'{self.post.author}', 'testuser')
        self.assertEqual(f'{self.post.body}', 'Body content goes here')

    def test_post_list_view(self):
        response = self.client.get('/post/1/')
        # we only created one test post
        no_response = self.client.get('/post/2/')

        self.assertEqual(response.status_code, 200)
        self.assertEqual(no_response.status_code, 404)
        self.assertContains(response, 'A good title')
        self.assertTemplateUsed(response, 'post_detail.html')