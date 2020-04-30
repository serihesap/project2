from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='product'),
    path('kategori/', views.kategoriler, name='kategori'),
    path('<int:category_id>/', views.detay, name='detay'),
    path('<int:gelenid>/sablon/', views.sablon2, name='sablon'),
]