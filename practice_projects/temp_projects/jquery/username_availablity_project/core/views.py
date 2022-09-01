from django.shortcuts import render

from django.http import JsonResponse


from .models import Username

# Create your views here.



def home(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        if Username.objects.filter(name=name).exists():
            status = 0
        else:
            status = 1
        return JsonResponse({'status': status})
    return render(request, 'core/home.html')