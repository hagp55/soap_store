from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('products/', views.all_products),
    path('detail/<int:pk>', views.single_product, name='single_product'),
    path('contact/', views.contact, name='contact'),
    # path('test/', views.page_not_found)
]