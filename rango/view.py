from django.http import HttpResponse
from django.shortcuts import render

def about(request):
    # Optionally log method or user info:
    print(request.method)
    print(request.user)
    return render(request, 'rango/about.html', {})