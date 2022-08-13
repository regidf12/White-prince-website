from django.shortcuts import render


def homepage(request):
    return render(request, 'main/index.html')


def about(request):
    return render(request, 'main/about.html')


def blog(request):
    return render(request, 'main/blog.html')


def contact(request):
    return render(request, 'main/contact.html')