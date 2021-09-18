from django.urls import path

from . import views


urlpatterns = [
    path('api/countries', views.CountriesList.as_view()),
    path('api/countries/<int:pk>', views.CountryDetail.as_view()),
]

