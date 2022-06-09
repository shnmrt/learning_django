from django.urls import path
from . import views

# domain.com/first_app/simple_view
urlpatterns = [
    #path('sports/', views.sports_view),
    #path('finance/', views.finance_view),
    path('<str:topic>/', views.news_view), # dynamic view
    path('<int:num1>/<int:num2>', views.add_view)
]