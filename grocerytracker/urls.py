from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('submitproduct', views.submit_product, name='submit_product'),
    path('displayproducts', views.display_products, name='display_products'),
]