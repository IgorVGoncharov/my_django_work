from django import forms
import datetime
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.contrib.auth.forms import AuthenticationForm



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


class RecipeForm(forms.Form):
    name = forms.CharField(min_length=3, max_length=50,
                           widget=forms.TextInput(attrs={'class': 'form-control',
                                                         'placeholder': 'Введите название рецепта'}))
    description = forms.CharField(widget=forms.Textarea(attrs={'class': 'form-control'}))
    cooking_steps = forms.CharField(widget=forms.Textarea(attrs={'class': 'form-control'}))
    cooking_time = forms.TimeField(widget=forms.TimeInput(attrs={'class': 'form-control', 'type': 'time'}))
    image = forms.ImageField()
    author = forms.CharField(max_length=100,
                             widget=forms.TextInput(attrs={'class': 'form-control',
                                                                  'placeholder': 'Введите имя автора'}))
    products = forms.CharField(widget=forms.Textarea(attrs={'class': 'form-control'}))


class SignUpForm(UserCreationForm): #Готово+++++++++++++++++++++++++++++++++++
    """Форма регистрации нового пользователя"""
    age = forms.IntegerField(min_value=0, max_value=120, label='Возраст')
    email = forms.EmailField(widget=forms.EmailInput(attrs={'class': 'form-control',
                                                            'placeholder': 'user@mail.ru'}))
    gender = forms.ChoiceField(choices=[('M', 'Male'), ('F', 'Female')], label='Пол',
                               widget=forms.RadioSelect(attrs={'class': 'form-check-input'}))
    password1 = forms.CharField(
        label='Пароль',
        strip=False,
        widget=forms.PasswordInput(attrs={"autocomplete": "new-password"}),
        help_text='Введите пароль',
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