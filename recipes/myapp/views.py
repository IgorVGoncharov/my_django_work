import logging
from django.core.files.storage import FileSystemStorage
from django.http import HttpResponse
from django.views.generic import CreateView, UpdateView
from django.shortcuts import render, get_object_or_404
from .models import Recipes_category, Profile, Recipes
from .forms import SignUpForm
from django.contrib.auth import login, authenticate
from django.contrib.auth.views import LoginView
from django.urls import reverse_lazy
from .forms import LoginForm, RecipeForm
# from .forms import AddRecipeForm
from django.contrib.auth import logout
from django.shortcuts import redirect

def index(request):
    # logger.info('Index page accessed')
    return HttpResponse("Hello, world!")

# class AddRecipe(CreateView):
#     '''Добавление рецепта'''
#     form_class = AddRecipeForm
#     template_name = 'myapp/add_recipe.html'
#     success_url = reverse_lazy('add_rec_confirm')
#     extra_context = {
#         'title': 'Добавление рецепта',
#     }

def add_recipe(request):
    if request.user.is_authenticated == True:
        if request.method == 'POST':
            form = RecipeForm(request.POST, request.FILES)
            message = 'Ошибка в данных'
            if form.is_valid():
                name = form.cleaned_data['name']
                description = form.cleaned_data['description']
                cooking_steps = form.cleaned_data['cooking_steps']
                cooking_time = form.cleaned_data['cooking_time']
                author = form.cleaned_data['author']
                products = form.cleaned_data['products']
                category = form.cleaned_data['category']
                user = request.user
                image = form.cleaned_data['image']
                fs = FileSystemStorage()
                fs.save(image.name, image)
                recipe = Recipes(name= name,
                                 description= description,
                                 cooking_steps= cooking_steps,
                                 cooking_time= cooking_time,
                                 image= image,
                                 author= author,
                                 products= products,
                                 category=category,
                                 user=user)
                recipe.save()
                message = 'Рецепт сохранен'
                return render(request, 'myapp/confirm.html', {'form': form, 'message': message})
        else:
            form = RecipeForm()
            message = 'Заполните форму рецепта'
            return render(request, 'myapp/add_recipe.html', {'form': form, 'message': message})
    else:
        message = 'Зайдите на сайт и Вы сможете добавлять рецепты'
        return render(request, 'myapp/confirm.html', {'message': message})

class UpdateRecipe(UpdateView):
    '''Изменение рецепта'''
    model = Recipes
    fields = ['name', 'description', 'cooking_steps', 'cooking_time', 'image', 'author', 'products', 'category']
    template_name = 'myapp/edit_recipe.html'
    success_url = reverse_lazy('change_rec_confirm')
    labels = ['наименование']
    extra_context = {
        'title': 'Редактирование рецепта',
    }



def all_categorys(request):
    """Форма для всех категорий рецептов"""
    categorys = Recipes_category.objects.all()
    return render(request, 'myapp/all_category.html', {'categorys': categorys})

def all_recipes(request):
    """Форма для всех рецептов"""
    recipes = Recipes.objects.all()
    return render(request, 'myapp/all_recipes.html', {'recipes': recipes, "title": "Все рецепты: "})

def category_full(request, category_id):
    """Форма для ссылки на отдельную категорию рецепта"""
    category = get_object_or_404(Recipes_category, pk=category_id)
    return render(request, 'myapp/recipe_full.html', {'category': category})

def recipe_full(request, recipe_id):
    """Форма для ссылки на отдельный рецепт"""
    recipe = get_object_or_404(Recipes, pk=recipe_id)
    return render(request, 'myapp/one_recipe.html', {'recipe': recipe})

def one_category(request, category_id):
    '''Форма отдельной категории'''
    category = get_object_or_404(Recipes_category, pk=category_id)
    return render(request, 'myapp/one_category.html', {'category': category})

class user_login(LoginView):
    '''Форма авторизации'''
    form_class = LoginForm
    template_name = 'myapp/login.html'
    extra_context = {'title': 'Авторизация на сайте'}

    def get_success_url(self):
        return reverse_lazy('five_recipes')

def logout_view(request):
    '''Форма выхода пользователя'''
    logout(request)
    return render(request, 'myapp/confirm.html', {'message': "Вы успешно вышли с сайта"})

# def logout_redirect(request):
#     return render(request, 'myapp/logout.html')

def add_rec_confirm(request):
    return render(request, 'myapp/confirm.html', {'message': "Рецепт успешно добавлен"})

def add_user_confirm(request):
    return render(request, 'myapp/confirm.html', {'message': "Пользователь успешно зарегистрирован"})

def change_rec_confirm(request):
    return render(request, 'myapp/confirm.html', {'message': "Изменения упешно внесены"})

def registration(request):
    """Регистрация новго пользователя"""
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            email = form.cleaned_data.get('email')
            age = form.cleaned_data.get('age')
            gender = form.cleaned_data.get('gender')
            profile = Profile(user=user, email=email, age=age, gender=gender)
            profile.save()
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=user.username, password=raw_password)
            login(request, user)
            return redirect('add_user_confirm')
    else:
        form = SignUpForm()
    return render(request, 'myapp/signup.html', {'form': form})

def recipes_by_category(request, category_id):
    """------"""
    recipes = Recipes.objects.filter(category_id=category_id)
    return render(request, 'myapp/all_recipes.html', {'recipes': recipes, "title": "Рецепты в выбранной категории: "})

def five_recipes(request):
    """Форма для пяти случаных рецептов"""
    recipes = Recipes.objects.all().order_by('?')[:5]
    return render(request, 'myapp/all_recipes.html', {'recipes': recipes, "title": "Пять случайных рецептов: "})

def one_recipe(request, recipe_id):
    '''Форма отдельного рецепта'''
    rec = get_object_or_404(Recipes, pk=recipe_id)
    return render(request, 'myapp/one_recipe.html', {'recipe': rec})

def user_check(request, recipe_id):
    """Форма проверки пользователя"""
    if request.user.is_authenticated == True:
        system_user = request.user
        recipes = get_object_or_404(Recipes, pk=recipe_id)
        object_user = recipes.user
        if system_user == object_user:
            return redirect(f'/edit/{recipe_id}/')
        else:
            message ="Вы не можете редактировать рецепт другого пользователя"
            return render(request, 'myapp/confirm.html', {'message': message})
    else:
        message = 'Необходимо сначала зайти на сайт'
        return render(request, 'myapp/confirm.html', {'message': message})
