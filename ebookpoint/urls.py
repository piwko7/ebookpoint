from django.urls import path, include
from .views import scrap_ebookpoint

urlpatterns = [
    path('ebookpoint/', scrap_ebookpoint, name='scrap_ebookpoint'),
]
