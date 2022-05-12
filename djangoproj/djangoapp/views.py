from django.shortcuts import render

# Create your views here.
from django.shortcuts import render


def home(request):
    return render(request, 'home.html')


def new_page(request):
    data = request.GET['fulltextarea']
    return render(request, 'newpage.html', {'data': data})