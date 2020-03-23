from django.http import HttpResponse
from django.shortcuts import render
from .account_classifier.classifier import AccountClassifier


# Create your views here.
def account_classifier(request, acc):
    classifier = AccountClassifier()
    outputs = [str(output) for output in classifier.check(acc)]
    print(outputs)
    return HttpResponse(outputs) if outputs else HttpResponse('Unknown')
