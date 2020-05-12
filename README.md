# project2

Bir Alışveriş Site denemesi

Django öğreniyorum.

Kaynağım

https://www.youtube.com/watch?v=CFbGMFoqS3Y&list=PLIUezwWmVtFUq0RcsaBn8LR_o9R5psLPh

<strong>19. Video'ya geçtim.</strong>

Bir Template parçalayıp programlıyorum.

Django 3 öğreniyorum.

![Localhost görüntüsü](/uploads/local_image.JPG)

2. Aşama Resmi <strong>12. Video</strong>

![Localhost görüntüsü2](/uploads/local_image02.JPG)

3. Aşama Resmi  <strong>13. Video</strong>

![Localhost görüntüsü3](/uploads/local_image03.JPG)

4. Aşama Resmi <strong>15. Video</strong>

![Localhost görüntüsü4](/uploads/local_image04.JPG)

5. Aşama Resmi <strong>16. Video</strong>

![Localhost görüntüsü5](/uploads/local_image05.JPG)

6. #### Aşama Form ile giriş yapma aşamaları 

* a) __Modeli tanımla__
````buildoutcfg
class Comment(models.Model):
    STATUS = (
        ('New', 'Yeni'),
        ('True', 'Evet'),
        ('False', 'Hayır')
    )
    product     = models.ForeignKey(Product,on_delete=models.CASCADE)
    user        = models.ForeignKey(User,on_delete=models.CASCADE)
    subject     = models.CharField(max_length=50, blank=True)
    comment     = models.TextField(max_length=50, blank=True)
    rate        = models.IntegerField(blank=True)
    status      = models.CharField(max_length=10,choices=STATUS,default='New')
    ip          = models.CharField(max_length=20,blank=True)
    create_at   = models.DateTimeField(auto_now_add=True)
    update_at   = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return self.subject
````
* b) __Aynı models.py içinde Form modelini de tanımlıyoruz__
````buildoutcfg
class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['subject', 'comment', 'rate']
````
* c) __Admin panelden yapılan girişler için, formun admin panel tarafını 
uygulamanın admin.py dosyasında kodluyoruz__
````buildoutcfg
from django.contrib import admin
from .models import Category 

class CommentAdmin(admin.ModelAdmin):
    list_display = ('subject', 'comment', 'product', 'user', 'status',)
    list_filter = ('status',)

admin.site.register(Comment,CommentAdmin)
````
* d) __Template içinde;__ 

__Html formunun hemen üstüne form kaydından doğacak
mesajları işleyebilmek için bir kalıbımız var__

Buraya uygulamamızın views.py dosyasındaki fonksiyondan form mesajı geliyor.

Yorumunuz başarıyla gönderildi vb.
````buildoutcfg
    {% if messages %}
        {% for message in messages %}
            <div class="alert alert-{{ message.tags }}" role="alert">
                {{ message }}
            </div>
        {% endfor %}
    {% endif %}
````
* e) __Template içinde Html Formu tanımla__
```Python
<form action="/product/addcomment/{{ product.id }}" method="post" class="review-form">
    {% csrf_token %}
    <div class="form-group">
        <input class="input" type="text" name="subject" id="id_subject" placeholder="Konu" />
    </div>
    <div class="form-group">
        <textarea class="input" name="comment" id="id_comment" placeholder="Yorumunuz"></textarea>
    </div>
    <div class="form-group">
        <div class="input-rating">
            <strong class="text-uppercase">Puanınız: </strong>
            <div class="stars">
                <input type="radio" id="star5" name="rate" value="5" /><label for="star5"></label>
                <input type="radio" id="star4" name="rate" value="4" /><label for="star4"></label>
                <input type="radio" id="star3" name="rate" value="3" /><label for="star3"></label>
                <input type="radio" id="star2" name="rate" value="2" /><label for="star2"></label>
                <input type="radio" id="star1" name="rate" value="1" /><label for="star1"></label>
            </div>
        </div>
    </div>
    {% if user.id is not None %}
        <button class="primary-btn">Yorumu Gönder</button>
    {% else %}
        Yorum eklemek için Giriş yapınız
    {% endif %}
</form>
```
__Form Örneği__
![Form örneği](/uploads/local_image06.JPG)
<hr>
* f) __Uygulamanın urls.py dosyasında path tanımlanır__ 

Bu path tanımını template form'daki action içinde kullandık.
````buildoutcfg
    path('addcomment/<int:id>', views.addcomment, name='addcomment'),
````
* g) __Uygulamanın views.py dosyasında addcomment fonksiyonu tanımlanır.__
````buildoutcfg
from django.contrib.auth.decorators import login_required
from .models import Category, Product, Images, CommentForm, Comment

    @login_reqiured
````
