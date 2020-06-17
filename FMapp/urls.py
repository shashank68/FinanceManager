from django.urls import include, path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('login', views.login, name='login'),
    path('register', views.register, name='register'),
    path('stocks', views.stocks, name='stocks'),
    path('newstock', views.newStockEntry, name='newStock'),
    # path('grph', views.grph, name='graph')
]