from django.http import HttpResponse
from django.shortcuts import render
from .account_classifier.classifier import AccountClassifier


# Create your views here.
def account_classifier(request, acc):
    classifier = AccountClassifier()
    try:
        outputs = classifier.check(acc)
    except Exception as E:
        return HttpResponse(str(E))

    if outputs:
        print(outputs)
        return HttpResponse(str(outputs))
    else:
        return HttpResponse('Unknown')
