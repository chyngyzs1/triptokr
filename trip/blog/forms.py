from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms 
from .models import Review
from phonenumber_field.modelfields import PhoneNumberField

from django.forms import ModelForm


class CreateUserForm(UserCreationForm):
    username = forms.CharField(max_length=40, label='User Name: ')
    email = forms.EmailField()
    phone = forms.CharField(max_length=20)
    first_name = forms.CharField(max_length=30)
    last_name = forms.CharField(max_length=30)

    class Meta:
        model = User

        fields = ('username', 'email', 'phone', 'first_name', 'last_name', 'password1', 'password2')


class ReviewForm(forms.ModelForm):
    class Meta:
        model = Review
        fields = ('full_name', 'email', 'text')

        widgets = {
            'full_name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Full Name'}),
            'email': forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'Email'}),
            'text': forms.TextInput(attrs={'class': 'form-control','placeholder': 'Review'}),
        }