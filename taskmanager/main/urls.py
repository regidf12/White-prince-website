from django.urls import path
from . import views

urlpatterns = [
    path('', views.homepage, name='homepage'),
    path('about', views.homepage, name='about'),
    path('blog', views.homepage, name='blog'),
    path('contact', views.homepage, name='contact'),
]
