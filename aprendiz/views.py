
from functools import wraps

from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.core.exceptions import PermissionDenied

from .models import aprendiz, Sede, Perfil

from .forms import (
    AprendizForm,
    ProgramaForm,
    InstructorForm,
    CompetenciaForm,
    SedeForm
)


# ==========================================
# CONTROL DE ROLES Y PERMISOS
# ==========================================

def rol_requerido(*roles):
    def decorador(vista):
        @login_required
        @wraps(vista)
        def comprobar_rol(request, *args, **kwargs):

            if request.user.is_superuser:
                return vista(request, *args, **kwargs)

            try:
                perfil = request.user.perfil
            except Perfil.DoesNotExist:
                raise PermissionDenied

            if perfil.rol_principal not in roles:
                raise PermissionDenied

            return vista(request, *args, **kwargs)

        return comprobar_rol
    return decorador


# ==========================================
# REGISTRAR APRENDIZ
# ==========================================

@rol_requerido('ADMIN', 'INSTRUCTOR')
def registrar_aprendiz(request):
    if request.method == 'POST':
        form = AprendizForm(request.POST)

        if form.is_valid():
            form.save()
            messages.success(
                request,
                'El aprendiz fue creado correctamente'
            )
            return redirect('registrar_aprendiz')
    else:
        form = AprendizForm()

    return render(
        request,
        'aprendiz/formularios/formulario.html',
        {
            'form': form,
            'titulo': 'Registrar aprendiz'
        }
    )


# ==========================================
# REGISTRAR PROGRAMA
# ==========================================

@rol_requerido('ADMIN', 'INSTRUCTOR')
def registrar_programa(request):
    if request.method == 'POST':
        form = ProgramaForm(request.POST)

        if form.is_valid():
            form.save()
            messages.success(
                request,
                'El programa fue registrado correctamente'
            )
            return redirect('registrar_programa')
    else:
        form = ProgramaForm()

    return render(
        request,
        'aprendiz/formularios/formulario.html',
        {
            'form': form,
            'titulo': 'Registrar programa'
        }
    )


# ==========================================
# REGISTRAR INSTRUCTOR
# ==========================================

@rol_requerido('ADMIN')
def registrar_instructor(request):
    if request.method == 'POST':
        form = InstructorForm(request.POST)

        if form.is_valid():
            form.save()
            messages.success(
                request,
                'El instructor fue registrado correctamente'
            )
            return redirect('registrar_instructor')
    else:
        form = InstructorForm()

    return render(
        request,
        'aprendiz/formularios/formulario.html',
        {
            'form': form,
            'titulo': 'Registrar instructor'
        }
    )


# ==========================================
# REGISTRAR COMPETENCIA
# ==========================================

@rol_requerido('ADMIN', 'INSTRUCTOR')
def registrar_competencia(request):
    if request.method == 'POST':
        form = CompetenciaForm(request.POST)

        if form.is_valid():
            form.save()
            messages.success(
                request,
                'La competencia fue registrada correctamente'
            )
            return redirect('registrar_competencia')
    else:
        form = CompetenciaForm()

    return render(
        request,
        'aprendiz/formularios/formulario.html',
        {
            'form': form,
            'titulo': 'Registrar competencia'
        }
    )


# ==========================================
# EDITAR APRENDIZ
# ==========================================

@rol_requerido('ADMIN')
def editar_aprendiz(request, documento):
    mi_aprendiz = get_object_or_404(
        aprendiz,
        documento=documento
    )

    form = AprendizForm(
        request.POST or None,
        instance=mi_aprendiz
    )

    form.fields['documento'].disabled = True

    if request.method == 'POST' and form.is_valid():
        form.save()

        messages.success(
            request,
            'El aprendiz fue editado de manera correcta'
        )

        return redirect('lista')

    return render(
        request,
        'aprendiz/formularios/formulario.html',
        {
            'form': form,
            'titulo': (
                f'Editar {mi_aprendiz.nombre} '
                f'{mi_aprendiz.apellido}'
            )
        }
    )


# ==========================================
# ELIMINAR APRENDIZ
# ==========================================

@rol_requerido('ADMIN')
def eliminar_aprendiz(request, documento):
    mi_aprendiz = get_object_or_404(
        aprendiz,
        documento=documento
    )

    if request.method == 'POST':
        mi_aprendiz.delete()

        messages.success(
            request,
            'Se eliminó el usuario correctamente'
        )

        return redirect('lista')

    return render(
        request,
        'aprendiz/eliminar.html',
        {
            'aprendiz': mi_aprendiz
        }
    )


# ==========================================
# LISTA DE APRENDICES
# ==========================================

@rol_requerido('ADMIN', 'INSTRUCTOR', 'APRENDIZ')
def lista_aprendices(request):
    aprendices = aprendiz.objects.all()

    contexto = {
        'aprendices': aprendices
    }

    return render(
        request,
        'aprendiz/index.html',
        contexto
    )


# ==========================================
# MOSTRAR MAPA
# ==========================================

@rol_requerido('ADMIN', 'INSTRUCTOR', 'APRENDIZ')
def mostrar_mapa(request):
    return render(
        request,
        'aprendiz/mapa.html'
    )


# ==========================================
# REGISTRAR SEDE
# ==========================================

@rol_requerido('ADMIN')
def registrar_sede(request):
    if request.method == 'POST':
        form = SedeForm(request.POST)

        if form.is_valid():
            form.save()

            messages.success(
                request,
                'La sede fue registrada correctamente'
            )

            return redirect('registrar_sede')
    else:
        form = SedeForm()

    return render(
        request,
        'aprendiz/formularios/formulario.html',
        {
            'form': form,
            'titulo': 'Registrar sede',
            'mostrar_mapa': True
        }
    )


# ==========================================
# LISTA DE SEDES
# ==========================================

@rol_requerido('ADMIN', 'INSTRUCTOR', 'APRENDIZ')
def lista_sedes(request):
    sedes = Sede.objects.all()

    return render(
        request,
        'aprendiz/lista_sedes.html',
        {
            'sedes': sedes
        }
    )


# ==========================================
# EDITAR SEDE
# ==========================================

@rol_requerido('ADMIN')
def editar_sede(request, id):
    sede = get_object_or_404(Sede, id=id)

    if request.method == 'POST':
        form = SedeForm(
            request.POST,
            instance=sede
        )

        if form.is_valid():
            form.save()

            messages.success(
                request,
                'La sede fue actualizada correctamente'
            )

            return redirect('lista_sedes')
    else:
        form = SedeForm(instance=sede)

    return render(
        request,
        'aprendiz/formularios/formulario.html',
        {
            'form': form,
            'titulo': 'Editar sede',
            'mostrar_mapa': True
        }
    )


# ==========================================
# ELIMINAR SEDE
# ==========================================

@rol_requerido('ADMIN')
def eliminar_sede(request, id):
    sede = get_object_or_404(Sede, id=id)

    if request.method == 'POST':
        sede.delete()

        messages.success(
            request,
            'La sede fue eliminada correctamente'
        )

        return redirect('lista_sedes')

    return render(
        request,
        'aprendiz/eliminar_sede.html',
        {
            'sede': sede
        }
    )


# ==========================================
# BUSCAR APRENDIZ
# ==========================================

@rol_requerido('ADMIN', 'INSTRUCTOR', 'APRENDIZ')
def buscar_aprendiz(request):
    resultado = None

    if request.method == 'POST':
        busqueda = request.POST.get(
            'buscar',
            ''
        ).strip()

        resultado = (
            aprendiz.objects.filter(
                nombre__icontains=busqueda
            )
            | aprendiz.objects.filter(
                apellido__icontains=busqueda
            )
            | aprendiz.objects.filter(
                documento__icontains=busqueda
            )
        )

    return render(
        request,
        'aprendiz/buscar_aprendiz.html',
        {
            'resultado': resultado
        }
    )


@login_required
def mi_perfil(request):
    perfil = getattr(request.user, 'perfil', None)

    registro_aprendiz = getattr(
        request.user,
        'registro_aprendiz',
        None
    )

    registro_instructor = getattr(
        request.user,
        'registro_instructor',
        None
    )

    return render(
        request,
        'aprendiz/mi_perfil.html',
        {
            'perfil': perfil,
            'registro_aprendiz': registro_aprendiz,
            'registro_instructor': registro_instructor,
        }
    )





    



