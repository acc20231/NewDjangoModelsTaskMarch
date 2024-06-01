from django.contrib.auth.decorators import login_required, permission_required
from django.contrib.auth.mixins import PermissionRequiredMixin, LoginRequiredMixin
from django.http import HttpResponse, HttpResponseNotFound, Http404
from django.shortcuts import render, get_object_or_404
from django.template.loader import render_to_string
from django.urls import reverse_lazy
from django.views.generic import CreateView, UpdateView

menu = [{'title': "О сайте", 'url_name': 'about'},
        {'title': "Добавить новую криптовалюту", 'url_name': 'add_page'},
        {'title': "Войти", 'url_name': 'login'}
        ]

data_db = [
    {'id': 1, 'title': 'Биткоин', 'content': 'Что такое биткоин.', 'is_published': True},
    {'id': 2, 'title': 'Альткоин', 'content': 'Что такое альткоин.', 'is_published': False},
    {'id': 3, 'title': 'Стейблкоин.', 'content': 'Что такое стейблкоин.', 'is_published': True},
]

cats_db = [
    {'id': 1, 'name': 'Блокчейн'},
    {'id': 2, 'name': 'Как получить криптовалюту'},
    {'id': 3, 'name': 'Как использовать криптовалюту'},
]


def index(request):
    data = {'title': 'Главная страница',
            'menu': menu,
            'posts': data_db, }
    return render(request, 'bit/index.html', data)


def show_post(request, post_id):
    return HttpResponse(f"Отображение статьи с id = {post_id}")


def about(request):
    return render(request, 'bit/about.html', {'title': 'О сайте', 'menu': menu})


def categories(request, cat_id):
    return HttpResponse(f"<h1>Статьи по категориям</h1><p >id:{cat_id}</p>")


def categories_by_slug(request, cat_slug):
    if request.GET:
        print(request.GET)
    return HttpResponse(f"<h1>Статьи по категориям</h1><p >slug:{cat_slug}</p>")


def archive(request, year):
    def archive(request, year):
        if year > 2023:
            raise Http404()

    return HttpResponse(f"<h1>Архив по годам</h1><p >{year}</p>")


def page_not_found(request, exception):
    return HttpResponseNotFound('<h1>Страница не найдена</h1>')


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