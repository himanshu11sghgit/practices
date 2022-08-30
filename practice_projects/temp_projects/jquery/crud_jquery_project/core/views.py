from django.shortcuts import render
from django.http import JsonResponse
from django.forms.models import model_to_dict


from core.models import Student
from core.forms import StudentForm

# Create your views here.

def home(request):
    form = StudentForm()
    students = Student.objects.all()
    context = {'form': form, 'students': students}
    return render(request, 'core/home.html', context)



def save_data(request):
    if request.method == 'POST':
        form = StudentForm(data=request.POST)
        if form.is_valid():
            id = request.POST.get('id')
            name = form.cleaned_data.get('name')
            email = form.cleaned_data.get('email')
            password = form.cleaned_data.get('password')
            if id == '':
                student = Student(name=name, email=email, password=password)
            else:
                student = Student(id=id, name=name, email=email, password=password)
            student.save()
            students = Student.objects.values()
            students_list = list(students)
            return JsonResponse(data={'status': 200, 'students': students_list})
        else:
            return JsonResponse(data={'status': 400})


def delete_data(request):
    if request.method == 'POST':
        try:
            id = request.POST.get('id')
            Student.objects.get(id=id).delete()
            return JsonResponse(data={'status': 200})
        except: 
            return JsonResponse(data={'status': 400})


def update_data(request):
    if request.method == 'POST':
        try:
            id = request.POST.get('id')
            student = Student.objects.get(id=id)
            student_dict = model_to_dict(student)
    
            return JsonResponse(data={'status': 200, 'student': student_dict})
        except: 
            return JsonResponse(data={'status': 400})