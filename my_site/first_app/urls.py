from django.urls import path
from . import views

# domain.com/first_app/simple_view
urlpatterns = [
    path('', views.simple_view) # domain.com/first_app
]