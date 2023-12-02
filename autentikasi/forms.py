from django import forms
from django.contrib.auth import get_user_model, authenticate
import re

User = get_user_model()

class RegisterForm(forms.Form):
    username = forms.CharField(label='Username', widget=forms.TextInput(attrs={
        'class': 'form-control',
        'placeholder': 'Username',
        'required': True,
    }))
    email = forms.EmailField(label='Email', widget=forms.EmailInput(attrs={
        'class': 'form-control',
        'placeholder': 'Email address',
        'required': True,
    }))
    address = forms.CharField(label='Address', widget=forms.TextInput(attrs={
        'class': 'form-control',
        'placeholder': 'Home address',
        'required': True,
    }))
    phone = forms.CharField(label='Phone Number', widget=forms.TextInput(attrs={
        'class': 'form-control',
        'placeholder': '+628123456789',
        'required': True,
    }))
    password_first = forms.CharField(label="Password", widget=forms.PasswordInput(attrs={
        'class': 'form-control',
        'placeholder': 'Password',
        'required': True,
    }))
    password_again = forms.CharField(label="Confirm password", widget=forms.PasswordInput(attrs={
        'class': 'form-control',
        'placeholder': 'Confirm your password',
        'required': True,
    }))

    def clean(self):
        cleaned_data = self.cleaned_data
        password_one = self.cleaned_data.get('password_first')
        password_two = self.cleaned_data.get('password_again')
        if password_one != password_two:
            raise forms.ValidationError("Passwords don't match")
        return cleaned_data

    def clean_username(self):
        username = self.cleaned_data.get('username')
        qs = User.objects.filter(username=username)
        if qs.exists():
            raise forms.ValidationError("The username you've chosen is unavailable.")
        return username

    def clean_email(self):
        email_address = self.cleaned_data.get('email')
        qs = User.objects.filter(email=email_address)
        if qs.exists():
            raise forms.ValidationError("The email address you've chosen is already registered.")
        return email_address

    def clean_phone(self):
        phone_pattern = re.compile(r'^\+\d{10,15}$')
        phone_number = self.cleaned_data.get('phone')
        if not phone_pattern.match(phone_number):
            raise forms.ValidationError("Phone number must be entered in the format: '+999999999'. 10-15 digits is allowed.")
        return phone_number

class LoginForm(forms.Form):
    username = forms.CharField(label='Username', widget=forms.TextInput(attrs={
        'class': 'form-control',
        'placeholder': 'Username',
        'required': True,
    }))
    password = forms.CharField(label='Password', widget=forms.PasswordInput(attrs={
        'class': 'form-control',
        'placeholder': 'Password',
        'required': True,
    }))
    
    def clean(self):
        cleaned_data = self.cleaned_data
        username = self.cleaned_data.get('username')
        password = self.cleaned_data.get('password')
        qs = User.objects.filter(username=username)
        user = authenticate(username=username, password=password)
        print(user)
        if not qs.exists():
            raise forms.ValidationError("The username you entered isn't connected to an account")
        elif user is None:
            raise forms.ValidationError("Wrong password!")
        return cleaned_data
        