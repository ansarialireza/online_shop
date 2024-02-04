from django.contrib import admin
from .models import *
from django.utils.html import format_html
from django.utils.translation import gettext_lazy as _

class IndexBannerAdmin(admin.ModelAdmin):
    list_display = ('category', 'preview_small_image', 'preview_large_image')

    def preview_small_image(self, obj):
        return format_html('<img src="{}" height="100" />', obj.small_image.url) if obj.small_image else ''
    preview_small_image.short_description = 'تصویر کوچک'

    def preview_large_image(self, obj):
        return format_html('<img src="{}" height="100" />', obj.large_image.url) if obj.large_image else ''
    preview_large_image.short_description = 'تصویر بزرگ'


class SofaBannerAdmin(admin.ModelAdmin):
    def get_small_image_preview(self, obj):
        return format_html('<img src="{}" height="50" />', obj.small_sofa_image.url) if obj.small_sofa_image else ''
    get_small_image_preview.allow_tags = True
    get_small_image_preview.short_description = 'تصویر کوچک مبل'

    def get_small_fabric_image_preview(self, obj):
        return format_html('<img src="{}" height="50" />', obj.small_sofafabric_image.url) if obj.small_sofafabric_image else ''
    get_small_fabric_image_preview.allow_tags = True
    get_small_fabric_image_preview.short_description = 'تصویر کوچک پارچه مبلی'

    def get_large_image_1_preview(self, obj):
        return format_html('<img src="{}" height="50" />', obj.large_sofa_image_1.url) if obj.large_sofa_image_1 else ''
    get_large_image_1_preview.allow_tags = True
    get_large_image_1_preview.short_description = 'تصویر بزرگ 1'

    def get_large_image_2_preview(self, obj):
        return format_html('<img src="{}" height="50" />', obj.large_sofa_image_2.url) if obj.large_sofa_image_2 else ''
    get_large_image_2_preview.allow_tags = True
    get_large_image_2_preview.short_description = 'تصویر بزرگ 2'

    def get_large_image_3_preview(self, obj):
        return format_html('<img src="{}" height="50" />', obj.large_sofa_image_3.url) if obj.large_sofa_image_3 else ''
    get_large_image_3_preview.allow_tags = True
    get_large_image_3_preview.short_description = 'تصویر بزرگ 3'

    list_display = ('id', 'get_small_image_preview', 'get_small_fabric_image_preview', 'get_large_image_1_preview', 'get_large_image_2_preview', 'get_large_image_3_preview')
    search_fields = ['id', 'small_sofa_image__name', 'small_sofafabric_image__name', 'large_sofa_image_1__name', 'large_sofa_image_2__name', 'large_sofa_image_3__name']

    fieldsets = [
        ('General Information', {'fields': ['small_sofa_image', 'small_sofafabric_image']}),
        ('Large Images', {'fields': ['large_sofa_image_1', 'large_sofa_image_2', 'large_sofa_image_3']}),
    ]

admin.site.register(SofaBanner, SofaBannerAdmin)
admin.site.register(IndexBanner, IndexBannerAdmin)
