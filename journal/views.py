from django.shortcuts import redirect, render

# Формы и модели
from .models import *
from .forms import *

# Для регистрации
from django.contrib.auth.forms import UserCreationForm

# Для логина
from django.contrib.auth import authenticate, login
from django.contrib.auth.forms import AuthenticationForm

# Фреймворк для вывода сообщений
from django.contrib import messages
# messages for CBV
from django.contrib.messages.views import SuccessMessageMixin


# Для классовых представлений
from django.views.generic import View, TemplateView, ListView, FormView

# Это используем в классах(потому что атрибуты класса оцениваются при импорте) 
# Если использовать reverse, то будет ошибка "Reverse Not Found", поэтому используем reverse в функциях
from django.urls import reverse_lazy



# Вывод категорий через ListView
class ArticleCreating(ListView):
    queryset = Category.objects.all()
    context_object_name = 'categories'
    template_name = 'base.html'


# Вывод формы и унаследование категорий
class CreateFormView(ArticleCreating, FormView):
    template_name = 'categories/index.html'
    form_class = FormArticle
    success_url = reverse_lazy('index')

    def form_valid(self, form):
        form.save()
        return super().form_valid(form)
        
############################################################################################################################################

# Регистрация
class RegistrationFormView(SuccessMessageMixin, FormView):
    form_class = UserCreationForm
    template_name = 'categories/reg.html'
    success_url = reverse_lazy('sign_in')
    success_message = 'Пользователь успешно зарегистрирован'

    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

    def form_valid(self, form):
        form.save()
        return super().form_valid(form)

    def form_invalid(self, form):
        messages.add_message(self.request, messages.ERROR, 'Данные введены неверно, повторите попытку')
        return redirect('sign_up')


# Авторизация
class AuthFormView(SuccessMessageMixin, FormView):
    form_class = AuthenticationForm
    template_name = 'categories/login.html'
    success_url = reverse_lazy('index')
    success_message = 'Привет %(username)s'

    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

    def form_valid(self, form):
        login(self.request, form.get_user())
        return super().form_valid(form)

    def form_invalid(self, form):
        messages.add_message(self.request, messages.ERROR, 'Данные введены неверно, повторите попытку')
        return redirect('sign_in')