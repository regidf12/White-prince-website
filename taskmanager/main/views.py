from django.core.mail import send_mail, BadHeaderError
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, redirect
from .forms import ContactForm
from taskmanager.settings import RECIPIENTS_EMAIL, DEFAULT_FROM_EMAIL
from django.views.generic import ListView
from . models import Article


def homepage(request):
    return render(request, 'main/index.html')


def about(request):
    return render(request, 'main/about.html')


def blog(request):
    return render(request, 'main/blog.html')


def vedmenkoproduction(request):
    return render(request, 'main/vedmenko.html')


def contact(request):
    if request.method == 'GET':
        form = ContactForm()
    elif request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            subject = form.cleaned_data['name']
            sender = form.cleaned_data['sender']
            message = form.cleaned_data['message']
            try:
                send_mail(subject, f'{message} от {sender}', DEFAULT_FROM_EMAIL, RECIPIENTS_EMAIL)
            except BadHeaderError:
                return HttpResponse('Ошибка в теме письма.')
            return HttpResponseRedirect('contact')
    else:
        return HttpResponse('Неверный запрос.')
    return render(request, 'main/contact.html', {'form': form})


def vedmenkotelegrambot(request):
    return render(request, 'main/vedmenkotelegrambot.html')


def vedmenkovkbot(request):
    return render(request, 'main/vedmenkovkbot.html')


def fearlessvikingz(request):
    return render(request, 'main/fearlessvikingz.html')


def smartassistant(request):
    return render(request, 'main/smartassistant.html')