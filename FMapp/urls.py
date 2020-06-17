from django.urls import include, path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('login', views.login, name='login'),
    path('logout', views.logout, name='logout'),
    path('register', views.register, name='register'),
    path('stocks', views.stocks, name='stocks'),
    path('newstock', views.newStockEntry, name='newStock'),
    path('savings', views.savings, name='savings'),
    path('newsaving', views.newsaving, name='newsaving'),
    path('loans', views.loans, name='loans'),
    path('newloan', views.newloan, name='newloan'),
    # path('grph', views.grph, name='graph')
]