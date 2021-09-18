from rest_framework.serializers import ModelSerializer
from .models import Contact


class ContactSerializer(ModelSerializer):
    class Meta:
        model = Contact
        fields = ['country_code', 'phone_number', 'first_name', 'last_name', 'contact_picture', 'is_favorite']
