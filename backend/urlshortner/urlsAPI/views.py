from django.shortcuts import redirect
from .models import urls
from .serializers import URLdeSerializer, URLSerializer
from rest_framework.decorators import api_view
from rest_framework.response import Response
import random
import string

# Create your views here.


@api_view(['GET'])
def find(request, pk):
    url_obj = urls.objects.get(shortURL=pk)
    url = url_obj.mainURL
    if not url.startswith(('http://', 'https://')):
        url = "http://" + url
    return redirect(url)


@api_view(['POST'])
def create(request):
    url = request.data['url']
    exist = True
    while exist:
        rndmstr = random_string()
        exist = urls.objects.all().filter(shortURL=rndmstr)
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
