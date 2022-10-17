from django.urls import path
from . import views

urlpatterns = [
    path('basic/', views.basic),
    path('', views.index, name='index'),
    path('contact', views.contact, name='contact'),
    path('about', views.about_us, name='about')
]