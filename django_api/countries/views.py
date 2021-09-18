from django.core.exceptions import ObjectDoesNotExist
from django.http import JsonResponse, Http404

from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response

from .models import Country
from .serializers import CountrySerializer


class CountriesList(APIView):
    """
        List all countries, or create a new country.
    """

    def get(self, request, format=None):
        """ List all countries. """
        countries = Country.objects.all()
        countries_serializer = CountrySerializer(countries, many=True)
        return Response(countries_serializer.data)

    def post(self, request, format=None):
        """ Create a new country. """
        country_serializer = CountrySerializer(data=request.data)
        if country_serializer.is_valid():
            country_serializer.save()
            return Response(
                {'status': True, 'data': country_serializer.data},
                status=status.HTTP_201_CREATED
            )
        return Response(
            {
                'status': False,
                'message': 'resource created successfully.',
                'data': country_serializer.data
             },
            status=status.HTTP_400_BAD_REQUEST
        )


class CountryDetail(APIView):
    """
    Retrieve, update or delete a country instance.
    """
    def get_object(self, pk):
        try:
            return Country.objects.get(pk=pk)
        except ObjectDoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        """ Retrieve a country instance. """
        country = self.get_object(pk)
        country_serializer = CountrySerializer(country)
        return Response(
                {
                    'status': True,
                    'data': country_serializer.data
                },
                status=status.HTTP_200_OK
            )

    def put(self, request, pk, format=None):
        """ Update a country instance. """
        country = self.get_object(pk)
        country_serializer = CountrySerializer(country, data=request.data)
        if country_serializer.is_valid():
            country_serializer.save()
            return Response(
                {
                    'status': True,
                    'message': 'resource updated successfully.',
                    'data': country_serializer.data
                },
                status=status.HTTP_200_OK
            )
        return Response(
            {
                'status': False,
                'message': 'can\'t updated the resource.',
                'error': country_serializer.errors
            },
            status=status.HTTP_400_BAD_REQUEST
        )

    def delete(self, request, pk, format=None):
        """ Delete a country instance. """
        country = self.get_object(pk)
        country.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

