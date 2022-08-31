from django.shortcuts import render, redirect


from .models import Student
from .forms import StudentForm

# Create your views here.


def home(request):
    if request.method == 'POST':
        form = StudentForm(data=request.POST)
        if form.is_valid():
            form.save()
            form = StudentForm()
    else:
        form = StudentForm()
    students = Student.objects.all()
    context = {
        'form': form,
        'students': students
    }
    return render(request, 'core/home.html', context)


def update_data(request, id):
    student = Student.objects.get(id=id)
    if request.method == 'POST':
        form = StudentForm(data=request.POST, instance=student)
        if form.is_valid():
            form.save()
            return redirect('/')
    else:
        form = StudentForm(instance=student)
    context = {'form': form}
    return render(request, 'core/update.html', context)


def delete_data(request, id):
    Student.objects.get(id=id).delete()
    return redirect('/')
