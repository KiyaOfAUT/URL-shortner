from django.urls import path
from .views import create, find

urlpatterns = [
    path('createurl', create),
    path('findurl/<str:shortURL>', find.as_view()),
]


