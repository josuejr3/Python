from django.shortcuts import render
from django.http import HttpResponse



# Create your views here.

def my_view(request):
    print("Oie")
    return render(
        request,
        'global/index.html',
    )