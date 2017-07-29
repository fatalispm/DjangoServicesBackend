import json

from django.contrib.auth import authenticate
from django.core.urlresolvers import reverse
from test_plus import TestCase

from bb_post.models.token import Token
from bb_post.tests.recipes import UserRecipe


class BaseUserTestCase(TestCase):
    def setUp(self):
        self.user = UserRecipe.make(email='i@gmail.com',
                                     password='123')
        self.user.set_password('password')
        self.user.save()

    def test_get_token(self):
        response = self.client.post(reverse('get-token'), data=json.dumps(dict(
            email=self.user.email,
            password='password'
        )), content_type='application/json')
        self.assertEqual(response.status_code, 200)
        data = json.loads(response.content.decode('utf-8'))
        self.assertIn('token', data['result'])

    def test_cant_get_token_with_wrong_data(self):
        response = self.client.post(reverse('get-token'), data=json.dumps(dict(
            email=self.user.email,
            password='password1'
        )), content_type='application/json')
        self.assertEqual(response.status_code, 200)
        data = json.loads(response.content.decode('utf-8'))
        self.assertEqual(data['success'], False)


