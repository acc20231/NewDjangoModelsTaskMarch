from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from django.urls import reverse
from .manager import CustomUserManager

class CustomUser(AbstractBaseUser, PermissionsMixin):
    class Status(models.IntegerChoices):
        DRAFT = 0, 'Мужчина'
        PUBLISHED = 1, 'Женщина'

    username = models.CharField(verbose_name="username", max_length=150, unique=True, )
    email = models.EmailField(verbose_name="email address", blank=True, max_length=200)
    first_name = models.CharField(verbose_name="first_name", max_length=150, blank=True, default='')
    last_name = models.CharField(verbose_name="last_name", max_length=150, blank=True, default='')
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    is_superuser = models.BooleanField(default=False)
    type = models.BooleanField(choices=tuple(map(lambda x: (bool(x[0]), x[1]), Status.choices)),
                               default=Status.DRAFT, verbose_name='Пол')

    EMAIL_FIELD = "email"
    USERNAME_FIELD = "username"
    REQUIRED_FIELDS = ["email"]

    objects = CustomUserManager()

    class Meta:
        verbose_name = 'Пользователя'
        verbose_name_plural = 'Пользователи'

    def has_perm(self, perm, obj=None):
        return True

    @property
    def is_admin(self):
        return self.admin

    def __str__(self):
        return self.username

class Crypto(models.Model):

    class Status(models.IntegerChoices):
        DRAFT = 0, 'Черновик'
        PUBLISHED = 1, 'Опубликовано'

    title = models.CharField(max_length=255)
    slug = models.SlugField(max_length=255, db_index=True, unique=True)
    category = models.ForeignKey('Category', on_delete=models.CASCADE, null=True)
    user = models.ForeignKey('CustomUser', on_delete=models.CASCADE, null=True)
    content = models.TextField(blank=True)
    time_create = models.DateTimeField(auto_now_add=True)
    time_update = models.DateTimeField(auto_now=True)
    is_published = models.BooleanField(choices=tuple(map(lambda x: (bool(x[0]), x[1]), Status.choices)),
                                       default=Status.DRAFT, verbose_name='Статус')

    class Meta:
        verbose_name = 'Виды криптовалют'
        verbose_name_plural = 'Вид криптовалют'
        ordering = ['-time_create']
        indexes = [
            models.Index(fields=['-time_create'])
        ]

    def get_absolute_url(self):
        return reverse('post', kwargs={'post_slug': self.slug})

    def __str__(self):
        return self.title


class Category(models.Model):
    name = models.CharField(max_length=100, db_index=True, verbose_name='Категории')
    slug = models.SlugField(max_length=255, unique=True, db_index=True, verbose_name='Slug')

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'

    def __str__(self):
        return self.name