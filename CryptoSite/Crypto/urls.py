from django.contrib.auth.views import LogoutView

from . import views, converters
from django.urls import path, include, re_path, register_converter

register_converter(converters.FourDigitYearConverter, "year4")
urlpatterns = [
    path('', views.index, name='home'),
    path('about/', views.about, name='about'),
    path('cats/<int:cat_id>/', views.categories, name='cats_id'),
    path('cats/<slug:cat_slug>/', views.categories_by_slug, name='cats'),
    path('addpage/', views.addpage, name='add_page'),
    path('category/<int:cat_id>/', views.show_category, name='category'),
    path('post/<slug:post_slug>/', views.show_post, name='post'),
    path('login/', views.LoginUser.as_view(), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),

]