from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def todoView(request):
    return render(request,'todo.html')
