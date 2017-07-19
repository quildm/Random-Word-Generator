from django.shortcuts import render, HttpResponse, redirect
from django.utils.crypto import get_random_string

# Create your views here.
# def index(request):
#     response = "Hello, I am your first request!"
#     return HttpResponse(response)



def index(request):
    response = {
        "string": get_random_string(length=14)
    }
    # request.session['chips'] = 0
    # request.session['chips'] = request.session['chips'] + 1

    if 'chips' not in request.session:
        request.session['chips'] = 0
    else:
        request.session['chips'] = request.session['chips'] +1

    return render(request, "random_word/index.html", response)
