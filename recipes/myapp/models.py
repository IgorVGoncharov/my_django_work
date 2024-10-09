from django.db import models

class User(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    password = models.CharField(max_length=100)
    age = models.IntegerField()
    sex = models.CharField(max_length=100)

    def __str__(self):
        return f'Username: {self.name}, email: {self.email}, age:{self.age}, sex:{self.sex}'

class Recipes(models.Model): #рецепты
    name = models.CharField(max_length=100)
    description = models.TextField()
    cooking_steps = models.TextField()
    cooking_time = models.TimeField()
    image = models.ImageField(upload_to='repices_image/')
    author = models.CharField(max_length=100)
    products = models.TextField()

class Recipes_category(models.Model):#категрии рецептов
    category_name = models.CharField(max_length=100)
    category_description = models.TextField()
    category_image = models.ImageField(upload_to='repices_cat_image/')

class Choice(models.Model): #ТАБЛИЦА ДЛЯ СВЯЗИ. ДОРАБОТАТЬ!!!!!!!!!!!!!!!!!!!!1#
    user_request = models.ForeignKey(User, on_delete=models.CASCADE)
    selected_category = models.ForeignKey(Recipes_category, on_delete=models.CASCADE)
    selected_recipe = models.ForeignKey(Recipes, on_delete=models.CASCADE)

