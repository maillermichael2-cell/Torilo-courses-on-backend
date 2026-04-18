from django.urls import path
from .import views              # . means import from the current app package 

# urls patterns 
urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('hello/', views.hello_world, name='hello')
]
