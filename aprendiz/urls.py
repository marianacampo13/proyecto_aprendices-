from django.urls import path
from . import views

urlpatterns = [
    path('', views.lista_aprendices, name='lista'),
    path('aprendices/registrar/', views.registrar_aprendiz, name='registrar_aprendiz'),
    path('aprendices/editar/<str:documento>/', views.editar_aprendiz, name='editar_aprendiz'),
    path('programas/registrar/', views.registrar_programa, name='registrar_programa'),
    path('instructores/registrar/', views.registrar_instructor, name='registrar_instructor'),
    path('competencias/registrar/', views.registrar_competencia, name='registrar_competencia'),
    path('aprendices/eliminar/<str:documento>/', views.eliminar_aprendiz, name='eliminar_aprendiz'),
    path('mapa/', views.mostrar_mapa, name='mapa'),
    path('sedes/registrar/', views.registrar_sede, name='registrar_sede'),
    path('sedes/', views.lista_sedes, name='lista_sedes'),   
    path('sedes/editar/<int:id>/', views.editar_sede, name='editar_sede'),
    path('sedes/eliminar/<int:id>/', views.eliminar_sede, name='eliminar_sede'),
    path('aprendices/buscar/', views.buscar_aprendiz, name='buscar_aprendiz'),
]

