from functools import cached_property
from django.shortcuts import render, get_object_or_404,redirect
from unicodedata import category

from core.forms import ProductForm
from core.models import *
from django.db.models import F, ExpressionWrapper, DecimalField, Avg, Sum
from django.views.generic import ListView, DetailView

# def index(request):
#     categories = Category.objects.all().annotate(product_count=models.Count('products'))
#     return render(request, 'index.html', {'categories': categories})

class CategoryListView(ListView):
    model = Category
    template_name = 'index.html'
    context_object_name = 'categories'
    queryset = Category.objects.all().annotate(product_count=models.Count('products'))

# def categories_details(request, category_name):
#
#     category = get_object_or_404(Category, name=category_name)
#
#     products = Product.objects.filter(category=category).annotate(
#         total_value = ExpressionWrapper(
#             F('price') * F('quantity'),
#             output_field=DecimalField(max_digits=10, decimal_places=2)
#         )
#     ).select_related('category')
#
#     aggregates = products.aggregate(
#         avg_price = Avg('price'),
#         total_sum = Sum('total_value')
#     )
#
#     most_expensive = products.order_by('-price').first()
#     cheapest = products.order_by('price').first()
#
#     return render(request, 'categories_details.html', {
#         'category': category,
#         'products': products,
#         'most_expensive_product': most_expensive,
#         'cheapest_product': cheapest,
#         'avg_product_price': aggregates['avg_price'],
#         'all_product_total_price': aggregates['total_sum'],
#     })

class CategoryDetailView(ListView):
    model = Product
    template_name = 'categories_details.html'
    context_object_name = 'products'

    @cached_property
    def get_category(self):
        return get_object_or_404(Category, name=self.kwargs['category_name'])

    def get_queryset(self):
        category = self.get_category
        return Product.objects.filter(category=category).annotate(
            total_value=ExpressionWrapper(
                F('price') * F('quantity'),
                output_field=DecimalField(max_digits=10, decimal_places=2)
            )
        ).select_related('category')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        category = self.get_category
        products_qs = context['products']
        products = list(products_qs)

        most_expensive = max(products, key=lambda p: p.price, default=None)
        cheapest = min(products, key=lambda p: p.price, default=None)

        if products:
            avg_price = sum(p.price for p in products) / len(products)
            total_price = sum(p.total_value for p in products)
        else:
            avg_price = 0
            total_price = 0

        context.update({
            'category': category,
            'products': products,
            'most_expensive_product': most_expensive,
            'cheapest_product': cheapest,
            'avg_product_price': avg_price,
            'all_product_total_price': total_price,
        })
        return context


class ProductListView(DetailView):
    model = Product
    template_name = 'product_detail.html'
    context_object_name = 'product'

    def get_queryset(self):
        return Product.objects.annotate(
            total_value=ExpressionWrapper(
                F('price') * F('quantity'),
                output_field=DecimalField(max_digits=10, decimal_places=2)
            )
        )



def add_product(request):
    if request.method == 'POST':
        form = ProductForm(request.POST)

        if form.is_valid():
            form.save()
            return redirect('index')
    else:
        form = ProductForm()
    return render(request, 'add_product.html', {'form': form})

def update_product(request,product_pk):
    product =get_object_or_404(Product, pk=product_pk)

    if request.method == 'POST':
        form = ProductForm(request.POST, instance=product)
        if form.is_valid():
            form.save()
            return redirect('categories_details', product.category.name)
    else:
        form = ProductForm(instance=product)
    return render(request, 'update_product.html', {'form': form})

def delete_product(request,product_pk):
    product =get_object_or_404(Product, pk=product_pk)
    if request.method == 'POST':
        product.delete()
        return redirect('index')
    else:
        return redirect('index')

















