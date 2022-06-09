from django.urls import path
from . import views

# domain.com/first_app/simple_view
urlpatterns = [
    #path('sports/', views.sports_view),
    #path('finance/', views.finance_view),
    #path('<int:num1>/<int:num2>', views.add_view)
    path('<int:num_page>', views.num_page_view), # url redirect
    path('<str:topic>/', views.news_view, name='topic-page'), # dynamic view # name is for reverse look from viem to urls 
]