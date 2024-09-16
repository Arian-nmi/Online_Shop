import json
<<<<<<< HEAD
from products.models import Product, Category
from django.shortcuts import render, get_object_or_404
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view
=======

from products.models import Product, Category
from django.shortcuts import render
from django.http import HttpResponse
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse, HttpResponseNotAllowed
>>>>>>> 9750d19510afba2425c8776ebd6db6b453cef295
from products.serializers import ProductSerializer, CategorySerializer


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
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=400)

<<<<<<< HEAD

def products(request):
    context = dict(Product.object.all())
    return render(request, 'product_list.html', context)


def product_detail(request, pk):
    product = Product.objects.get(pk=pk)
    return render(request, 'product_detail.html', {'product': product})
=======
    # products = Product.objects.all()
    # return render(request, 'products/product_list.html', {'products': products})


def product_detail(request, product_id):
    product = get_object_or_404(Product, id=product_id)
    return render(request, 'products/product_detail.html', {'product': product})
>>>>>>> 9750d19510afba2425c8776ebd6db6b453cef295


def category_product_list(request, category_id):
    category = get_object_or_404(Category, id=category_id)
<<<<<<< HEAD
    product = Product.objects.filter(category=category)
    return render(request, 'category_product_list.html', {'category': category, 'products': product})


def home(request):
    return render(request, "home.html")
=======
    products = Product.objects.filter(category=category)
    return render(request, 'products/category_product_list.html', {'category': category, 'products': products})
>>>>>>> 9750d19510afba2425c8776ebd6db6b453cef295
