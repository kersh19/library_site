from django import forms
from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User
from django.db.models import Count

from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
# Create your views here.
from django.template import context
from django.urls import reverse
from django.views.generic import TemplateView, ListView
from django.http import HttpResponse
from .models import News, Poln_text, Exhibition_tema, Kontakt, Date, Exh_nov_iz, Tags
from django import views
from django.urls import reverse_lazy
from django.http import HttpResponse
def news(request):
    new = News.objects.all()
    context = {
        'news': new,
    }
    return render(request, 'website/base.html', context=context)


def base_abi(request):

    n_abil = News.objects.all()
    context = {
        'news_abil': n_abil,
    }
    return render(request, 'website/abil.html', context=context)


def prep(request):
    vebinar = Poln_text.objects.all()
    context = {
        'vebinars': vebinar,
    }
    return render(request, 'website/prepod.html', context=context)
def student(request):
    return render(request, 'website/student.html')
def exhibition(request):  # выставки
    exhibition = Exhibition_tema.objects.all().order_by('-id')
    context = {
        'exhibitions': exhibition,
    }
    return render(request, 'website/exhibitions.html', context=context)
def nov_iz(request):
    exh = Exh_nov_iz.objects.values('category').annotate(dcount = Count('category'))
    exhibition = Exh_nov_iz.objects.all()
    category = Tags.objects.all()
    context = {
        'exhs': exh,
        'exhibitions': exhibition,
        'categorys':category,
    }
    return render(request, 'website/nov_iz.html', context=context)
def o_bibl(request):  # если ничего из бд не берется, то так показываем страницу
    return render(request, 'website/biblioteka.html')
def kontakt(request):
    kontakt = Kontakt.objects.all()
    context = {
        'kontakts': kontakt
    }
    return render(request, 'website/kontakt.html', context=context)
def base(request):
    new = News.objects.all()
    vebinar = Poln_text.objects.all()
    dr = Date.objects.values('dat').annotate(dcount = Count('dat'))
    date = Date.objects.all()
    context = {
        'drs':dr,
        'news': new,
        'vebinars': vebinar,
        'dates': date,
    }
    return render(request, 'website/base.html', context=context)
def date(request, date_id):
    date = get_object_or_404(Date, id=date_id)
    return render(request, 'website/Dates.html', {'date': date})
def historypr(request):
    return render(request, 'website/historypr.html')
def historynas(request):
    return render(request, 'website/historynas.html')
def polozh(request):
    return render(request, 'website/polozhenia.html')