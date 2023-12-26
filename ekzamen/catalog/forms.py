from django import forms
from django.contrib.auth.forms import UserCreationForm

from .models import User, Zakaz


class SignUpForm(UserCreationForm):
    last_name = forms.CharField(label='Фамилия', widget=forms.TextInput, required=True)
    first_name = forms.CharField(label='Имя', widget=forms.TextInput, required=True)
    username = forms.CharField(label='Логин', widget=forms.TextInput, required=True)
    email = forms.EmailField(label='Email', widget=forms.EmailInput, required=True)
    password1 = forms.CharField(label='Пароль', widget=forms.PasswordInput, required=True)
    password2 = forms.CharField(label='Подтверждение пароля', widget=forms.PasswordInput, required=True)
    photo = forms.ImageField(label='Фото пользователя', widget=forms.FileInput, required=False)

    class Meta:
        model = User
        fields = ('last_name', 'first_name', 'username', 'email', 'password1', 'password2', 'photo')

class ZakazForm(forms.ModelForm):
    class Meta:
        model = Zakaz
        fields = "__all__"
        widgets = {'user': forms.HiddenInput, 'product': forms.HiddenInput}