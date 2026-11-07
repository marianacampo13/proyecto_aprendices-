from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from .models import aprendiz, Sede

from .forms import (
    AprendizForm,
    ProgramaForm,
    InstructorForm,
    CompetenciaForm,
    SedeForm
)

def registrar_aprendiz(request):
    if request.method == 'POST':
        form = AprendizForm(request.POST)

        if form.is_valid():
            form.save()
            messages.success(request, 'El aprendiz fue creado correctamente')
            return redirect('registrar_aprendiz')
    else:
        form = AprendizForm()

    return render(request, 'aprendiz/formularios/formulario.html', {
        'form': form,
        'titulo': 'Registrar aprendiz'
    })


def registrar_programa(request):
    if request.method == 'POST':
        form = ProgramaForm(request.POST)

        if form.is_valid():
            form.save()
            return redirect('registrar_programa')
    else:
        form = ProgramaForm()

    return render(request,'aprendiz/formularios/formulario.html', {
        'form': form,
        'titulo': 'Registrar programa'
    })


def registrar_instructor(request):
    if request.method == 'POST':
        form = InstructorForm(request.POST)

        if form.is_valid():
            form.save()
            return redirect('registrar_instructor')
    else:
        form = InstructorForm()

    return render(request, 'aprendiz/formularios/formulario.html', {
        'form': form,
        'titulo': 'Registrar instructor'
    })


def registrar_competencia(request):
    if request.method == 'POST':
        form = CompetenciaForm(request.POST)

        if form.is_valid():
            form.save()
            return redirect('registrar_competencia')
    else:
        form = CompetenciaForm()

    return render(request, 'aprendiz/formularios/formulario.html', {
        'form': form,
        'titulo': 'Registrar competencia'
    })


def editar_aprendiz(request, documento):
    mi_aprendiz = get_object_or_404(aprendiz, documento=documento)
    form = AprendizForm(request.POST or None, instance=mi_aprendiz)
    form.fields['documento'].disabled = True
    if request.method == 'POST' and form.is_valid():
        form.save()
        messages.success(request, 'El aprendiz fue editado de manera correcta')
        return redirect('lista')  # Redirige a tu lista de aprendices


    return render(request, 'aprendiz/formularios/formulario.html', {
        'form': form,
        'titulo': f'Editar {mi_aprendiz.nombre} {mi_aprendiz.apellido}'
    })
def eliminar_aprendiz(request, documento):
    mi_aprendiz = get_object_or_404(aprendiz, documento=documento)
    
    if request.method == 'POST':
        mi_aprendiz.delete()
        messages.success(request, 'Se eliminó el usuario correctamente')
        return redirect('lista') 
        
    return render(request, 'aprendiz/eliminar.html', {'aprendiz': mi_aprendiz})




def lista_aprendices(request):

    aprendices = aprendiz.objects.all()

    contexto = {
        "aprendices":aprendices
    }
    return render(request, 'aprendiz/index.html', contexto)

def mostrar_mapa(request):
    return render(request, 'aprendiz/mapa.html')


def registrar_sede(request):
    if request.method == 'POST':
        form = SedeForm(request.POST)

        if form.is_valid():
            form.save()
            messages.success(request, 'La sede fue registrada correctamente')
            return redirect('registrar_sede')

    else:
        form = SedeForm()

    return render(request, 'aprendiz/formularios/formulario.html', {
        'form': form,
        'titulo': 'Registrar sede',
        'mostrar_mapa': True
    })


def lista_sedes(request):
    sedes = Sede.objects.all()

    return render(request, 'aprendiz/lista_sedes.html', {
        'sedes': sedes
    })


def editar_sede(request, id):
    sede = Sede.objects.get(id=id)

    if request.method == 'POST':
        form = SedeForm(request.POST, instance=sede)

        if form.is_valid():
            form.save()
            messages.success(request, 'La sede fue actualizada correctamente')
            return redirect('lista_sedes')

    else:
        form = SedeForm(instance=sede)

    return render(request, 'aprendiz/formularios/formulario.html', {
        'form': form,
        'titulo': 'Editar sede',
        'mostrar_mapa': True
    })


def eliminar_sede(request, id):
    sede = Sede.objects.get(id=id)

    if request.method == 'POST':
        sede.delete()
        messages.success(request, 'La sede fue eliminada correctamente')
        return redirect('lista_sedes')

    return render(request, 'aprendiz/eliminar_sede.html', {
        'sede': sede
    })


def editar_sede(request, id):
    sede = Sede.objects.get(id=id)

    if request.method == 'POST':
        form = SedeForm(request.POST, instance=sede)

        if form.is_valid():
            form.save()
            messages.success(request, 'La sede fue actualizada correctamente')
            return redirect('lista_sedes')

    else:
        form = SedeForm(instance=sede)

    return render(request, 'aprendiz/formularios/formulario.html', {
        'form': form,
        'titulo': 'Editar sede',
        'mostrar_mapa': True
    })


def eliminar_sede(request, id):
    sede = Sede.objects.get(id=id)

    if request.method == 'POST':
        sede.delete()
        messages.success(request, 'La sede fue eliminada correctamente')
        return redirect('lista_sedes')

    return render(request, 'aprendiz/eliminar_sede.html', {
        'sede': sede
    })



def buscar_aprendiz(request):
    resultado = None

    if request.method == 'POST':
        busqueda = request.POST.get('buscar', '').strip()

        resultado = aprendiz.objects.filter(
            nombre__icontains=busqueda
        ) | aprendiz.objects.filter(
            apellido__icontains=busqueda
        ) | aprendiz.objects.filter(
            documento__icontains=busqueda
        )

    return render(request, 'aprendiz/buscar_aprendiz.html', {
        'resultado': resultado
    })


