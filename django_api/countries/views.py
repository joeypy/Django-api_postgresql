from django.core.exceptions import ObjectDoesNotExist
from django.http import JsonResponse

from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.parsers import JSONParser

from .models import Country
from .serializers import CountrySerializer


@api_view(['GET', 'POST'])
def countries_list(request):
    # GET METHOD
    if request.method == 'GET':
        countries = Country.objects.all()

        name = request.GET.get('name', None)
        if name is not None:
            countries = countries.filter(name__icontains=name)

        countries_serializer = CountrySerializer(countries, many=True)
        return JsonResponse(countries_serializer.data, safe=False)
        # 'safe-False' for objects serialization

    # POST METHOD
    elif request.method == 'POST':
        countries_data = JSONParser().parse(request)
        countries_serializer = CountrySerializer(data=countries_data)
        if countries_serializer.is_valid():
            countries_serializer.save()
            return JsonResponse(countries_serializer.data, status=status.HTTP_201_CREATED)
        return JsonResponse(countries_serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET', 'PUT', 'DELETE'])
def countries_detail(request, pk):
    try:
        country = Country.objects.get(pk=pk)
    except ObjectDoesNotExist:
        return JsonResponse(
            {'status': False, 'message': 'The country does not exist'},
            status=status.HTTP_404_NOT_FOUND
        )

    # GET METHOD
    if request.method == 'GET':
        country_serializer = CountrySerializer(country)
        return JsonResponse(country_serializer.data)

    # PUT METHOD
    elif request.method == 'PUT':
        country_data = JSONParser().parse(request)
        country_serializer = CountrySerializer(country, data=country_data)
        if country_serializer.is_valid():
            country_serializer.save()
            return JsonResponse(country_serializer.data, status=status.HTTP_201_CREATED)
        return JsonResponse(country_serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    # DELETE METHOD
    elif request.method == 'DELETE':
        country.delete()
        return JsonResponse(
            {'status': True, 'message': 'Country was deleted successfully'},
            status=status.HTTP_204_NO_CONTENT
        )
