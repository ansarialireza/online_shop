"""
URL configuration for config project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings
from django.contrib.sitemaps.views import sitemap
# from website.sitemaps import StaticViewSitemap
# from blog.sitemaps import BlogSitemap
from django.conf.urls import handler404
from azbankgateways.urls import az_bank_gateways_urls


# sitemaps = {
#     "static": StaticViewSitemap,
#     'blog': BlogSitemap
# }

    
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('website.urls')),
    path('accounts/', include('accounts.urls')),
    path('products/', include('products.urls')),
    path('orders/', include('orders.urls')),
    path('cart/', include('cart.urls')),
    path('robots.txt', include('robots.urls')),
    path('summernote/', include('django_summernote.urls')),
    path('captcha/', include('captcha.urls')),
    path('bankgateways/', az_bank_gateways_urls()),
    path('payments/',include('payments.urls')),
    # path("sitemap.xml",sitemap,{"sitemaps": sitemaps},name="django.contrib.sitemaps.views.sitemap",),
]
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

# handler404 = 'website.views.handler404'