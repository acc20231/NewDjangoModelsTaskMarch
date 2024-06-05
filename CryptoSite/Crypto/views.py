from django.contrib.auth import authenticate, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.views import LoginView
from django.http import HttpResponse, HttpResponseNotFound, Http404, HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from django.urls import reverse_lazy, reverse
from Crypto.forms import LoginUserForm
from Crypto.models import Crypto

menu = [{'title': "О сайте", 'url_name': 'about'},
        {'title': "Добавить новую криптовалюту", 'url_name': 'add_page'},
        {'title': "Войти", 'url_name': 'login'}
        ]

data_db = [
    {'id': 1, 'title': 'Криптовалюта',
     'content': 'Криптовалюта — это децентрализованная цифровая валюта, которая обеспечивает безопасность с помощью криптографии.',
     'is_published': False},
    {'id': 2, 'title': 'Блокчейн',
     'content': 'Блокчейн — это особая база данных, которую также называют децентрализованным цифровым реестром.',
     'is_published': False},
    {'id': 3, 'title': 'Стейблкоин.', 'content': 'Что такое стейблкоин.', 'is_published': False},
]

cats_db = [
    {'id': 1, 'name': 'Криптовалюта'},
    {'id': 2, 'name': 'Блокчейн'},
    {'id': 3, 'name': 'Как использовать криптовалюту'},
]


def index(request):
    posts = Crypto.objects.filter(is_published=1)
    data = {'title': 'Главная страница',
            'menu': menu,
            'posts': posts, }
    return render(request, 'bit/index.html', data)


def show_post(request, post_slug):
    post = get_object_or_404(Crypto, slug=post_slug)

    data = {
        'title': post.title,
        'menu': menu,
        'post': post,
        'cat_selected': 1,
    }

    return render(request, 'bit/post.html', context=data)

@login_required
def about(request):
    return render(request, 'bit/about.html', {'title': 'О сайте', 'menu': menu})

@login_required
def categories(request, cat_id):
    return HttpResponse(f"<h1>Статьи по категориям</h1><p >id:{cat_id}</p>")

@login_required
def categories_by_slug(request, cat_slug):
    if request.GET:
        print(request.GET)
    return HttpResponse(f"<h1>Статьи по категориям</h1><p >slug:{cat_slug}</p>")


def page_not_found(request, exception):
    return HttpResponseNotFound('<h1>Страница не найдена</h1>')

@login_required
def addpage(request):
    return HttpResponse("Добавить новую криптовалюту")


def login(request):
    return HttpResponse("Авторизация")


def show_category(request, cat_id):
    data = {
        'title': 'Отображение по рубрикам',
        'menu': menu,
        'posts': data_db,
        'cat_selected': cat_id,
    }

    return render(request, 'bit/index.html', context=data)


# def login_user(request):
#     if request.method == 'POST':
#         form = LoginUserForm(request.POST)
#         if form.is_valid():
#             cd = form.cleaned_data
#             user = authenticate(request, username=cd['username'], password=cd['password'])
#             if user and user.is_active:
#                 login(user)
#                 return HttpResponseRedirect(reverse('home'))
#
#     else:
#         form = LoginUserForm()
#     return render(request, 'users/login.html', {'form': form})

class LoginUser(LoginView):
    form_class = AuthenticationForm
    template_name = 'users/login.html'
    extra_context = {'title': "Авторизация"}

    # def get_success_url(self):
    #     return reverse_lazy('home')


def logout_user(request):
    logout(request)
    return HttpResponseRedirect(reverse('login'))