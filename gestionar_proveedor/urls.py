
from django.urls import path, include
from . import views

urlpatterns = [
    path('dashboard/', views.dashboard, name='dashboard'),
    
    #proveedor
    path('proveedor/', views.gestionar_proveedor, name='gestionar_proveedor'),
    path('proveedor/añadir/', views.añadir_proveedor, name='añadir_proveedor'),
    path('proveedor/editar/<int:proveedor_id>/', views.editar_proveedor, name='editar_proveedor'),
    path('proveedor/activar-inactivar/<int:proveedor_id>/', views.activar_inactivar_proveedor, name='activar_inactivar_proveedor'),
    path('proveedor/consultar/', views.consultar_proveedor, name='consultar_proveedor'),
    
]