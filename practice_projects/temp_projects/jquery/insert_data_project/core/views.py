from django.shortcuts import render
from django.http import JsonResponse


from .models import Student

# Create your views here.



def home(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        password = request.POST.get('password')
        try:
            student = Student(name=name, email=email, password=password)
            student.save()
            msg = "Data is saved successfully!!"
        except:
            msg = "Data is failed to save!!"
        return JsonResponse({'msg': msg})

    return render(request, 'core/home.html')