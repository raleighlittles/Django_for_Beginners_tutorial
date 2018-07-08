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

        self.valid_response_code = 200
        self.invalid_response_code = 404
        self.redirect_response_code = 302


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

    def test_post_detail_view(self):
        response = self.client.get('/post/1/')
        # a knowingly wrong
        no_response = self.client.get('/post/999/')
        self.assertEqual(response.status_code, self.valid_response_code)
        self.assertEqual(no_response.status_code, self.invalid_response_code)
        self.assertContains(response, 'A good title')
        self.assertTemplateUsed(response, 'post_detail.html')

    def test_post_create_view(self):
        response = self.client.post(reverse('post_new'),
                                    {
                                        'title': 'New title',
                                        'body': 'New text',
                                        'author' : self.user,
                                    })

        self.assertEqual(response.status_code, self.valid_response_code)
        self.assertContains(response, 'New title')
        self.assertContains(response, 'New text')

    def test_post_update_view(self):
        response = self.client.post(reverse('post_edit', args='1'), {
            'title': 'Updated title',
            'body': 'Updated text',
        })
        self.assertEqual(response.status_code, self.redirect_response_code)

    def test_post_delete_view(self):
        response=self.client.get(reverse('post_delete', args='1'))
        self.assertEqual(response.status_code, self.valid_response_code)
