from django.urls import path
from .views import *

urlpatterns = [
    path('', index, name='main_page'),
    path('top-sellers/', top_sellers, name='top_sellers'),
    path('advertisement-post/', advertisment_post, name='da')
]
