from django.shortcuts import render
from .models import urls
from rest_framework import generics
from .serializers import URLdeSerializer, URLSerializer
from rest_framework.decorators import api_view
from rest_framework.response import Response
import random
import string

# Create your views here.


class find(generics.RetrieveAPIView):
    queryset = urls.objects.all()
    serializer_class = URLSerializer
    lookup_field = 'shortURL'


@api_view(['POST'])
def create(request):
    url = request.data['url']
    exist = True
    while exist:
        rndmstr = random_string()
        exist = urls.objects.filter(shortURL=rndmstr)
    both_urls = {"shortURL": rndmstr, "mainURL": url}
    urlobject = URLdeSerializer(data=both_urls)
    if urlobject.is_valid():
        urlobject.save()
        return Response({"shortened url": f"http://127.0.0.1:8000/{rndmstr}"})

    return Response({"message": "server error try again later"}, 500)


def random_string():
    strng = ''
    n = random.uniform(6, 12)
    for i in range(int(n)):
        strng = strng + random.choice(string.ascii_letters)
    return strng
