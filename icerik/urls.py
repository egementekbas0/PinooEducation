from django.urls import path
from .views import *
from django.conf import settings
from django.conf.urls.static import static
urlpatterns = [
    path('home.html', home, name='home'),
    path('kids.html', icerik_index, name='kids'),
    path('teachers.html', icerik_index2, name='teachers'),
    path('teachersicerik.html/<str:icerikanabaslik>/', icerik_icerik, name='teachersicerik'),
    path('kidsicerik.html/<str:icerikanabaslik>/', icerik_icerik2, name='kidsicerik'),
]+static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)