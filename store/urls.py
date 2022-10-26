from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('detail/<int:pk>', views.single_product, name='single_product'),
    path('contact/', views.contact, name='contact'),
]