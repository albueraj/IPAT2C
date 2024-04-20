from django.urls import path
from . import views


urlpatterns = [
    path('olala', views.home, name='home'),
]