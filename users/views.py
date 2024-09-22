from django.shortcuts import render
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view
from users.models import User
from users.serializers import UserSerializer


@api_view(['GET', 'POST'])
def user_list(request):
    if request.method == 'GET':
        users = User.objects.all()
        serializer = UserSerializer(users, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=400)


<<<<<<< HEAD
def users(request):
    user = dict(User.objects.all())
    return render(request, 'users/user_list.html', user)


def user_detail(request, pk):
    user = User.objects.get(pk=pk)
    return render(request, 'users/user_detail.html', {'user': user})
=======
def user(request):
    context = dict(User.objects.all())
    return render(request, 'user_list.html', context)


def user_detail(request, pk):
    users = User.objects.get(pk=pk)
    return render(request, 'user_detail.html', {'users': users})
>>>>>>> 8da2cb7b478197b9389d7f1535fcc5b4cb1cb9f2
