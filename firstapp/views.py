from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.


def test_view(request):
    return HttpResponse("<h1>hello, this is test page</h1>")
