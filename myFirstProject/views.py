from django.shortcuts import render, HttpResponse

# Create your views here.

def index(request):
    return HttpResponse("<h1>Hello World!</h1>")

def second_page(request):
    return render(request, 'second_page.html')

def third_page(request):
    return render(request, 'third_page.html')

def fourth_page(request):
    return render(request, 'fourth_page.html')

def fifth_page(request):
    return render(request, 'fifth_page.html')

def sixth_page(request):
    return render(request, 'sixth_page.html')
