from django.contrib import admin
from django.urls import path

from . import views


app_name = 'persona_app'

urlpatterns = [

    path(
        '', 
        views.HomeView.as_view(), 
        name='home'
        
    ),
    path(
        'add-familiar/', 
        views.FamiliarCreateView.as_view(),
        name='add-familiar'
        
    ),
    path(
        'success/', 
        views.SuccessView.as_view(), 
        name='registro_correcto'
    ),
    path(
        'update-success/', 
        views.UpdateSuccessView.as_view(), 
        name='actualizacion-exitosa'
    ),
    path(
        'actualizar-familiar/<pk>', 
        views.FamiliarUpdateView.as_view(), 
        name='actualizar'
    ),
    path(
        'lista-familiares/', 
        views.ListFamiliares.as_view(),
        name='familiares'
    ),
    path(
        'detalle-familiar/<pk>', 
        views.FamiliarDetailView.as_view(),
        name='detalle_familiar'
    ),
    path(
        'eliminar-familiar/<pk>', 
        views.FamiliarDeleteView.as_view(), 
        name='eliminar'
    ),


]
 