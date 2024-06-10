# Generated by Django 4.2.1 on 2024-06-10 08:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
        ('Crypto', '0012_alter_customuser_groups'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customgroup',
            name='name',
            field=models.CharField(max_length=150, unique=True, verbose_name='Название группы'),
        ),
        migrations.AlterField(
            model_name='customgroup',
            name='permissions',
            field=models.ManyToManyField(blank=True, to='auth.permission', verbose_name='Разрешения для пользователей'),
        ),
        migrations.AlterField(
            model_name='customuser',
            name='user_permissions',
            field=models.ManyToManyField(blank=True, related_query_name='user', to='Crypto.customgroup', verbose_name='Персональные разрешения для пользователя'),
        ),
    ]
