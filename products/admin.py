from django.contrib import admin
from django.utils.html import format_html
from jalali_date import date2jalali
from django.urls import reverse
from django.utils.translation import gettext as _
from mptt.admin import MPTTModelAdmin
from .models import *

class PriceRangeFilter(admin.SimpleListFilter):
    title = _('Price Range')
    parameter_name = 'price_range'

    def lookups(self, request, model_admin):
        return (
            ('0-100000', _('0 - 100,000')),
            ('100001-500000', _('100,000 - 500,000')),
            ('500001-1000000', _('500,000 - 1,000,000')),
            ('1000001-2000000', _('1,000,000 - 2,000,000')),
            ('2000001-5000000', _('2,000,000 - 5,000,000')),
            ('5000001-10000000', _('5,000,000 - 10,000,000')),
            ('10000001-20000000', _('10,000,000 - 20,000,000')),
            ('20000001-and-above', _('20,000,000 and above')),
        )


    def queryset(self, request, queryset):
        if self.value() == '0-100':
            return queryset.filter(price__price_wholesale__lte=100)
        elif self.value() == '101-200':
            return queryset.filter(price__price_wholesale__range=(101, 200))
        elif self.value() == '201-300':
            return queryset.filter(price__price_wholesale__range=(201, 300))
        return queryset


class CategoryAdmin(MPTTModelAdmin):
    list_display = ('category_name', 'parent', 'slug')
    search_fields = ['category_name']
    list_filter = ['category_name',]



class ImageAdmin(admin.ModelAdmin):
    list_display = ['id','related_products']
    search_fields = ['Product__title']
    list_filter = ['id',]

    def related_products(self, obj):
        products = Product.objects.filter(images=obj)
        product_list = [product.title for product in products]
        return ', '.join(product_list) if product_list else 'No Products'
    related_products.short_description = 'Related Products'

class TextureAdmin(admin.ModelAdmin):
    list_display = ['image_preview']
    search_fields = ['products__title']

    def image_preview(self, obj):
        return format_html('<img src="{}" style="max-height: 60px; max-width: 60px;" />',
                           obj.image.url) if obj.image else 'No Image'

    image_preview.short_description = 'Image Preview'

class PriceAdmin(admin.ModelAdmin):
    list_display = ['unit', 'price_wholesale', 'price_retail']


class ProductAdmin(admin.ModelAdmin):
    list_display = ['title', 'price',   'product_code', 'date_created_jalali', 'textures_summary']
    list_display_links = ['title']
    search_fields = ['title', 'category__category_name',  'product_code']
    list_filter = ['product_code','category','dimensions__length','dimensions__width',  'date_created', PriceRangeFilter] 
    filter_horizontal = ('textures','images')
    def date_created_jalali(self, obj):
        jalali_date = date2jalali(obj.date_created)
        return jalali_date.strftime('%Y/%m/%d')

    def textures_summary(self, obj):
        textures_count = obj.textures.count()
        return format_html('<a href="{}">{}</a>', reverse('admin:products_product_change', args=[obj.id]), f'{textures_count}')


    date_created_jalali.short_description = 'تاریخ ایجاد'
    date_created_jalali.admin_order_field = 'date_created'
    textures_summary.short_description = 'تعداد تکسچرها'

class WallcoveringsAdmin(admin.ModelAdmin):
    list_display = ['title', 'category', 'price', 'dimensions',   'date_created']
    search_fields = ['title', 'category__category_name',   'product_code']
    list_filter = ['title','product_code','category','dimensions__length','dimensions__width',  'date_created', PriceRangeFilter]
    ordering = ['date_created']
    filter_horizontal = ('textures','images')

    list_per_page = 20

class FloorcoveringsAdmin(admin.ModelAdmin):
    list_display = ['title', 'price','product_code']
    search_fields = ['title', 'category__category_name',  'product_code']
    list_filter = ['title','product_code','category','dimensions__length','dimensions__width',  'date_created', PriceRangeFilter]
    filter_horizontal = ('textures','images',)

class CorniceAdmin(admin.ModelAdmin):
    list_display = ['title', 'price', 'product_code',]
    search_fields = ['title', 'category__category_name', 'product_code']
    list_filter = ['title', 'product_code', 'category', 'dimensions__length', 'dimensions__width', 'date_created', 'price__unit',]
    filter_horizontal = ('textures', 'images',)
    # exclude = ('price', )

class ReadycurtainAdmin(admin.ModelAdmin):
    list_display = ['title', 'curtain_rod',]
    search_fields = ['title', 'category__category_name', 'product_code']
    list_filter = ['title', 'product_code', 'category', 'dimensions__length', 'dimensions__width', 'date_created', PriceRangeFilter]
    filter_horizontal = ('textures','images')


class ZebracurtainAdmin(admin.ModelAdmin):
    list_display = ['title',]
    search_fields = ['title', 'category__category_name',  'product_code']
    list_filter = ['title','product_code','category','dimensions__length','dimensions__width',  'date_created', PriceRangeFilter]
    filter_horizontal = ('textures','images')

class CustomcurtainAdmin(admin.ModelAdmin):
    list_display = ['title','curtain_rod', 'curtain_model', 'side_fabric']
    search_fields = ['title', 'category__category_name',  'product_code']
    list_filter = ['title','product_code','category','dimensions__length','dimensions__width',  'date_created', PriceRangeFilter]
    filter_horizontal = ('textures','images','accessory')

class SofafabricAdmin(admin.ModelAdmin):
    list_display = ['title',]
    search_fields = ['title', 'category__category_name',  'product_code']
    list_filter = ['title','product_code','category','dimensions__width',  'date_created', PriceRangeFilter]
    filter_horizontal = ('textures','images')

class SofaAdmin(admin.ModelAdmin):
    list_display = ['title', 'Fabrictype', 'accessory_summary']
    search_fields = ['title', 'category__category_name',  'product_code']
    list_filter = ['title','product_code','category','dimensions__length','dimensions__width',  'date_created', PriceRangeFilter]
    filter_horizontal = ('textures','images','accessory')

    def accessory_summary(self, obj):
        accessories = obj.accessory.all()
        return ', '.join([accessory.title for accessory in accessories]) if accessories else 'No Accessories'

    accessory_summary.short_description = 'Accessories'

class DimensionsAdmin(admin.ModelAdmin):
    list_display = ('id', 'length_with_unit', 'width_with_unit', 'thickness_with_unit')
    search_fields = ['title', 'category__category_name',  'product_code']
    list_filter = ['length','width','thickness']

    def length_with_unit(self, obj):
        return f'{obj.length} {obj.length_unit}'
    length_with_unit.short_description = 'طول'

    def width_with_unit(self, obj):
        return f'{obj.width} {obj.width_unit}'
    width_with_unit.short_description = 'عرض'

    def thickness_with_unit(self, obj):
        return f'{obj.thickness} {obj.thickness_unit}'
    thickness_with_unit.short_description = 'ضخامت'

class ProductTextureAdmin(admin.ModelAdmin):
    list_display = ('product', 'texture', 'code')
    search_fields = ('product__title', 'texture__code')  # جستجو بر اساس نام محصول و کد تکسچر

# class CorniceSupplyAdmin(admin.ModelAdmin):
#     pass
# class CorniceSizeAdmin(admin.ModelAdmin):
#     pass
# class SupplyPriceAdmin(admin.ModelAdmin):
#     pass


admin.site.register(Category, CategoryAdmin)
admin.site.register(Dimensions, DimensionsAdmin)
admin.site.register(Image, ImageAdmin)
admin.site.register(Texture, TextureAdmin)
admin.site.register(Price, PriceAdmin)
admin.site.register(Product, ProductAdmin)
admin.site.register(Wallcoverings, WallcoveringsAdmin)
admin.site.register(Floorcoverings, FloorcoveringsAdmin)
admin.site.register(Cornice, CorniceAdmin)
admin.site.register(Readycurtain, ReadycurtainAdmin)
admin.site.register(Zebracurtain, ZebracurtainAdmin)
admin.site.register(Sofafabric, SofafabricAdmin)
admin.site.register(Sofa, SofaAdmin)
admin.site.register(Customcurtain,CustomcurtainAdmin)



