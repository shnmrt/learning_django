from django.shortcuts import render


# Create your views in here 

def example_view(request):
    # first_app/templates/first_app/example.html
    return render(request,'first_app/example.html')