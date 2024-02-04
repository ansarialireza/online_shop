from django.shortcuts import render
from django.views import View
from products.models import Sofa, Curtain, Decoration
from itertools import chain
from .models import *
from products.models import Sofa,Sofafabric

class HomeView(View):
    template_name = 'website/index.html'

    def get(self, request, *args, **kwargs):
        # Fetch latest products
        latest_sofas = Sofa.objects.order_by('-date_created')[:9]
        latest_curtains = Curtain.objects.order_by('-date_created')[:9]
        latest_decorations = Decoration.objects.order_by('-date_created')[:9]
        latest_products = list(chain(latest_sofas, latest_curtains, latest_decorations))

        # Fetch banners
        sofas_banners = IndexBanner.objects.filter(category='sofa')
        curtains_banners = IndexBanner.objects.filter(category='curtains')[:1]
        decoration_banners = IndexBanner.objects.filter(category='decoration')[:1]

        return render(request, self.template_name, {
            'products': latest_products,
            'sofas_banners': sofas_banners,
            'curtains_banners': curtains_banners,
            'decoration_banners': decoration_banners,
        })

class SofasView(View):
    template_name = 'website/sofas.html'

    def get(self, request):
        latest_sofas = Sofa.objects.order_by('-date_created')[:9]
        latest_sofafabrics = Sofafabric.objects.order_by('-date_created')[:9]
        sofa_banners = SofaBanner.objects.all()

        context = {
            'latest_sofas': latest_sofas,
            'latest_sofafabrics': latest_sofafabrics,
            'sofa_banners': sofa_banners,
        }

        return render(request, self.template_name, context)
    
class AboutView(View):
    template_name = 'website/about_us.html'

    def get(self, request):
        return render(request,self.template_name)
    

def handler404(request, exception):
    return render(request, 'website/404.html', status=404)
