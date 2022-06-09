from django.http import Http404, HttpResponseNotFound
from django.shortcuts import render
from django.http.response import HttpResponse

# Create your views in here 

articles = {
    'sports':'Sports Page',
    'finance':'Finance Page',
    'politics': 'Politics Page'
}

"""
# function based view
def sports_view(request):
    return HttpResponse(articles['sports']) # TEMPLATE HTML (JINJA)

def finance_view(request):
    return HttpResponse(articles['finance'])
"""
def news_view(request, topic):
    try:
        #result = articles[topic]
        return HttpResponse(articles[topic])
    except:
        raise Http404('404 GENERIC ERROR') # 404.html 

def add_view(request, num1, num2):
    # domain.com/first_app/num1/num2 --> num1+num2
    add_result = num1 + num2
    result = f"{num1}+{num2} = {add_result}"
    return HttpResponse(str(result))