from orders.models import Order, OrderItem
from django.shortcuts import render
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view
from orders.serializers import OrderSerializer


@api_view(['GET', 'POST'])
def order_list(request):
    if request.method == 'GET':
        orders = OrderItem.objects.all()
        serializer = OrderSerializer(orders, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = OrderSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=400)


def order(request):
    my_order = dict(OrderItem.object.all())
    return render(request, 'orders/order_list.html', my_order)


def products(request):
    context = dict(OrderItem.object.all())
    return render(request, 'order_list.html', context)


def order_detail(request, pk):
    order = OrderItem.objects.get(pk=pk)
    return render(request, 'orders/order_detail.html', {'order': order})

