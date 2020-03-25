from django.http import HttpResponse
from django.shortcuts import render
from .account_classifier.classifier import AccountClassifier


# Create your views here.
def account_classifier(request, acc):
    classifier = AccountClassifier()
    try:
        outputs = classifier.check(acc)
    except ValueError as E:
        print(E)
        return HttpResponse(str(E))
    except Exception as E:
        print(E)
        return HttpResponse('Error')

    if outputs:
        print(outputs)
        return HttpResponse(str(outputs))
    else:
        print(outputs)
        return HttpResponse('Unknown')
