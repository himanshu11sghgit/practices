from django import forms


from .models import Image



class ImageForm(forms.ModelForm):
    class Meta:
        model = Image
        fields = ('img',)
        labels = {
            'img': 'Photo'
        }
        widgets = {
            'img': forms.ClearableFileInput(attrs={'class': 'form-control', 'id': 'photo-id'})
        }