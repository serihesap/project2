from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse, Http404, HttpResponseRedirect
from django.shortcuts import render

from home.models import Setting
from .models import Category, Product, Images, CommentForm, Comment


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
    comments = Comment.objects.filter(product_id=id, status='True') # Onaylanan yorumları çekiyoruz.
    context = {
        'category':category,
        'product':product,
        'resimler':resimler,
        'comments':comments
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

@login_required(login_url='/login') # Şu anda tanımlı değil. Bu sayede oturum açmadan yorum yapılamyor
def addcomment(request,id):

    url = request.META.get('HTTP_REFERER')  # yorum sayfasına geri dönmek için son url'yi aldık.

    if request.method == 'POST': # form post edildiyse
        form = CommentForm(request.POST) # Modelde tanımlı olan form tanımına göre verileri çek.
        if form.is_valid():
            current_user    = request.user # Session'daki Kullanıcı bilgilerine erişim

            data            = Comment() # model ile bağlantı kuruluyor
            data.user_id    = current_user.id
            data.product_id = id
            data.subject    = form.cleaned_data['subject']
            data.comment    = form.cleaned_data['comment']
            data.rate       = form.cleaned_data['rate']
            data.ip         = request.META.get('REMOTE_ADDR') # Client bilgisayarın IP'si
            data.save() # Veritabanına kaydet

            messages.success(request,'Yorumunuz başarı ile gönderilmiştir. Teşekkürler')

            return HttpResponseRedirect(url)

        messages.warning(request, 'Yorumunuz kaydedilemedi. lütfen  kontrol ediniz.')
        return HttpResponseRedirect(url)


