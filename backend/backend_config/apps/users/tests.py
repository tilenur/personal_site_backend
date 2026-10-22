from django.contrib.auth.models import User
from rest_framework.test import APITestCase
from rest_framework import status


class JWTAuthenticationTests(APITestCase):
    def test_login_returns_tokens(self):
        credentials = {
            "username": "jwt_test_user",
            "password": "testpassword123",
        }

        User.objects.create_user(**credentials)

        response = self.client.post(
            "/api/token/",
            credentials,
            format="json",
        )

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertIn("access", response.data)
        self.assertIn("refresh", response.data)
