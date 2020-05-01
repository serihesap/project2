from django.shortcuts import render

from .models import Setting

setting = Setting.objects.get(pk=1)

def index(request):
    # metin = 'Ali'
    # return HttpResponse('Merhaba %s' % metin)
    context = {'setting':setting,'page':'home'}
    return render(request, 'index.html', context)

def hakkimizda(request):
    context = {'setting':setting}
    return render (request,'hakkimizda.html',context)

def referanslar(request):
    context = {'setting': setting}
    return render(request,'referanslar.html',context)

def iletisim(request):
    context = {'setting': setting}
    return render(request,'iletisim.html',context)


