from rest_framework.test import APITestCase
from rest_framework import status
from django.contrib.auth.models import User
from .models import Contact


class ContactPermissionTests(APITestCase):
    def test_anonymous_user_cannot_view_contacts(self):
        response = self.client.get("/api/v1/contacts/")

        self.assertIn(
            response.status_code,
            [status.HTTP_401_UNAUTHORIZED, status.HTTP_403_FORBIDDEN],
        )

    def test_anonymous_user_submit_contacts(self):
        data = {
            "name": "Test Visitor",
            "email": "visitor@example.com",
            "message": "AUtomated test message",
        }
        response = self.client.post(
            "/api/v1/contacts/",
            data,
            format="json",
        )

        self.assertEqual(
            response.status_code,
            status.HTTP_201_CREATED,
        )

    def test_staff_user_get_contacts(self):
        user = User.objects.create_user(
            username="teststaff",
            password="testpassword123",
            is_staff=True,
        )

        self.client.force_authenticate(user=user)

        response = self.client.get("/api/v1/contacts/")

        self.assertEqual(
            response.status_code,
            status.HTTP_200_OK,
        )

    def test_staff_user_cannot_delete_contacts(self):
        user = User.objects.create_user(
            username="teststaff",
            password="testpassword123",
            is_staff=True,
        )

        self.client.force_authenticate(user=user)

        contact = Contact.objects.create(
            name="Test Staff",
            email="staff@example.com",
            message="Test staff message",
        )

        response = self.client.delete(f"/api/v1/contacts/{contact.id}/")

        self.assertEqual(
            response.status_code,
            status.HTTP_403_FORBIDDEN,
        )

    def test_superuser_delete_contacts(self):
        superuser = User.objects.create_superuser(
            username="admintest",
            password="testpassword123",
        )

        self.client.force_authenticate(user=superuser)

        contact = Contact.objects.create(
            name="Test Super User",
            email="superuser@example.com",
            message="Super User message",
        )

        response = self.client.delete(f"/api/v1/contacts/{contact.id}/")

        self.assertEqual(
            response.status_code,
            status.HTTP_204_NO_CONTENT,
        )

        self.assertFalse(Contact.objects.filter(id=contact.id).exists())
