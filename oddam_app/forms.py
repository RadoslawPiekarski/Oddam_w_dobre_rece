from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class CreateUserForm(forms.Form):
    # username = forms.CharField(max_length=20, label="E-mail", widget=forms.TextInput(attrs={'placeholder': 'Login'}))
    email = forms.EmailField(max_length=50, label="E-mail", widget=forms.TextInput(attrs={'placeholder': 'Email'}))
    password = forms.CharField(max_length=20, label="Hasło", widget=forms.PasswordInput(render_value=False, attrs={'placeholder': 'Hasło'}))
    password2 = forms.CharField(max_length=20, label="Powtórz hasło", widget=forms.PasswordInput(render_value=False, attrs={'placeholder': 'Powtórz hasło'}))
    firstname = forms.CharField(max_length=20, label="Imię", widget=forms.TextInput(attrs={'placeholder': 'Imię'}))
    lastname = forms.CharField(max_length=50, label="Nazwisko", widget=forms.TextInput(attrs={'placeholder': 'Nazwisko'}))

