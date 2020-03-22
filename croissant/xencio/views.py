import requests
from django.http import HttpResponse
from django.shortcuts import render


# Create your views here.
def accountIdentifier(request):
    requests_response = requests.get('https://www.baidu.com')

    django_response = HttpResponse(
        content=requests_response.content,
        status=requests_response.status_code,
        content_type=requests_response.headers['Content-Type']
    )
    return django_response
