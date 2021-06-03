from django.shortcuts import render, HttpResponse


# Create your views here.
def index(request):
    return render(request, 'index.htm')
    # return HttpResponse("This is Homepage.")


def blog(request):
    return HttpResponse("This is Blog Page.")


def about(request):
    return HttpResponse("This is About Page.")


def contact(request):
    return HttpResponse("This is Contact Page.")
