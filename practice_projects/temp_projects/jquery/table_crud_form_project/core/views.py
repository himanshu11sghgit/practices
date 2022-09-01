from django.shortcuts import render
from django.http import JsonResponse
from django.core import serializers

from .models import Student



# Create your views here.



def home(request):
    return render(request, 'core/home.html')


def add_data(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')

        student = Student(name=name, email=email)
        student.save()
        return JsonResponse({'msg': 'data saved successfully'})
    

def get_data(request):
    if request.method == 'POST':
        students = Student.objects.all()
        serializer = serializers.serialize("json", list(students))
        print(serializer)
        return JsonResponse({'students': serializer}, safe=False)