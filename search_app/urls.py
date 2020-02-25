from django.urls import path
from . import views 

urlpatterns=[
    path("search/", views.photographer_search, name="photographer_search")
]