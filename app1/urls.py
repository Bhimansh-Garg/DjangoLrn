from django.urls import path
from . import views
#localHost:8000\app1
urlpatterns = [
    path('', views.app1, name="app1"),
]