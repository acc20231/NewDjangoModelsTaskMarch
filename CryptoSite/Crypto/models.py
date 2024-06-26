from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin, Permission
from django.urls import reverse
from .manager import CustomUserManager, CustomGroupManager

class CustomUser(AbstractBaseUser, PermissionsMixin):
    class Status(models.IntegerChoices):
        DRAFT = 0, 'Мужчина'
        PUBLISHED = 1, 'Женщина'

    username = models.CharField(verbose_name="Логин", max_length=150, unique=True, )
    email = models.EmailField(verbose_name="E-mail адрес", blank=True, max_length=200)
    first_name = models.CharField(verbose_name="Имя", max_length=150, blank=True, default='')
    last_name = models.CharField(verbose_name="Фамилия", max_length=150, blank=True, default='')

    groups = models.ManyToManyField('Crypto.CustomGroup', blank=True, verbose_name="Группы",)

    is_staff = models.BooleanField(default=False, verbose_name='Доступ к сайду администратора')
    is_active = models.BooleanField(default=True, verbose_name='Активность')
    is_superuser = models.BooleanField(default=False, verbose_name='Администратор')
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

class CustomGroup(models.Model):
    name = models.CharField(("Название группы"), max_length=150, unique=True)
    permissions = models.ManyToManyField(
        Permission,
        verbose_name=("Разрешения для пользователей"),
        blank=True,
    )

    objects = CustomGroupManager()

    class Meta:
        verbose_name = ("Группа")
        verbose_name_plural = ("Группы")

    def __str__(self):
        return self.name

    def natural_key(self):
        return (self.name,)
class Crypto(models.Model):

    class Status(models.IntegerChoices):
        DRAFT = 0, 'Черновик'
        PUBLISHED = 1, 'Опубликовано'

    title = models.CharField(max_length=255, verbose_name='Название криптовалюты')
    slug = models.SlugField(max_length=255, db_index=True, verbose_name='URL')
    category = models.ForeignKey('Category', on_delete=models.CASCADE, null=True, verbose_name='Категория криптовалюты')
    user = models.ForeignKey('CustomUser', on_delete=models.CASCADE, null=True, verbose_name='Пользователь')
    content = models.TextField(blank=True, verbose_name='Информация о криптовалюте')
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
    slug = models.SlugField(max_length=255, unique=True, db_index=True, verbose_name='URL')

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'

    def __str__(self):
        return self.name

