from django.shortcuts import render
from django.http import HttpResponse

def members(request):
    return HttpResponse("Ahoj světe")

def members2(request):
    return render(request, 'myfirst.html')