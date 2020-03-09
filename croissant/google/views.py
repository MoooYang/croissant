from django.shortcuts import render
from django.http import HttpResponse
import requests

def index(request):
    requests_response = requests.get('https://www.baidu.com')

    django_response = HttpResponse(
        content=requests_response.content,
        status=requests_response.status_code,
        content_type=requests_response.headers['Content-Type']
    )
    return django_response
