from rest_framework.viewsets import ModelViewSet

from apps.contacts.models import Contact
from apps.contacts.serializers import ContactSerializer
from rest_framework.permissions import AllowAny, IsAdminUser
from .permissions import IsSuperUser


class ContactViewSet(ModelViewSet):
    queryset = Contact.objects.all()
    serializer_class = ContactSerializer

    def get_permissions(self):
        if self.action == "create":
            return [AllowAny()]

        if self.action == "destroy":
            return [IsSuperUser()]
        return [IsAdminUser()]
