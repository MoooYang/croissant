from django.http import HttpResponse
from django.shortcuts import render
from .account_classifier.classifier import AccountClassifier


# Create your views here.
def account_classifier(request, acc):
    classifier = AccountClassifier()
    outputs = classifier.check(acc)
    if outputs:
        outputs = [str(output) for output in outputs]
        print(outputs)
        return HttpResponse(outputs)
    else:
        return HttpResponse('Invalidate Account')
