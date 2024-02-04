from django.shortcuts import render, get_object_or_404
from django.views import View
from .models import Product
from django.views.generic import ListView
from .models import *




class ProductDetailView(View):
    template_name = 'products/product_detail/product_detail.html'

    def get_class_name_for_record(self, record_id):
        try:
            cornice = Cornice.objects.get(id=record_id)
            return 'cornice', cornice
        except Cornice.DoesNotExist:
            pass

        try:
            floorcoverings =Floorcoverings.objects.get(id=record_id)
            return 'Floorcoverings', floorcoverings
        except Floorcoverings.DoesNotExist:
            pass

        try:
            custom_curtain = Customcurtain.objects.get(id=record_id)
            return 'Customcurtain', custom_curtain
        except Customcurtain.DoesNotExist:
            pass

        return None, None

    def get(self, request, product_id, *args, **kwargs):
        class_name, products = self.get_class_name_for_record(product_id)
        print(f"class name : {class_name}")

        if class_name=='cornice':
            product = get_object_or_404(Product, pk=product_id)
            context = {'product': product,'cornice': products, 'class_name': class_name}
        elif class_name=='Customcurtain':
            product = get_object_or_404(Product, pk=product_id)
            context = {'product': product,'custom_curtain':products, 'class_name': class_name}
        elif class_name=='Floorcoverings':
            product = get_object_or_404(Product, pk=product_id)
            context = {'product': product,'Floorcoverings':products, 'class_name': class_name}
        else:
            product = get_object_or_404(Product, pk=product_id)
            context = {'product': product, 'class_name': class_name}

        return render(request, self.template_name, context)

    
class SofaView(View):
    template_name = 'products/product_home/sofa.html'

    def get(self, request, *args, **kwargs):
        sofas = Sofa.objects.all()
        context = {'sofas': sofas}
        return render(request, self.template_name, context)
    
class SofafabricView(View):
    template_name = 'products/product_home/sofafabric.html'

    def get(self, request, *args, **kwargs):
        sofafabrics = Sofafabric.objects.all()
        context = {'sofafabrics': sofafabrics}
        return render(request, self.template_name, context)
    
class WallcoveringsView(View):
    template_name = 'products/product_home/wallcovering.html'

    def get(self, request, *args, **kwargs):
        wallcoverings = Wallcoverings.objects.all()
        context = {'wallcoverings': wallcoverings}
        return render(request, self.template_name, context)
    
class FloorcoveringsView(View):
    template_name = 'products/product_home/floorcovering.html'

    def get(self, request, *args, **kwargs):
        floorcoverings = Floorcoverings.objects.all()
        context = {'floorcoverings': floorcoverings}
        return render(request, self.template_name, context)
    
class CorniceView(View):
    template_name = 'products/product_home/cornice.html'

    def get(self, request, *args, **kwargs):
        cornices = Cornice.objects.all()
        context = {'cornices': cornices}  
        return render(request, self.template_name, context)

class ReadycurtainView(View):
    template_name = 'products/product_home/Readycurtain.html'

    def get(self, request, *args, **kwargs):
        readycurtains = Readycurtain.objects.all()
        context = {'readycurtains': readycurtains}
        return render(request, self.template_name, context)
    
class CustomcurtainView(View):
    template_name = 'products/product_home/customcurtain.html'

    def get(self, request, *args, **kwargs):
        customcurtains = Customcurtain.objects.all()
        context = {'customcurtains': customcurtains}
        return render(request, self.template_name, context)
    
class ZebracurtainView(View):
    template_name = 'products/product_home/zebracurtain.html'

    def get(self, request, *args, **kwargs):
        Zebracurtains = Zebracurtain.objects.all()
        context = {'Zebracurtains': Zebracurtains}
        return render(request, self.template_name, context)





class SearchResultsView(ListView):
    model = Product
    template_name = 'products/search_results.html'
    context_object_name = 'results'

    def get_queryset(self):
        query = self.request.GET.get('q', '')
        return Product.objects.filter(title__icontains=query)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['query'] = self.request.GET.get('q', '')
        return context
