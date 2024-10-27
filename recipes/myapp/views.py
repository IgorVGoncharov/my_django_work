import logging
from django.core.files.storage import FileSystemStorage
from django.views import View
from django.http import HttpResponse, JsonResponse
from django.views.generic import TemplateView, FormView, CreateView, UpdateView
from django.shortcuts import render, get_object_or_404, redirect
from .models import Author, Post, Recipes_category, Profile, Recipes
from .forms import ImageForm, RecipeForm, SignUpForm
from .forms import UserForm, ManyFieldsForm, RecipesCategoryForm
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.views import LoginView
from django.urls import reverse_lazy
from .forms import LoginForm
from .forms import AddPostForm
from random import sample
from django.contrib.auth import logout
from django.shortcuts import redirect



menu = [{'title': "О сайте", 'url_name': 'about'},
        {'title': "Добавить статью", 'url_name': 'add_page'},
        {'title': "Обратная связь", 'url_name': 'contact'},
        {'title': "Войти", 'url_name': 'login'}
        ]

# menu = [{'title': "О сайте", 'url_name': 'about'},
#         {'title': "Добавить статью", 'url_name': 'add_page'},
#         {'title': "Обратная связь", 'url_name': 'contact'},
#         {'title': "Войти", 'url_name': 'login'}
#         ]

# logger = logging.getLogger(__name__)
#
# def index(request):
#     logger.info('Index page accessed')
#     return HttpResponse("Hello, world!")
# def about(request):
#     try:
#         # some code that might raise an exception
#         result = 1 / 0
#     except Exception as e:
#         logger.exception(f'Error in about page: {e}')
#         return HttpResponse("Oops, something went wrong.")
#     else:
#         logger.debug('About page accessed')
#         return HttpResponse("This is the about page.")
# def about(request):
#     return HttpResponse("About us")
# def recipes(request):
#     return HttpResponse("Страница с рецептами")



class HelloView(View):
    def get(self, request):
        return HttpResponse("Hello World from class!")

def hello(request):
    return HttpResponse("Hello World from function!")

def year_post(request, year):
    text = ""
    ... # формируем статьи за год
    return HttpResponse(f"Posts from {year}<br>{text}")

class MonthPost(View):
    def get(self, request, year, month):
        text = ""
        ... # формируем статьи за год и месяц
        return HttpResponse(f"Posts from {month}/{year}<br>{text}")

def post_detail(request, year, month, slug):
    ... # Формируем статьи за год и месяц по идентификатору. Пока обойдёмся без запросов к базе данных
    post = {
        "year": year,
        "month": month,
        "slug": slug,
        "title": "Кто быстрее создаёт списки в Python, list() или []",
        "content": "В процессе написания очередной программы задумался над тем,"
                    "какой способ создания списков в Python работает быстрее..."
    }
    return JsonResponse(post, json_dumps_params={'ensure_ascii':False})

def my_view(request):
    context = {"name": "John"}
    return render(request, "myapp/my_template.html", context)

class TemplIf(TemplateView):
    template_name = "myapp/templ_if.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['message'] = "Привет, мир!"
        context['number'] = 5
        return context

def view_for(request):
    my_list = ['apple', 'banana', 'orange']
    my_dict = {
        'каждый': 'красный',
        'охотник': 'оранжевый',
        'желает': 'жёлтый',
        'знать': 'зелёный',
        'где': 'голубой',
        'сидит': 'синий',
        'фазан': 'фиолетовый',
        }
    context = {'my_list': my_list, 'my_dict': my_dict}
    return render(request, 'myapp/templ_for.html', context)

def index(request):
    return render(request, 'myapp/index.html')

def about(request):
    return render(request, 'myapp/about.html')

def author_posts(request, author_id):
    author = get_object_or_404(Author, pk=author_id)
    posts = Post.objects.filter(author=author).order_by('-id')[:5]
    return render(request, 'myapp/author_posts.html', {'author': author, 'posts': posts})
    # return render(request, 'myapp/author_posts.html', {'author': author})

def post_full(request, post_id):
    post = get_object_or_404(Post, pk=post_id)
    return render(request, 'myapp/post_full.html', {'post': post})

logger = logging.getLogger(__name__)

def user_form(request):
    if request.method == 'POST':
        form = UserForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            email = form.cleaned_data['email']
            age = form.cleaned_data['age']
            # Делаем что-то с данными
            logger.info(f'Получили {name=}, {email=}, {age=}.')
    else:
        form = UserForm()
    return render(request, 'myapp/user_form.html', {'form': form})

def many_fields_form(request):
    if request.method == 'POST':
        form = ManyFieldsForm(request.POST)
        if form.is_valid():
        # Делаем что-то с данными
            logger.info(f'Получили {form.cleaned_data=}.')
    else:
        form = ManyFieldsForm()
    return render(request, 'myapp/many_fields_form.html', {'form': form})

def recipes_category_form(request):#+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
    if request.method == 'POST':
        form = RecipesCategoryForm(request.POST)
        if form.is_valid():
            logger.info(f'Получили {form.cleaned_data=}.')
    else:
        form = RecipesCategoryForm()
    return render(request, 'myapp/add_category_recipes.html', {'form': form})





def upload_image(request):
    if request.method == 'POST':
        form = ImageForm(request.POST, request.FILES)
        if form.is_valid():
            image = form.cleaned_data['image']
            fs = FileSystemStorage()
            fs.save(image.name, image)
    else:
        form = ImageForm()
    return render(request, 'myapp/upload_image.html', {'form':form})

#UГотово



def add_category(request):#Готово
    #Добавление категории
    if request.method == 'POST':
        form = RecipesCategoryForm(request.POST, request.FILES)
        message = 'Ошибка в данных'
        if form.is_valid():
            category_name = form.cleaned_data['category_name']
            category_description = form.cleaned_data['category_description']
            image = form.cleaned_data['image']
            fs = FileSystemStorage()
            fs.save(image.name, image)
            logger.info(f'Получили {category_name=}, {category_description=}, {image=}. ')
            category = Recipes_category(category_name=category_name,
                        category_description=category_description,
                        image=image)
            category.save()
            message = 'Категория рецепта сохранена'
    else:
        form = RecipesCategoryForm()
        message = 'Заполните форму'
    return render(request, 'myapp/add_category_recipes.html', {'form':  form, 'message': message})

def add_recipe(request):#Готово
    #Добавление категории
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
            image = form.cleaned_data['image']
            fs = FileSystemStorage()
            fs.save(image.name, image)
            logger.info(f'Получили {name=}, {description=}, {cooking_steps=}, '
                        f'{cooking_time=}, {author=}, {products=}, {image=}. ')
            #category = Recipes_category(category_name=category_name,
            #            category_description=category_description,
            #            image=image)
            #category.save()
            message = 'Рецепт сохранен'
    else:
        form = RecipeForm()
        message = 'Заполните форму'
    return render(request, 'myapp/add_category_recipes.html', {'form':  form, 'message': message})



# def registration(request):
#     if request.method == 'POST':
#         form = SignUpForm(request.POST)
#         if form.is_valid():
#             user = form.save()
#             email = form.cleaned_data.get('email')
#             age = form.cleaned_data.get('age')
#             gender = form.cleaned_data.get('gender')
#             profile = Profile(user=user, email=email, age=age, gender=gender)
#             profile.save()
#             raw_password = form.cleaned_data.get('password1')
#             user = authenticate(username=user.username, password=raw_password)
#             login(request, user)
#             return redirect('/')
#     else:
#         form = SignUpForm()
#     return render(request, 'myapp/signup.html', {'form': form})




def add_user(request):
    if request.method == 'POST':
        form = UserForm(request.POST)
        message = 'Ошибка в данных'
        if form.is_valid():
            name = form.cleaned_data['name']
            email = form.cleaned_data['email']
            password = form.cleaned_data['password']
            age = form.cleaned_data['age']
            gender = form.cleaned_data['gender']
            logger.info(f'Получили {name=}, {email=}, {password=}, {age=}, {gender=}. ')
            user = User(name=name, email=email, age=age, password=password, gender=gender)
            user.save()
            message = 'Пользователь сохранён'
    else:
        form = UserForm()
        message = 'Заполните форму'
    return render(request, 'myapp/user_form.html', {'form':  form, 'message': message})

def registration(request):#++++Готово++++
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
            return redirect('/')
    else:
        form = SignUpForm()
    return render(request, 'myapp/signup.html', {'form': form})

class user_login(LoginView):#++++Готово+++
    '''Форма авторизации'''
    form_class = LoginForm
    template_name = 'myapp/login.html'
    extra_context = {'title': 'Авторизация на сайте'}

    def get_success_url(self):
        return reverse_lazy('index')

def logout_view(request):
    logout(request)
    return redirect('/')

def one_recipe(request, recipe_id): #+++Готово+++
    '''Форма отдельного рецепта'''
    rec = get_object_or_404(Recipes, pk=recipe_id)
    return render(request, 'myapp/one_recipe.html', {'recipe': rec})

def one_category(request, category_id): #+++Готово+++
    '''Форма отдельной категории'''
    category = get_object_or_404(Recipes_category, pk=category_id)
    return render(request, 'myapp/one_category.html', {'category': category})



def recipe_full(request, recipe_id):#+++Готово+++
    """Форма для ссылки на отдельный рецепт"""
    recipe = get_object_or_404(Post, pk=recipe_id)
    return render(request, 'myapp/recipe_full.html', {'recipe': recipe})

def five_recipes(request):#+++Готово+++
    """Форма для пяти случаных рецептов"""
    recipes = Recipes.objects.all().order_by('?')[:5]
    return render(request, 'myapp/all_recipes.html', {'recipes': recipes})

def all_categorys(request):#+++Готово+++
    """Форма для всехкатегорий рецептов"""
    categorys = Recipes_category.objects.all()
    return render(request, 'myapp/all_category.html', {'categorys': categorys})

def all_recipes(request):#+++Готово+++
    """Форма для всех рецептов"""
    recipes = Recipes.objects.all()
    return render(request, 'myapp/all_recipes.html', {'recipes': recipes})

def category_full(request, category_id):#+++Готово+++
    """Форма для ссылки на отдельный рецепт"""
    category = get_object_or_404(Recipes_category, pk=category_id)
    return render(request, 'myapp/recipe_full.html', {'category': category})

# class let_try(CreateView):
#     form_class = LetTryForm
#     template_name = 'myapp/add_recipe.html'
#     success_url = reverse_lazy('myapp/login.html')
#     extra_context = {
#         'menu': menu,
#         'title': 'Добавление статьи',
#     }

# class AddPage(CreateView):
#     form_class = AddPostForm
#     # model = Women
#     # fields = ['title', 'slug', 'content', 'is_published']
#     template_name = 'women/addpage.html'
#     # success_url = reverse_lazy('home')
#     extra_context = {
#         'menu': menu,
#         'title': 'Добавление статьи',
#     }

class AddPage(CreateView):
    form_class = AddPostForm
    # model = Women
    # fields = ['title', 'slug', 'content', 'is_published']
    template_name = 'myapp/addpage.html'
    success_url = reverse_lazy('index')
    extra_context = {
        'menu': menu,
        'title': 'Добавление рецепта',
    }

class UpdatePage(UpdateView):
    model = Recipes
    fields = ['name', 'description', 'cooking_steps', 'cooking_time', 'image', 'author', 'products', 'category']
    template_name = 'myapp/addpage.html'
    # template_name = 'myapp/one_recipe.html'
    success_url = reverse_lazy('index')
    extra_context = {
        'menu': menu,
        'title': 'Редактирование рецепта',
    }

