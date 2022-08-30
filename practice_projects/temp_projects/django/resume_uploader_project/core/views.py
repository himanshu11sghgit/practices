from django.shortcuts import render, redirect



from .models import Resume
from .forms import ResumeForm




# Create your views here.



def home(request):
    if request.method == 'POST':
        form = ResumeForm(data=request.POST, files=request.FILES)
        if form.is_valid():
            form.save()
            form = ResumeForm()
    else:
        form = ResumeForm()

    resumes = Resume.objects.all()
    context = {'form': form, 'resumes': resumes}
    return render(request, 'core/home.html', context)



def view_data(request, id):
    resume = Resume.objects.get(id=id)
    context = {'resume': resume}
    return render(request, 'core/view.html', context)


def delete_data(request, id):
    Resume.objects.get(id=id).delete()
    return redirect('/')


