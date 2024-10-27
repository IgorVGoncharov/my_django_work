from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, redirect



from django.contrib.auth.views import LoginView
from django.urls import reverse_lazy
# from .forms import LoginForm


# class CustomLoginView(LoginView):
#     authentication_form = LoginForm
#     template_name = 'user_app/login.html'
#     extra_context = {'title': 'Авторизация на сайте'}
#
#     def get_success_url(self):
#         return reverse_lazy('blog:index')

def registration(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            # получаем имя пользователя и пароль из формы
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password1')
            # выполняем аутентификацию
            user = authenticate(username=username, password=password)
            login(request, user)
            return redirect('/')
    else:
        form = UserCreationForm()
    return render(request, 'signup.html', {'form': form})

