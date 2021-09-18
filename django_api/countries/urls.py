from django.urls import path

from . import views

urlpatterns = [
    path('', views.CountriesList.as_view()),
    path('<int:pk>', views.CountryDetail.as_view()),
]

