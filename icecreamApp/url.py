from unicodedata import name
from django.contrib import admin
from django.urls import path,include
from icecreamApp  import views

urlpatterns = [
    path('', views.index, name='icecreamAPP'),
    path('about',views.about, name='about'),
    path('flavour', views.flavour, name='flavour'),
    path('dryfruit', views.dryfruit, name='dryfruit'),
    path('fruit', views.fruit, name='fruit'),
    path('indiantrde', views.indiantrde, name='indiantrde'),
     path('inter', views.inter, name='inter'),
    path('contact' , views.contact1, name='contact')
    
]