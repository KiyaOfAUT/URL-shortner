from django.urls import path
from .views import create, find

urlpatterns = [
    path('createurl', create),
    path('<str:pk>', find),
]


