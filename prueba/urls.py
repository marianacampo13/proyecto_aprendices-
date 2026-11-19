
from django.contrib import admin
from django.urls import path, include
from django.contrib.auth import views as auth_views
from django.shortcuts import render
from aprendiz import views


urlpatterns = [
    path('admin/', admin.site.urls),

    path('', include('aprendiz.urls')),

    path(
        'formulario/',
        views.registrar_aprendiz,
        name='formulario'
    ),

    path(
        'accounts/login/',
        auth_views.LoginView.as_view(
            template_name='aprendiz/login.html'
        ),
        name='login'
    ),

    path(
        'cerrar-sesion/',
        auth_views.LogoutView.as_view(next_page='/'),
        name='logout'
    ),
]


def permiso_denegado(request, exception):
    return render(
        request,
        'aprendiz/403.html',
        status=403
    )

handler403 = 'prueba.urls.permiso_denegado'


