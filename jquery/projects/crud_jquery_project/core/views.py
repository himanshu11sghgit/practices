from django.shortcuts import render
from django.http import JsonResponse, HttpResponse
from django.core import serializers
from django.forms.models import model_to_dict
import json


from core.models import Student
from core.forms import StudentForm

# Create your views here.



def home(request):
    
    if request.method == 'POST':
        print(request.POST)
        print(type(request.POST))
        form = StudentForm(data=request.POST)
        id = request.POST.get('id')
        if form.is_valid():
                
            name = form.cleaned_data.get('name')
            email = form.cleaned_data.get('email')
            password = form.cleaned_data.get('password')

            if id == '':
                student = Student(name=name, email=email, password=password)
            else:
                student = Student(id=id, name=name, email=email, password=password)

            student.save()

            # convert modal objects into json by using values and list method 
            # students = Student.objects.values()
            # students_list = list(students)

            # convert model objects into json by using core.serializers method
            students = Student.objects.all()
            students_list = serializers.serialize("json", students)
            # print(students_list)
            # print(type(students_list))

            # return HttpResponse(json.dumps({'status': '1', 'students': students_list}), content_type='application/json')
            return JsonResponse({'status': '1', 'students': students_list})
        else:
            return JsonResponse({'status': '0'})


    form = StudentForm()
    students = Student.objects.all()
    context = {
        'form': form,
        'students': students
    }

    return render(request, 'core/home.html', context)


def update(request):
    if request.method == 'POST':
        id = request.POST.get('id')
        try:
            student = Student.objects.get(id=id)

            # convert model instance into json by using core.serializers method
            student_dict = serializers.serialize("json", [student,])
            # print(type(student_dict))
            # print(type(json.dumps(student_dict)))


            # convert model instance into json by using model_to_dict method 
            student_dict = model_to_dict(student)
            return JsonResponse({'status': '1', 'student': student_dict})
        except:
            return JsonResponse({'status': '0'})


def delete(request):
    if request.method == 'POST':
        id = request.POST.get('id')
        try:
            Student.objects.get(id=id).delete()
            return JsonResponse({'status': '1'})
        except:
            return JsonResponse({'status': '0'})