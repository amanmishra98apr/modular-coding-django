from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.


def year(request):
    return HttpResponse("I'm final year student")
