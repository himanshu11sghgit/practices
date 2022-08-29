from django.shortcuts import render


from .models import Image
from .forms import ImageForm

# Create your views here.



def home(request):
    if request.method == 'POST':
        form = ImageForm(data=request.POST, files=request.FILES)
        print(request.POST)
        print(request.FILES)
        if form.is_valid():
            form.save()

    form = ImageForm()
    images = Image.objects.all()
    context = {'form': form, 'images': images}
    return render(request, 'core/home.html', context)