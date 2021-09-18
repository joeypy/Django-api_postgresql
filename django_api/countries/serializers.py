from rest_framework import serializers
from .models import Country


class CountrySerializer(serializers.ModelSerializer):
    model = Country
    fields  = ('id', 'name', 'capital', )