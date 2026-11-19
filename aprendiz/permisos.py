
from functools import wraps
from django.contrib.auth.decorators import login_required
from django.shortcuts import render


def requiere_rol(*roles_permitidos):
    def decorador(vista):
        @login_required
        @wraps(vista)
        def verificar_rol(request, *args, **kwargs):

            # El superusuario tiene acceso total
            if request.user.is_superuser:
                return vista(request, *args, **kwargs)

            # Consultar el perfil del usuario
            perfil = getattr(request.user, 'perfil', None)

            # El administrador puede realizar todas las acciones
            if perfil and perfil.rol_principal == 'ADMIN':
                return vista(request, *args, **kwargs)

            # Verificar el rol autorizado
            if perfil and perfil.rol_principal in roles_permitidos:
                return vista(request, *args, **kwargs)

            # Si no tiene permiso, mostrar un mensaje
            return render(
                request,
                'aprendiz/sin_permiso.html',
                status=403
            )

        return verificar_rol
    return decorador
