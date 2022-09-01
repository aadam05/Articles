from django.urls import path

from .views import *

urlpatterns = [
    path('', CreateFormView.as_view(), name='index'),
    path('register', RegistrationFormView.as_view(), name='sign_up'),
    path('login', AuthFormView.as_view(), name='sign_in'),
    path('category/<slug:slug>', ArticleCreating.as_view(), name='cats'),
]