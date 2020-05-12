from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='product'),
    path('<slug:slug>/', views.slayt, name='slayt'),
    path('kategori/', views.kategoriler, name='kategori'),
    path('<int:category_id>/', views.detay, name='detay'),
    path('<int:id>/<slug:slug>/', views.product_detail, name='product_detail'),
    path('<int:gelenid>/sablon/', views.sablon2, name='sablon')
]