# Generated by Django 4.2.1 on 2024-06-10 09:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Crypto', '0014_alter_customuser_user_permissions'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customuser',
            name='groups',
            field=models.ManyToManyField(blank=True, to='Crypto.customgroup', verbose_name='Группы'),
        ),
    ]
