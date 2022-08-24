from django.urls import path

from .views import *

urlpatterns = [
    path('', ArticleCreating.as_view(), name='index'),
    path('register', Registration.as_view(), name='sign_up'),
    path('login', Auth.as_view(), name='sign_in'),
    path('category/<slug:slug>/', ShowCat.as_view(), name='category'),
]