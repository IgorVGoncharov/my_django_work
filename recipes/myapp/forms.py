from django import forms
import datetime
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.contrib.auth.forms import AuthenticationForm
from django.core.exceptions import ValidationError
from .models import Recipes_category, Recipes



    # def clean_name(self):
    #     """Плохой пример. Подмена параметра min_length."""
    #     name = self.cleaned_data['name']
    #     if len(name) < 3:
    #         raise forms.ValidationError('Имя должно содержать не менее 3 символов')
    #     return name
    #
    # def clean_email(self):
    #     email: str = self.cleaned_data['email']
    #
    #     if not (email.endswith('vk.team') or email.endswith('corp.mail.ru')):
    #         raise forms.ValidationError('Используйте корпоративную почту')
    #     return email


class ManyFieldsForm(forms.Form):
    name = forms.CharField(max_length=50,
                           widget=forms.TextInput(attrs={'class': 'form-control',
                                                         'placeholder': 'Введите имя пользователя'}))
    email = forms.EmailField(widget=forms.EmailInput(attrs={'class': 'form-control',
                                                            'placeholder': 'user@mail.ru'}))
    age = forms.IntegerField(min_value=18)
    height = forms.FloatField()
    is_active = forms.BooleanField(required=False)
    birthdate = forms.DateField(initial=datetime.date.today,
                                widget=forms.DateInput(attrs={'class': 'form-control',
                                                              'type': 'date'}))
    gender = forms.ChoiceField(choices=[('M', 'Male'), ('F', 'Female')],
                               widget=forms.RadioSelect(attrs={'class': 'form-check-input'}))
    message = forms.CharField(widget=forms.Textarea(attrs={'class': 'form-control'}))

class ImageForm(forms.Form):
    image = forms.ImageField()


# Готово

class RecipesCategoryForm(forms.Form): # Готово
    # Форма добавления категорий рецептов
    category_name = forms.CharField(max_length=100,
                           widget=forms.TextInput(attrs={'class': 'form-control',
                                                         'placeholder': 'Введите категорию рецепта'}))
    category_description = forms.CharField(widget=forms.Textarea(attrs={'class': 'form-control'}))
    image = forms.ImageField()

class UserForm(forms.Form):#+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++#
    # Форма добавления пользователя
    name = forms.CharField(min_length=3, max_length=50,
                           widget=forms.TextInput(attrs={'class': 'form-control',
                                                         'placeholder': 'Введите имя пользователя'}))
    email = forms.EmailField(widget=forms.EmailInput(attrs={'class': 'form-control',
                                                            'placeholder': 'user@mail.ru'}))
    password = forms.CharField(max_length=100,
                               widget=forms.PasswordInput())
    age = forms.IntegerField(min_value=0, max_value=120)
    gender = forms.ChoiceField(choices=[('M', 'Male'), ('F', 'Female')],
                               widget=forms.RadioSelect(attrs={'class': 'form-check-input'}))





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


class LoginForm(AuthenticationForm):
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

# class LetTryForm(forms.Form):
#     name = forms.CharField(min_length=3, max_length=50, label="Название рецепта",
#                            widget=forms.TextInput(attrs={'class': 'form-control',
#                                                          'placeholder': 'Введите название рецепта'}))

# class AddRecipeForm(forms.ModelForm):
#     category = forms.ModelChoiceField(queryset=Recipes_category.objects.all(), empty_label="Категория не выбрана: ",
#                                       label="Категории рецептов")
#
#     class Meta:
#         model = Recipes
#         fields = ['name', 'description', 'cooking_steps', 'cooking_time', 'image', 'author', 'products', 'category']
#         widgets = {
#             'name': forms.TextInput(attrs={'class': 'form-input', 'placeholder': 'Введите название рецепта'}),
#             'description': forms.Textarea(attrs={'cols': 50, 'rows': 5, 'placeholder': 'Введите описание рецепта'}),
#             'cooking_steps': forms.Textarea(attrs={'placeholder': 'Опишите шаги приготовления'}),
#             'cooking_time': forms.TextInput(attrs={'placeholder': 'Введите время приготовления'}),
#             'author': forms.TextInput(attrs={'placeholder': 'Введите имя автора'}),
#             'products': forms.Textarea(attrs={'placeholder': 'Распишите используемые продукты'}),
#         }
#         labels = {'slug': 'URL',
#                   'name': 'Название рецепта',
#                   'description': 'Описание рецепта',
#                   'cooking_steps': 'Шаги приготовления',
#                   'cooking_time': 'Время приготовления',
#                   'image': 'Картинка',
#                   'author': 'Имя автора',
#                   'products': ' Используемые продукты',
#                   }
#
#     def clean_title(self):
#         title = self.cleaned_data['name']
#         if len(title) > 50:
#             raise ValidationError("Длина превышает 50 символов")
#
#         return title
#

class RecipeForm(forms.Form):
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

