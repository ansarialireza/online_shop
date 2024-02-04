from django.urls import path
from .views import *

app_name = 'products'

urlpatterns = [
    path('search/', SearchResultsView.as_view(), name='search_results'),
    path('Sofa/', SofaView.as_view(), name='sofa'),
    path('Sofafabric/', SofafabricView.as_view(), name='sofafabric'),
    path('Wallcoverings/', WallcoveringsView.as_view(), name='wallcovering'),
    path('Floorcoverings/', FloorcoveringsView.as_view(), name='floorcovering'),
    path('Cornice/', CorniceView.as_view(), name='cornice'),
    path('Readycurtain/', ReadycurtainView.as_view(), name='readycurtain'),
    path('Customcurtain/', CustomcurtainView.as_view(), name='customcurtain'),
    path('zebracurtain/', ZebracurtainView.as_view(), name='zebracurtain'),
    path('<int:product_id>/', ProductDetailView.as_view(), name='product_detail'),
]