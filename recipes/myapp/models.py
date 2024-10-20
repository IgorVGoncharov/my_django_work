from django.db import models
from django.contrib.auth.models import User




class Author(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()

    def __str__(self):
        return f'Name: {self.name}, email: {self.email}'

class Post(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    author = models.ForeignKey(Author, on_delete=models.CASCADE)

    def __str__(self):
        return f'Title is {self.title}'

    def get_summary(self):
        words = self.content.split()
        return f'{" ".join(words[:12])}...'


# Готово

# class User(models.Model):#+++#
#     name = models.CharField(max_length=100)
#     email = models.EmailField()
#     password = models.CharField(max_length=100)
#     age = models.IntegerField()
#     gender = models.CharField(max_length=100)
#
#     def __str__(self):
#         return f'Username: {self.name}, email: {self.email}, password: {self.password}, ' \
#                f'age:{self.age}, gender:{self.gender}'

class Recipes_category(models.Model):#категрии рецептов+++
    category_name = models.CharField(max_length=100, unique=True)
    category_description = models.TextField()
    image = models.ImageField(upload_to='media')

    def __str__(self):
        return self.category_name

class Recipes(models.Model): #рецепты
    name = models.CharField(max_length=100, unique=True)
    description = models.TextField()
    cooking_steps = models.TextField()
    cooking_time = models.IntegerField()
    image = models.ImageField(upload_to='media/')
    author = models.CharField(max_length=100)
    products = models.TextField()
    category = models.ForeignKey(Recipes_category, on_delete=models.CASCADE) # не доделал

    def __str__(self):
        return self.name

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    email = models.EmailField()
    age = models.IntegerField()
    gender = models.CharField(max_length=100)

