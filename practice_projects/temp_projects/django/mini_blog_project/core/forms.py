from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm, UsernameField
from django.utils.translation import gettext_lazy as _


from .models import Blog


class BlogForm(forms.ModelForm):
    class Meta:
        model = Blog
        fields = ('title', 'description', 'image')
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control', 'id': 'title-id'}),
            'description': forms.Textarea(attrs={'class': 'form-control', 'id': 'description-id'}),
            'image': forms.ClearableFileInput(attrs={'class': 'form-control', 'id': 'image-id'}),
        }


class SignupForm(UserCreationForm):
    password1 = forms.CharField(
        label='Password',
        widget=forms.PasswordInput(attrs={'class': 'form-control', 'id': 'password1-id'}),
    )
    password2 = forms.CharField(
        label='Confirm Password',
        widget=forms.PasswordInput(attrs={'class': 'form-control', 'id': 'password2-id'}),
    )
    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email')
        labels = {
            'username': 'Username',
            'first_name': 'First Name',
            'last_name': 'Last Name',
            'email': 'Email',
        }
        widgets = {
            'username': forms.TextInput(attrs={'class': 'form-control', 'id': 'username-id'}),
            'first_name': forms.TextInput(attrs={'class': 'form-control', 'id': 'firstname-id'}),
            'last_name': forms.TextInput(attrs={'class': 'form-control', 'id': 'lastname-id'}),
            'email': forms.EmailInput(attrs={'class': 'form-control', 'id': 'email-id'}),
        }

    def __init__(self, *args, **kwargs):
        super(SignupForm, self).__init__(*args, **kwargs)

        for fieldname in ['username', 'password1', 'password2']:
            self.fields[fieldname].help_text = None


class LoginForm(AuthenticationForm):
    username = UsernameField(widget=forms.TextInput(attrs={'autofocus': True, 'class': 'form-control', 'id': 'username-id'}))
    password = forms.CharField(
        label=_('Password'),
        strip=False,
        widget=forms.PasswordInput(attrs={'autocomplete': 'current-password', 'class': 'form-control', 'id': 'password-id'}),
    )
