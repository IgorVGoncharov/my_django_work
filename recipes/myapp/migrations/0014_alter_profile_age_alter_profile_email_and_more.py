# Generated by Django 5.1.1 on 2024-11-02 10:35

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0013_alter_recipes_name'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='age',
            field=models.IntegerField(verbose_name='Возраст'),
        ),
        migrations.AlterField(
            model_name='profile',
            name='email',
            field=models.EmailField(max_length=254, verbose_name='E-mail'),
        ),
        migrations.AlterField(
            model_name='profile',
            name='gender',
            field=models.CharField(max_length=100, verbose_name='Пол'),
        ),
        migrations.AlterField(
            model_name='profile',
            name='user',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='Пользователь'),
        ),
        migrations.AlterField(
            model_name='recipes',
            name='author',
            field=models.CharField(max_length=100, verbose_name='Автор'),
        ),
        migrations.AlterField(
            model_name='recipes',
            name='category',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='myapp.recipes_category', verbose_name='Категория рецпета'),
        ),
        migrations.AlterField(
            model_name='recipes',
            name='cooking_steps',
            field=models.TextField(verbose_name='Шаги приготовления'),
        ),
        migrations.AlterField(
            model_name='recipes',
            name='cooking_time',
            field=models.IntegerField(verbose_name='Время приготовления'),
        ),
        migrations.AlterField(
            model_name='recipes',
            name='description',
            field=models.TextField(verbose_name='Описание рецепта'),
        ),
        migrations.AlterField(
            model_name='recipes',
            name='image',
            field=models.ImageField(upload_to='media/', verbose_name='Изображение'),
        ),
        migrations.AlterField(
            model_name='recipes',
            name='products',
            field=models.TextField(verbose_name='Используемые продукты'),
        ),
        migrations.AlterField(
            model_name='recipes_category',
            name='category_description',
            field=models.TextField(verbose_name='Описание катеогрии рецепта'),
        ),
        migrations.AlterField(
            model_name='recipes_category',
            name='category_name',
            field=models.CharField(max_length=100, unique=True, verbose_name='Категория рецепта'),
        ),
        migrations.AlterField(
            model_name='recipes_category',
            name='image',
            field=models.ImageField(upload_to='media', verbose_name='Изображение'),
        ),
    ]
