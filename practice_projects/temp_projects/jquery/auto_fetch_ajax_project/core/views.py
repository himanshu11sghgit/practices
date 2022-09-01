from django.shortcuts import render
from django.http import HttpResponse, JsonResponse


import json


from .models import Tweet
from .forms import TweetForm
from .serializers import TweetSerializer

# Create your views here.


def home(request):
    if request.method == 'POST':
        form = TweetForm(data=request.POST)
        if form.is_valid():
            form.save()
            return JsonResponse({'msg': 'tweet saved successfully'})

    else:
        form = TweetForm()

    context = {'form': form}
    return render(request, 'core/home.html', context)



def get_data(request):
    if request.method == 'POST':
        tweets = Tweet.objects.all()
        serializer = TweetSerializer(tweets, many=True)
        return JsonResponse(serializer.data, safe=False)