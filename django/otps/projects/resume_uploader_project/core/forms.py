from django import forms


from .models import Resume


GENDER_CHOICES = (
    ('Male', 'Male'),
    ('Female', 'Female'),
)


JOB_CITIES = (
    ('Delhi', 'Delhi'),
    ('Mumbai', 'Mumbai'),
    ('Goa', 'Goa'),
    ('Chennai', 'Chennai'),
    ('Kolkata', 'Kolkata'),
)


class ResumeForm(forms.ModelForm):
    gender = forms.ChoiceField(widget=forms.RadioSelect, choices=GENDER_CHOICES)
    job_city = forms.MultipleChoiceField(widget=forms.CheckboxSelectMultiple, choices=JOB_CITIES)
    class Meta:
        model = Resume
        fields = ('name', 'dob', 'gender','address', 'state', 'pin', 'mobile', 'job_city', 'profile_img', 'file')

        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'dob': forms.DateInput(attrs={'class': 'form-control', 'id': 'datepicker'}),
            'address': forms.Textarea(attrs={'class': 'form-control', 'rows': 5}),
            'state': forms.Select(attrs={'class': 'form-select'}),
            'pin': forms.NumberInput(attrs={'class': 'form-control'}),
            'mobile': forms.NumberInput(attrs={'class': 'form-control'}),
            'profile_img': forms.ClearableFileInput(attrs={'class': 'form-control'}),
            'file': forms.ClearableFileInput(attrs={'class': 'form-control'}),
        }




