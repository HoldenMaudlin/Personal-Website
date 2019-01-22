from django.shortcuts import render

def index(request):
    template = 'sudokusource/index.html'
    context = {}
    return render(request, template, None)