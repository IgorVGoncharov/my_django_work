from django import forms
import datetime

class UserForm(forms.Form):
    name = forms.CharField(max_length=50,
                           widget=forms.TextInput(attrs={'class': 'form-control',
                                                         'placeholder': 'Введите имя пользователя'}))
    email = forms.EmailField(widget=forms.EmailInput(attrs={'class': 'form-control',
                                                            'placeholder': 'user@mail.ru'}))
    password = forms.CharField(max_length=100,
                               widget=forms.PasswordInput())
    age = forms.IntegerField(min_value=0, max_value=120)
    gender = forms.ChoiceField(choices=[('M', 'Male'), ('F', 'Female')],
                               widget=forms.RadioSelect(attrs={'class': 'form-check-input'}))

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
    message =     forms.CharField(widget=forms.Textarea(attrs={'class': 'form-control'}))

class ImageForm(forms.Form):
    image = forms.ImageField()




