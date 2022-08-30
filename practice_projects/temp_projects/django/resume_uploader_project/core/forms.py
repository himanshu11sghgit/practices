from django import forms



from .models import Resume


GENDER_CHOICES = (
    ('Male', 'Male'),
    ('Female', 'Female')
)

JOB_CITIES = (
    ('Delhi', 'Delhi'),
    ('Goa', 'Goa'),
    ('Mumbai', 'Mumbai'),
    ('Chennai', 'Chennai')
)



class ResumeForm(forms.ModelForm):
    gender = forms.ChoiceField(choices=GENDER_CHOICES, widget=forms.RadioSelect)
    job_city = forms.MultipleChoiceField(choices=JOB_CITIES, widget=forms.CheckboxSelectMultiple)
    class Meta:
        model = Resume
        fields = ('name', 'dob', 'gender', 'locality', 'pin', 'city', 'state', 'mobile', 'email', 'job_city', 'image', 'file')
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'dob': forms.DateInput(attrs={'class': 'form-control', 'id': 'datepicker'}),
            'locality': forms.TextInput(attrs={'class': 'form-control'}),
            'pin': forms.NumberInput(attrs={'class': 'form-control'}),
            'city': forms.TextInput(attrs={'class': 'form-control'}),
            'state': forms.Select(attrs={'class': 'form-select'}),
            'mobile': forms.NumberInput(attrs={'class': 'form-control'}),
            'email': forms.EmailInput(attrs={'class': 'form-control'}),
            'image': forms.ClearableFileInput(attrs={'class': 'form-control'}),
            'file': forms.ClearableFileInput(attrs={'class': 'form-control'}),
        }
