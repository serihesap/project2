from django.http import HttpResponse, Http404
from django.shortcuts import render

from home.models import Setting
from product.models import Category, Product, Images


def index(request):
    setting = Setting.objects.get(pk=1)
    context = {'setting':setting}
    return render(request, 'index.html', context)

def kategoriler(request):
    kategoriler = Category.objects.order_by('-create_at')[:10]
    # kategori_listesi     = ', '.join([q.title for q in kategoriler])
    # return HttpResponse(kategori_listesi)
    context = {
        'kategori_listesi' : kategoriler
    }
    return render(request,'product/index.html',context)

def detay(request, category_id):
    try:
        category = Category.objects.get(pk = category_id)
    except Category.DoesNotExist:
        raise Http404('Bu kategori yok %s ' % category_id)

    return HttpResponse('Bu Kategorinin %s.' % category_id)

def product_detail(request,id,slug):
    # # import json
    # # data_details = {'id' : id, 'slug' : slug}
    # mesaj = "Ürün " , id , "/" , slug
    # return HttpResponse(mesaj) #json.dumps(data_details))
    # # Request olamadan kullanman gerekir. request ile kullaırsak, getir yapıyor.
    category = Category.objects.all()
    product = Product.objects.get(pk=id)
    resimler = Images.objects.filter(product_id=id)
    context = {
        'category':category,
        'product':product,
        'resimler':resimler
    }
    return render(request,"product_detail.html",context)



def sablon2(request, gelenid):
    return HttpResponse('Bu ŞABLON iki %s' % gelenid)

def slayt(request, slug):
    urun = Product.objects.get(slug=slug)
    context={
        'urun':urun
    }
    return render(request,'tekurun.html',context)

