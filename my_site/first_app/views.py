from django.shortcuts import render
from django.http.response import HttpResponse

# Create your views in here 

def simple_view(request):
    return HttpResponse('SIMPLE VIEW') # TEMPLATE HTML (JINJA)

