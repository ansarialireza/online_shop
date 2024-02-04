from django.urls import path
from .views import *

app_name = 'website'

urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('about/', AboutView.as_view(), name='about'),
    path('sofas/', SofasView.as_view(), name='sofas'),

    # other paths...
]

handler404 = 'website.views.handler404'
