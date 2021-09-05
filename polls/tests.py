from django.contrib.auth import get_user_model
from rest_framework.authtoken.models import Token
from rest_framework.test import APITestCase, APIClient
from rest_framework.test import APIRequestFactory

from polls import apiviews


# class TestPoll(APITestCase):
#     def setUp(self):
#         self.factory = APIRequestFactory()
#         self.view = apiviews.PollViewSet.as_view({'get': 'list'})
#         self.uri = '/polls/'
#         self.user = self.setup_user()
#         self.token = Token.objects.create(user=self.user)
#         self.token.save()
#
#     @staticmethod
#     def setup_user():
#         User = get_user_model()
#         return User.objects.create_user(
#             'test',
#             email='testuser@test.com',
#             password='test'
#         )
#
#     def test_list(self):
#         request = self.factory.get(self.uri, HTTP_AUTHORIZATION=f'Token {self.token.key}')
#         response = self.view(request)
#         self.assertEqual(response.status_code, 200,
#                          f'Expected Response Code 200, received {response.status_code} instead.')


# ==== The same test can be written using APIClient ====================================
class TestPoll(APITestCase):
    def setUp(self):
        self.client = APIClient()
        self.uri = '/polls/'
        self.user = self.setup_user()

    @staticmethod
    def setup_user():
        User = get_user_model()
        return User.objects.create_user(
            'test',
            email='testuser@test.com',
            password='test'
        )

    def test_list2(self):
        self.client.login(username="test", password="test")
        response = self.client.get(self.uri)
        self.assertEqual(response.status_code, 200,
                         f'Expected Response Code 200, received {response.status_code} instead.')

# ==== The same test can be written using APIClient and POST ====================================
    def test_create(self):
        self.client.login(username="test", password="test")
        params = {
            "question": "How are you?",
            "created_by": 1
            }
        response = self.client.post(self.uri, params)
        self.assertEqual(response.status_code, 201,
                         f'Expected Response Code 201, received {response.status_code} instead.'
                         )
