from django.urls import path
from . import views


urlpatterns = [
    path('', views.HomeView.as_view(), name='index'),
    path('category/<slug>', views.ProductsByCategoryView.as_view(), name='products_category'),
    path('detail/<int:pk>', views.SingleProducDetailView.as_view(), name='single_product'),
    path('tag/<slug>/', views.ProductsByTagsView.as_view(), name='products_tag'),
    path('contact/', views.contact, name='contact'),
]