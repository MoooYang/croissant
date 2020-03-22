from django.urls import path
from . import views

app_name = 'xencio'
urlpatterns = [
    path('account/', views.accountIdentifier, name='account'),
]