# Generated by Django 4.2.1 on 2024-06-10 06:12

import Crypto.manager
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
        ('Crypto', '0008_alter_customuser_is_superuser'),
    ]

    operations = [
        migrations.CreateModel(
            name='CustomGroup',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=150, unique=True, verbose_name='name')),
                ('permissions', models.ManyToManyField(blank=True, to='auth.permission', verbose_name='permissions')),
            ],
            options={
                'verbose_name': 'group',
                'verbose_name_plural': 'groups',
            },
            managers=[
                ('objects', Crypto.manager.CustomGroupManager()),
            ],
        ),
    ]
