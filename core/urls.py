from django.urls import path
from core.views import *

urlpatterns = [
    path('',index,name='index'),
    path('category/<str:category_name>/', categories_details, name='categories_details'),
    path('add_product/', add_product, name='add_product'),
]