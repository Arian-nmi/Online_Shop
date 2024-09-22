<<<<<<< HEAD
from django.shortcuts import get_object_or_404
=======
from django.shortcuts import render, get_object_or_404
>>>>>>> 8da2cb7b478197b9389d7f1535fcc5b4cb1cb9f2
from products.models import Product, Category
from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view
<<<<<<< HEAD
from products.serializers import ProductSerializer
=======
from products.serializers import ProductSerializer, CategorySerializer
>>>>>>> 8da2cb7b478197b9389d7f1535fcc5b4cb1cb9f2


@api_view(['GET', 'POST'])
def product_list_creation(request):
    if request.method == 'GET':
        product = Product.objects.all()
        serializer = ProductSerializer(product, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = ProductSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)


def products(request):
<<<<<<< HEAD
    my_products = dict(Product.object.all())
    return render(request, 'products/product_list.html', my_products)


def product_detail(request, pk):
    product = Product.objects.get(pk=pk)
    return render(request, 'products/product_detail.html', {'product': product})


def category_product_list(request, category_id):
    category = get_object_or_404(Category, id=category_id)
    product = Product.objects.filter(category=category)
    return render(request, 'products/category_product_list.html', {'category': category, 'products': product})
=======
    context = dict(Product.object.all())
    return render(request, 'products/product_list.html', context)


def product_detail(request, pk):
    product = Product.objects.get(pk=pk)
    return render(request, 'products/product_detail.html', {'product': product})

    # products = Product.objects.all()
    # return render(request, 'products/product_list.html', {'products': products})


def category_product_list(request, category_id):
    category = get_object_or_404(Category, id=category_id)
    product = Product.objects.filter(category=category)
    return render(request, 'category_product_list.html', {'category': category, 'products': product})
>>>>>>> 8da2cb7b478197b9389d7f1535fcc5b4cb1cb9f2
