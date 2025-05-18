from django.urls import path
from core.views import *

urlpatterns = [
    path('', CategoryListView.as_view(), name='index'),
    path('category/<str:category_name>/', CategoryDetailView.as_view(), name='categories_details'),
    path('product_detail/<int:pk>', ProductListView.as_view(), name='product_detail'),
    path('add_product/', add_product, name='add_product'),
    path('update_product/<int:product_pk>/', update_product, name='update_product'),
    path('delete_product/<int:product_pk>/', delete_product, name='delete_product'),
]