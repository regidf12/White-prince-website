from django.urls import path
from . import views

urlpatterns = [
    path('', views.homepage, name='homepage'),
    path('about', views.about, name='about'),
    path('blog', views.ArticleListView.as_view(), name='blog'),
    path('contact', views.contact, name='contact'),
    path('vedmenko-production', views.vedmenkoproduction, name='vedmenkoproduction'),
    path('vedmenko-telegram-bot', views.vedmenkotelegrambot, name='vedmenkotelegrambot'),
    path('vedmenko-vk-bot', views.vedmenkovkbot, name='vedmenkovkbot'),
    path('fearless-vikingz', views.fearlessvikingz, name='fearlessvikingz'),
    path('smart-assistant', views.smartassistant, name='smartassistant'),
]
