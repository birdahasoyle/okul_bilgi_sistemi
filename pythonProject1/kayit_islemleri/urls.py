from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.register_form, name='kayit_ekle'),
    path('<int:id>', views.register_form, name='kayit_guncelle'),
    path('delete<int:id>', views.record_delete, name='kayit_sil'),
    path('liste/', views.register_list, name='kayit_listele'),
    path('ogrenciliste/', views.ogrenci_list, name='kayit_listele'),
]