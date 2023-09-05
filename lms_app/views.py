from django.shortcuts import render

# Create your views here.
def show(request):
    return render(request , 'demo.html')
    