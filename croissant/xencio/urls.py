from django.urls import path
from . import views

app_name = 'xencio'
urlpatterns = [
    path('account/<str:acc>', views.account_classifier, name='account'),
]