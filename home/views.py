from django.shortcuts import render

from .models import Setting


def index(request):
    # metin = 'Ali'
    # return HttpResponse('Merhaba %s' % metin)
    setting = Setting.objects.get(pk=1)

    context = {'setting':setting}
    return render(request, 'index.html', context)

