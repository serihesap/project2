from django.contrib import messages
from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import render

from product.models import Product, Category
from .models import Setting, Contact, ContactForm

setting = Setting.objects.get(pk=1)

def index(request):
    # metin = 'Ali'
    # return HttpResponse('Merhaba %s' % metin)
    category = Category.objects.all()
    sliderdata=Product.objects.all()[:4]
    dayproducts = Product.objects.all()[:3]
    lastproducts = Product.objects.all().order_by('-id')[:4]
    randomproducts = Product.objects.all().order_by('?')[:4]
    context = {'setting':setting,
               'page':'home',
               'sliderdata':sliderdata,
               'category':category,
               'dayproducts':dayproducts,
               'lastproducts':lastproducts,
               'randomproducts':randomproducts
               }
    return render(request, 'index.html', context)

def hakkimizda(request):
    context = {'setting':setting}
    return render (request,'hakkimizda.html',context)

def referanslar(request):
    context = {'setting': setting}
    return render(request,'referanslar.html',context)

def iletisim(request):

    if request.method == 'POST': # Form post edildiyse
        form = ContactForm(request.POST) # form post edildiyse
        if form.is_valid():
            data = Contact() # model ile bağlantı kur
            data.name    = form.cleaned_data['name'] # formdan bilgiyi al
            data.email   = form.cleaned_data['email']
            data.subject = form.cleaned_data['subject']
            data.message = form.cleaned_data['message']
            data.ip      = request.META.get('REMOTE_ADDR')
            data.save()
            messages.success(request,'Mesajınız için teşekkür ederiz.')
            return HttpResponseRedirect('/iletisim')

    form = ContactForm() # form ile bağlantı kur
    context = {'setting': setting,'form':form}
    return render(request,'iletisim.html',context)


def category_products(request,id,slug) :
    category = Category.objects.all()
    products = Product.objects.filter(category_id=id)
    categorydata = Category.objects.get(pk=id) # yol için
    context={
        'products': products,
        'category': category,
        'categorydata' : categorydata
    }
    return render(request,'products.html',context)