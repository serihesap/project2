from django.contrib import admin

# Register your models here.
from .models import Category, Product, Images


class CategoryYonet(admin.ModelAdmin):
    list_display = ('parent','title','image_tag','slug')
    list_filter = ('slug','create_at')


class ProductImageInline(admin.TabularInline):
    model = Images
    extra = 2


class ProductAdmin(admin.ModelAdmin) :
    list_display = ('title','category','price','amount','image_tag','status')
    list_filter = ('status','category')

    inlines = [ProductImageInline]


class ImagesAdmin(admin.ModelAdmin):
    list_display = ('title','image_tag')


admin.site.register(Category,CategoryYonet)
admin.site.register(Product, ProductAdmin)
admin.site.register(Images,ImagesAdmin)
