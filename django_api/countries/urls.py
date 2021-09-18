from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns

from . import views

urlpatterns = [
    path('api/countries', views.CountriesList.as_view()),
    path('api/countries/<int:pk>', views.CountryDetail.as_view()),
]

