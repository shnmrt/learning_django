from django.urls import path
from . import views

#register the app name
# URL NAMES
app_name = 'my_app'

# domain.com/first_app/simple_view
urlpatterns = [
    path('', views.example_view, name='example'), # domain.com/first_app
    path('variable/',views.variable_view, name='variable')
]