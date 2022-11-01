from django.urls import path

from . import views

urlpatterns = [
    path('index/', views.index, name='index'),
    path('portfolio/', views.portfolio, name='portfolio'),
    path('about/', views.about, name='about'),
    path('shop/', views.shop, name='shop'),

]
