from django.contrib import admin

from .models import *

class PaisAdmin(admin.ModelAdmin):
    list_display = ('id','nombre',)

class UniversidadAdmin(admin.ModelAdmin):
    list_display = ('id','nombre',)


class InstitucionAdmin(admin.ModelAdmin):
    list_display = ('id','nombre', 'pais',)

class PlanEstudioAdmin(admin.ModelAdmin):
    list_display = ('id','nombre', 'fecha_vigencia', 'universidad',)

class GuiaAdmin(admin.ModelAdmin):
    list_display = ('id','nombre', 'fecha_vigencia', 'institucion',)

class NodoModCursoAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'guia',)

class NodoCursoAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'plan',)

class EnlaceModCursoAdmin(admin.ModelAdmin):
    list_display = ('id', 'origen', 'destino', 'guia',)

class EnlaceCursoAdmin(admin.ModelAdmin):
    list_display = ('id', 'origen', 'destino', 'plan',)


admin.site.register(Pais, PaisAdmin)
admin.site.register(Universidad, UniversidadAdmin)
admin.site.register(Institucion, InstitucionAdmin)
admin.site.register(PlanEstudio, PlanEstudioAdmin)
admin.site.register(Guia, GuiaAdmin)
admin.site.register(NodoModCurso, NodoModCursoAdmin)
admin.site.register(NodoCurso, NodoCursoAdmin)
admin.site.register(EnlaceCurso, EnlaceCursoAdmin)
admin.site.register(EnlaceModCurso, EnlaceModCursoAdmin)



