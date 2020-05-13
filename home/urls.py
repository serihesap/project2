from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='home'),
    path('hakkimizda/', views.hakkimizda, name='hakkimizda'),
    path('referanslar/', views.referanslar, name='referanslar'),
    path('iletisim/', views.iletisim, name='iletisim'),
    path('category/<int:id>/<slug:slug>', views.category_products, name='category_products'),
    path('ara/', views.products_search, name='products_search'),
]