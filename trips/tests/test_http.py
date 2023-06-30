from django.contrib.auth import get_user_model
from rest_framework import status
from rest_framework.reverse import reverse
from rest_framework.test import APITestCase

PASSWORD = 'test@1234'

class AuthenticationTest(APITestCase):
    def test_user_can_sign_up(self):
        print(PASSWORD)