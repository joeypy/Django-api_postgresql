from django.urls import path, re_path
from . import views

urlpatterns = [
    path('api/countries', views.countries_list),
    re_path(r'^api/countries/(?P<pk>[0-9]+)$', views.countries_detail),
]
