from django.shortcuts import render

# from PyDictionary import PyDictionary

# Create your views here.



def home(request):
    if request.method == "POST":
        word = request.POST.get("word")
        # meaning = PyDictionary().meaning(word)
        context = {"word": word}
    else:
        context = {}
    return render(request, "core/home.html", context)


# def word(request):
#     context = {}
#     return render(request, "core/word.html", context)