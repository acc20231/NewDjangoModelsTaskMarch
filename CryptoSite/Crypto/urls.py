from django.contrib.auth.views import PasswordChangeView, PasswordChangeDoneView

from . import views, converters
from django.urls import path, include, re_path, register_converter

register_converter(converters.FourDigitYearConverter, "year4")
urlpatterns = [
    path('', views.index, name='home'),
    path('about/', views.about, name='about'),

    path('addpage/', views.addpage, name='add_page'),
    path('category/<int:cat_id>/', views.show_category, name='category'),
    path('post/<slug:post_slug>/', views.show_post, name='post'),

    path('password-change/', views.UserPasswordChange.as_view(), name='password_change'),
    path('password-change/done/', PasswordChangeDoneView.as_view(template_name="users/password_change_done.html"),
         name="password_change_done"),

    path('login/', views.LoginUser.as_view(), name='login'),
    path('logout/', views.logout_user, name='logout'),

    path('register/', views.RegisterUser.as_view(), name='register'),
    path('profile/', views.ProfileUser.as_view(), name='profile'),

]