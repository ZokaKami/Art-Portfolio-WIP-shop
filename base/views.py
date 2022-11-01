from django.shortcuts import render, HttpResponse, HttpResponseRedirect
from django.urls import reverse_lazy, reverse


def index(request):
    return render(request, 'base/index.html')


def portfolio(request):
    return render(request, 'base/portfolio.html')


def about(request):
    return render(request, 'base/about.html')


def shop(request):
    return render(request, 'base/shop.html')
