import logging
from django.core.files.storage import FileSystemStorage
from django.views import View
from django.http import HttpResponse, JsonResponse
from django.views.generic import TemplateView
from django.shortcuts import render, get_object_or_404
from .models import Author, Post, User
from .forms import ImageForm

from .forms import UserForm, ManyFieldsForm



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