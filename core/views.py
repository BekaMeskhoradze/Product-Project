from django.shortcuts import render, get_object_or_404,redirect
from core.forms import ProductForm
from core.models import *
from django.db.models import F, ExpressionWrapper, DecimalField, Avg, Sum

def index(request):
    categories = Category.objects.all().annotate(product_count=models.Count('products'))
    return render(request, 'index.html', {'categories': categories})

def categories_details(request, category_name):
    #name-ს იმიტო ვატან,რადგან მოდელში name => unique=True
    category = get_object_or_404(Category, name=category_name)
    #Database-ში გამოთვლის price * quantity და მერე გამოაქვს
    products = Product.objects.filter(category=category).annotate(
        total_value = ExpressionWrapper(
            F('price') * F('quantity'),
            output_field=DecimalField(max_digits=10, decimal_places=2)
        )
    ).select_related('category')

    aggregates = products.aggregate(
        avg_price = Avg('price'),
        total_sum = Sum('total_value')
    )

    most_expensive = products.order_by('-price').first()
    cheapest = products.order_by('price').first()

    return render(request, 'categories_details.html', {
        'category': category,
        'products': products,
        'most_expensive_product': most_expensive,
        'cheapest_product': cheapest,
        'avg_product_price': aggregates['avg_price'],
        'all_product_total_price': aggregates['total_sum'],
    })

def add_product(request):
    if request.method == 'POST':
        form = ProductForm(request.POST)

        if form.is_valid():
            form.save()
            return redirect('index')
    else:
        form = ProductForm()
    return render(request, 'add_product.html', {'form': form})