from django.shortcuts import render

def index(request):
    template = 'firehub/index.html'
    context = {}
    return render(request, template, None)