# project2

echo "# project2" >> README.md

git init

git add README.md

git commit -m "first commit"

git remote add origin https://github.com/serihesap/project2.git

git push -u origin master


git reset --hard HEAD
git push -f origin HEAD^:master

git rm .env --cached
git commit -m "Stopped tracking .env File"

Using your favorite text editor, open the file .git/info/exclude

Add rules to the exclude file as you would the .gitignore file


Üzerinde çalışacağımız proje eğer farklı bir repoda ise, projeyi fork seçeneği ile kendi repomuza çekiyoruz. 

Sonra kendi repomuz üzerinden bağlantısını kopyalayalıyoruz.
Daha sonra makinamızda, projeyi kuracağımız dizinde, git bash ekranını açıyoruz.

(Eğer kendi reponuz üzerinden bir proje yürütmek istiyorsanız, 

Create a new repository seçeneği ile bir repo oluşturup onun bağlantısını kopyalayın.)

$ git clone kopyalanan_link

Proje artık yerel makinamızda olduğuna göre üzerinde çalışmaya başlayabiliriz. 

İlk önce cd proje_adi komutu ile terminalde projenin içine giriyoruz. 

Bu işlemden sonra değişiklikleri kimin yaptığını bildirmek için isim ve mail adresi giriyoruz.

Bunu sadece ilk seferde, ilk kez git kullanıyorken yapıyoruz. 

Daha sonraki işlemlerde bu ayarları yapmamıza gerek yok.

$ git config --global user.name "Cengiz YILMAZ"

$ git config --global user.email "kullanici@gmail.com"

Proje içerisinde farklı klasörlere giriş yapıp farklı dosyalar oluşturabiliriz

 veya olanı silebilir, güncelleme yapmak isteyebiliriz. Bu gibi değişiklikleri yaptıktan sonra, bash ekranına geçelim.

$ git status ile durumumuzu kontrol edelim. Yeni eklenen dosyalar kırmızı renk ile gösterilmektedir.

Şimdi bu dosyaları git’ e ekleyelim.

$ git add index.html şeklinde, sadece bir veya birkaç dosya ekleyebiliriz.

$ git add * ile dosyaların hepsi eklenir.

$ git add . ile (dosya, klasör) yaptığımız tüm değişiklikleri git’e ekliyoruz.

Genelde $ git add . ile tüm değişiklikleri ekleriz. Siz de bu komutu girin.

$ git status ile durumumuza bakalım. Sonradan eklenen dosyalar yeşil renk ile gösterilmektedir.

$ git diff ile de yaptığımız farklılıkları listeleyebiliriz
 (Eğer bu komutu çalıştırdıysanız ctrl+z ile farklılıklar listesinden çıkış yapabilirsiniz).
 
Şimdi commit ile git’e eklediğimiz dosyaları onaylayalım ve yaptığımız değişiklikler için bir mesaj ekleyelim.

$ git commit -a tüm dosyaları commit etmektir.

$ git commit -m "index sayfası değiştirildi" değişikliği mesaj ile ilettik.

$ git commit -am "index değiştirildi" iki işlemi bir arada yapmış olduk. 

İki satır komut girmek yerine tek satır ile iki işlemi yaptık.

Ancak biz bir önceki adımda $ git add . ile tüm değişiklikleri eklediğimiz için 

şimdi $ git commit -m "index sayfası değiştirildi" formatında bir commit mesajı ekleyeceğiz.

Şimdi değişiklikleri GitHub’a gönderelim.

$ git push origin master komutu ile GitHub üzerindeki projenin master dalına değişiklikleri gönderdik.

Origin linki işaret eder. Tekrar link vermemek için kullanılır.

Burada proje bizim kendi repomuza eklenmiş oldu. 

Eğer bu yaptığımız değişiklikleri projenin esas sahibine ulaştırmak istiyorsak, 

GitHub üzerinde pull request seçeneği ile istek atıyoruz 

(Eğer kendi reponuzda çalıştıysanız bu işleme gerek yok. Sizin reponuzda projenin esas sahibi sizsiniz).

Özetle

$ git clone kopyalanan_link

$ git status

$ git add .

$ git commit -m "commit mesajı"

$ git push origin master


Projeyi Güncelleme

Github üzerinde projede değişiklikler olduğunda yerel makinamıza değişiklikleri çekmek için;

$ git pull origin dal_ismi GitHub üzerindeki dalı bizim yereldeki dala merge etmeyi sağlar. 

Güncellemeler olduğunda, yenilikleri elimizdeki projeye dahil etmek için bu komutu kullanırız.

git pull -p uzak sunucudaki değişiklikleri çeker ve yereldeki origin olan branchlari siler.


Dallanma

GitHub üzerindeki bir projeyi farklı bir dala çekmek için,

$ git fetch bu komutla, GitHub’daki değişiklikler farklı bir dala alınır.

$ git merge FETCH_HEAD bizim yereldeki master dalımıza projenin güncel halini ekledik. 

Yereldeki master dalının adı head.

$ git branch mevcut dalları listeler.

$ git branch Yenidal_ismi yeni dal oluşturmak için isim verilir.

$ git checkout Yenidal master dalından Yenidal’a geçtik.

$ git checkout -b Yenidal2_ismi Yeni bir dal oluşturup geçiş yapmayı sağlar.

$ git branch -d Yenidal oluşturulan yeni dalı siler (Yerelde).

$ git branch -dr Yenidal oluşturulan yeni dalı siler (Yerelde ve GitHub’da).

(Silme işlemlerini yaparken master dalında olduğunuzdan emin olun.)

Farklı dallar oluşturup, bu dallarda projeleri farklı yapılandırabliriz. İki farklı dalı birleştirebiliriz.

$ git merge Yenidal ile Yenidal’daki değişiklikler master dalına aktarılıp birleştirildi. 

Yenidal ile ilgili işlem yapılacağı zaman master dalına geçmiş olmamız gerekir. 

Dolayısıyla birleştirme işlemi de master dalındayken yapılır.


Silme

git push origin :silinecek_dal_ismi bu komut sayesinde uzak sunucudaki branch silinir.

git reset --hard HEAD komutu yerelde yapılan değişiklikleri silmek için kulanılır.

Yerelde Proje Oluşturup Github’a Gönderme

Github hesabımızda proje için bir repository oluşturuyoruz. 

Aynı isimle yerelde bir proje klasörü oluşturduktan sonra; terminalde, proje dizininde;

git init komutunu çalıştıralım. Ardından reponun linkini kopyalayıp;

git remote add origin https://github.com/kullanici_adi/repo.git şeklinde repo ile bağlantıyı kuralım.

Projenizdeki değişiklikler için;

git add . && git commit -m "ilk commit" komutunu çalıştırdık.

git push -u origin master komutu ile projeyi repoya gönderdik.

$ git status

$ git add -A   (veya git add all)

$ git commit -m "DjangoProjesi2 canliya alma islemi"

