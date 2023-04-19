from django.urls import path
from . import views

urlpatterns = [
     path('', views.index, name='index'),
    path('belge-sifreleme/', views.belge_sifreleme, name='belge_sifreleme'),
    path('belge-desifreleme/', views.belge_desifreleme, name='belge_desifreleme'),
    path('des-bilgilendirme/', views.des_bilgilendirme, name='des_bilgilendirme'),
    
    
    ]
