from django.shortcuts import render


def homepage(request):
    return render(request, 'main/index.html')


def about(request):
    return render(request, 'main/about.html')


def blog(request):
    return render(request, 'main/blog.html')


def contact(request):
    return render(request, 'main/contact.html')


def vedmenkoproduction(request):
    return render(request, 'main/vedmenko.html')


def vedmenkotelegrambot(request):
    return render(request, 'main/vedmenkotelegrambot.html')


def vedmenkovkbot(request):
    return render(request, 'main/vedmenkovkbot.html')


def fearlessvikingz(request):
    return render(request, 'main/fearlessvikingz.html')


def smartassistant(request):
    return render(request, 'main/smartassistant.html')