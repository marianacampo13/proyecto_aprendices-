
from django.contrib import admin
from .models import (
    aprendiz,
    programa,
    instructores,
    competencias,
    Sede,
    Perfil
)


@admin.register(aprendiz)
class AprendizAdmin(admin.ModelAdmin):
    list_display = (
        'nombre',
        'apellido',
        'documento',
        'correo',
        'usuario'
    )

    search_fields = (
        'nombre',
        'apellido',
        'documento'
    )


@admin.register(instructores)
class InstructoresAdmin(admin.ModelAdmin):
    list_display = (
        'nombre',
        'apellido',
        'documento',
        'especialidad',
        'usuario'
    )

    search_fields = (
        'nombre',
        'apellido',
        'documento'
    )


admin.site.register(programa)
admin.site.register(competencias)
admin.site.register(Sede)
admin.site.register(Perfil)
