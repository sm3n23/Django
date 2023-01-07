from . import views, Api
from django.urls import path
urlpatterns = [
    path('home', views.home, name='home'),


    path('tables.html', views.table, name='table'),
    path('charts.html', views.charts, name='table'),




    #Api
    path('api/list', Api.Dlist, name='DHT11List'),

    # genericViews
    path('api/post', Api.Dhtviews.as_view(), name='DHT_post'),
]