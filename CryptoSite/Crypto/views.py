from django.contrib.auth import authenticate, logout, get_user_model
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.views import LoginView, PasswordChangeView
from django.http import HttpResponse, HttpResponseNotFound, Http404, HttpResponseRedirect
from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse_lazy, reverse
from django.views.generic import CreateView, UpdateView

from Crypto.forms import LoginUserForm, RegisterUserForm, ProfileUserForm, UserPasswordChangeForm, AddPostForm
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


def page_not_found(request, exception):
    return HttpResponseNotFound('<h1>Страница не найдена</h1>')


def addpage(request):
    if request.method == 'POST':
        form = AddPostForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = AddPostForm()
    return render(request, 'bit/addpage.html', {'menu': menu, 'title': 'Добавление статьи', 'form': form})


def show_category(request, cat_id):
    data = {
        'title': 'Отображение по рубрикам',
        'menu': menu,
        'posts': data_db,
        'cat_selected': cat_id,
    }

    return render(request, 'bit/index.html', context=data)


class LoginUser(LoginView):
    form_class = AuthenticationForm
    template_name = 'users/login.html'
    extra_context = {'title': "Авторизация"}

    def get_success_url(self):
        return reverse_lazy('home')


def logout_user(request):
    logout(request)
    return HttpResponseRedirect(reverse('login'))


class RegisterUser(CreateView):
    form_class = RegisterUserForm
    template_name = 'users/register.html'
    extra_context = {'title': "Регистрация"}
    success_url = reverse_lazy('login')


class ProfileUser(LoginRequiredMixin, UpdateView):
    model = get_user_model()
    form_class = ProfileUserForm
    template_name = 'users/profile.html'
    extra_context = {'title': "Профиль пользователя"}

    def get_success_url(self):
        return reverse_lazy('users:profile', args=[self.request.user.pk])

    def get_object(self, queryset=None):
        return self.request.user


class UserPasswordChange(PasswordChangeView):
    form_class = UserPasswordChangeForm
    success_url = reverse_lazy("password_change_done")
    template_name = "users/password_change_form.html"
    extra_context = {'title': "Изменение пароля"}