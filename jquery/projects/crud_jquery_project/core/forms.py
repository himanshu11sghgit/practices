from django import forms

from core.models import Student


class StudentForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = ('name', 'email', 'password')
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control', 'id': 'name-id'}),
            'email': forms.EmailInput(attrs={'class': 'form-control', 'id': 'email-id'}),
            'password': forms.PasswordInput(attrs={'class': 'form-control', 'id': 'password-id'}),
        }