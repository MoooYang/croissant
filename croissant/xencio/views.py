from django.http import HttpResponse
from django.shortcuts import render
from .account_classifier.classifier import AccountClassifier


# Create your views here.
def account_classifier(request, acc):
    classifier = AccountClassifier()
    print(acc)
    output = str(classifier.check(acc))
    print(output)
    return HttpResponse(output)
