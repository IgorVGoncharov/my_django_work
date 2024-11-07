from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.contrib.auth.forms import AuthenticationForm
from .models import Recipes_category

class LoginForm(AuthenticationForm):
    """Форма авторизации"""
    username = forms.CharField(
        max_length=150,
        label='Имя пользователя',
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            'placeholder': 'Введите имя пользователя'
        })
    )
    password = forms.CharField(
        max_length=128,
        label='Пароль',
        widget=forms.PasswordInput(attrs={
            'class': 'form-control',
            'placeholder': 'Введите пароль'
        })
    )

    class Meta:
        model = User
        fields = ['username', 'password']

class SignUpForm(UserCreationForm):
    """Форма регистрации нового пользователя"""
    username = forms.CharField(label="Имя пользователя", widget=forms.Textarea(attrs={'class': 'form-input',
    'placeholder': 'Обязательное поле. Не более 150 символов. Только буквы, цифры и символы @/./+/-/_.',
                                                            'cols': 50, 'rows': 2}))
    age = forms.IntegerField(min_value=0, max_value=120, label="Возраст",
                             widget=forms.TextInput(attrs={'class': 'form-input',
    'placeholder': 'Введите возраст от 1 до 99'}))
    email = forms.EmailField(label="E-mail", widget=forms.EmailInput(attrs={'class': 'form-control',
                                                            'placeholder': 'Пример: user@mail.ru'}))
    gender = forms.ChoiceField(choices=[('M', 'Male'), ('F', 'Female')], label='Пол',
                               widget=forms.RadioSelect(attrs={'class': 'form-check-input',
                                                               'placeholder': 'Введите возраст'}))
    password1 = forms.CharField(
        label='Пароль',
        strip=False,
        widget=forms.PasswordInput(attrs={"autocomplete": "new-password", 'placeholder': 'Введите пароль'}),
    )
    password2 = forms.CharField(
        label='Подтверждение пароля',
        strip=False,
        widget=forms.PasswordInput(attrs={"autocomplete": "new-password",
                                          'placeholder': 'Для подтверждения введите, пожалуйста, пароль ещё раз.'}),
    )

    class Meta:
        model = User
        fields = ('username', 'email', 'age', 'gender', 'password1', 'password2',)

class RecipeForm(forms.Form):
    """Форма рецепта"""
    name = forms.CharField(min_length=3, max_length=50, label="Название рецепта",
                           widget=forms.TextInput(attrs={'class': 'form-control',
                                                         'placeholder': 'Введите название рецепта'}))
    description = forms.CharField(label="Описание рецепта",
                                  widget=forms.Textarea(attrs={'class': 'form-control',
                                                               'placeholder': 'Введите описание рецепта'}))
    cooking_steps = forms.CharField(label="Шаги приготовления",
                                    widget=forms.Textarea(attrs={'class': 'form-control',
                                                                 'placeholder': 'Опишите шаги приготовления'}))
    cooking_time = forms.IntegerField(label="Время приготовления",
                                      widget=forms.TextInput(attrs={'class': 'form-control',
                                                                    'placeholder': 'Введите время приготовления'}))
    image = forms.ImageField(label="Картинка")
    author = forms.CharField(max_length=100, label="Автор",
                             widget=forms.TextInput(attrs={'class': 'form-control',
                                                                  'placeholder': 'Введите имя автора'}))
    products = forms.CharField(label="Используемые продукты",
                               widget=forms.Textarea(attrs={'class': 'form-control',
                                                            'placeholder': 'Распишите используемые продукты'}))
    category = forms.ModelChoiceField(queryset=Recipes_category.objects.all(), empty_label="Категория не выбрана: ",
                                          label="Категории рецептов")
