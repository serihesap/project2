from django.contrib import admin

# Register your models here.
from mptt.admin import DraggableMPTTAdmin

from .models import Category, Product, Images


class CategoryAdmin(DraggableMPTTAdmin):
    mptt_indent_field = "title"
    list_display = ('tree_actions', 'indented_title','image_tag',
                    'related_products_count', 'related_products_cumulative_count')
    list_display_links = ('indented_title',)
    list_filter = ('slug', 'create_at')
    prepopulated_fields = {'slug' : ('title',)}  # slug alanını make ve model alanından oluşturur.

    def get_queryset(self, request):
        qs = super().get_queryset(request)

        # Add cumulative product count
        qs = Category.objects.add_related_count(
                qs,
                Product,
                'category',
                'products_cumulative_count',
                cumulative=True)

        # Add non cumulative product count
        qs = Category.objects.add_related_count(qs,
                 Product,
                 'category',
                 'products_count',
                 cumulative=False)
        return qs

    def related_products_count(self, instance):
        return instance.products_count
    related_products_count.short_description = 'İlgili ürünler (Bu kategori için)'

    def related_products_cumulative_count(self, instance):
        return instance.products_cumulative_count
    related_products_cumulative_count.short_description = 'İlgili ürünler (Ağaçta)'



class ProductImageInline(admin.TabularInline):
    model = Images
    extra = 2


class ProductAdmin(admin.ModelAdmin) :
    list_display = ('title','category','price','amount','image_tag','status')
    list_filter = ('status','category')
    prepopulated_fields = {'slug' : ('title',)}  # slug alanını make ve model alanından oluşturur.

    inlines = [ProductImageInline]


class ImagesAdmin(admin.ModelAdmin):
    list_display = ('title','image_tag')


admin.site.register(Category,CategoryAdmin)
admin.site.register(Product, ProductAdmin)
admin.site.register(Images,ImagesAdmin)
