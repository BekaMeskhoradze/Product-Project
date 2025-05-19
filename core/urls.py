from django.urls import path
from core.views import *
from django.views.generic import TemplateView

app_name = 'core'

urlpatterns = [
    path('', CategoryListView.as_view(), name='index'),
    path('about/', TemplateView.as_view(template_name='about.html'), name='about'),
    path('contact/', TemplateView.as_view(template_name='contact.html'), name='contact'),
    path('category/<str:category_name>/', CategoryDetailView.as_view(), name='categories_details'),
    path('product_detail/<int:pk>', ProductListView.as_view(), name='product_detail'),
    path('add_product/', ProductCreateView.as_view(), name='add_product'),
    path('update_product/<int:pk>/', ProductUpdateView.as_view(), name='update_product'),
    path('delete_product/<int:pk>/', ProductDeleteView.as_view(), name='delete_product'),
]