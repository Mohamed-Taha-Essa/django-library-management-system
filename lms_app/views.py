from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request , 'pages/books.html')


def books(request):
    return render(request, 'pages/books.html')
