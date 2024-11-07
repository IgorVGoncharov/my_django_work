from django.db import models
from django.contrib.auth.models import User


class Recipes_category(models.Model):
    """Модель категорий рецептов"""
    category_name = models.CharField(max_length=100, unique=True, verbose_name='Категория рецепта')
    category_description = models.TextField(verbose_name='Описание катеогрии рецепта')
    image = models.ImageField(upload_to='media', verbose_name='Изображение')

    def __str__(self):
        return self.category_name

class Profile(models.Model):
    """Модель пользователя"""
    user = models.OneToOneField(User, on_delete=models.CASCADE, verbose_name='Пользователь')
    email = models.EmailField(verbose_name='E-mail')
    age = models.IntegerField(verbose_name='Возраст')
    gender = models.CharField(max_length=100, verbose_name='Пол')

class Recipes(models.Model):
    """Модель рецептов"""
    name = models.CharField(max_length=100, unique=True, verbose_name='Название рецепта')
    description = models.TextField(verbose_name='Описание рецепта')
    cooking_steps = models.TextField(verbose_name='Шаги приготовления')
    cooking_time = models.IntegerField(verbose_name='Время приготовления')
    image = models.ImageField(upload_to='media/', verbose_name='Изображение')
    author = models.CharField(max_length=100, verbose_name='Имя автора')
    products = models.TextField(verbose_name='Используемые продукты')
    category = models.ForeignKey(Recipes_category, on_delete=models.CASCADE, verbose_name='Категория рецпета') # не доделал
    user = models.ForeignKey(User, blank=True, verbose_name='Пользователь', on_delete=models.CASCADE)

    def __str__(self):
        return self.name

    def get_summary(self):
        words = self.description.split()
        return f'{" ".join(words[:40])}...'



