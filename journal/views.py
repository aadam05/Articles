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

# Для классовых представлений
from django.views.generic import View, TemplateView, ListView

# Вывод категорий
class ShowCat(ListView):
    model = Category
    context_object_name = 'categories'
    template_name = 'base.html'


# Создание статьи
class ArticleCreating(View):
    def get(self, request):
        form = FormArticle() # создаем пустую форму чтобы после сохранения старой вывелась пустая форма
        return render(request, 'categories/index.html', {'form':form})
    
    def post(self, request):    
        form = FormArticle(request.POST) # закидываем форму с введенными данными в переменную

        if form.is_valid(): 
            form.save() # сохранаяем форму в бд если она валидна
        return render(request, 'categories/index.html', {'form':FormArticle}) # передаем запрос, какой шаблон, и форму
    

############################################################################################################################################

# Регистрация
class Registration(View):
    def get(self, request):
        form = UserCreationForm()
        return render(request, 'categories/reg.html', {'form':form})

    def post(self, request):
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Вы успешно зарегистрированы')
            return redirect('sign_in')
        else:
            messages.error(request, 'Неправильная форма, повторите попытку')
            return render(request, 'categories/reg.html', {'form':UserCreationForm})

# Авторизация
class Auth(View):
    def get(self, request):
        form = AuthenticationForm()
        return render(request, 'categories/login.html', {'form':form})

    def post(self, request):
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            messages.success(request, 'Добро пожаловть ' + username)
        else:
            messages.error(request, 'Логин или пароль неверны, повторите попытку')
            return render(request, 'categories/login.html', {'form':AuthenticationForm})
