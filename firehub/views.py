from django.shortcuts import render

# Create your views here.

from django.http import HttpResponse

def index(request):
    template = 'firehub/index.html'
    context = {}
    return render(request, template, None)