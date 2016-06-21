from django.contrib import admin
from .models import Facultad, CursoAcademico, Asignatura, AsignaturaAnno, ValoracionAsignatura, Tarea, MeGustaTarea, Comentario, MeGustaComentario, Logs

@admin.register(Facultad)
class AdminFacultad(admin.ModelAdmin):
    list_display = ('id', 'nombre', 'universidad')
    list_filter = ('id', )

@admin.register(CursoAcademico)
class AdminCursoAcademico(admin.ModelAdmin):
    list_display = ('id', 'inicioCuatrimestreUno', 'inicioCuatrimestreDos')
    list_filter = ('id', )

@admin.register(Asignatura)
class AdminAsignatura(admin.ModelAdmin):
    list_display = ('id', 'nombre', 'curso', 'idioma')
    list_filter = ('id', 'curso', 'idioma')

@admin.register(AsignaturaAnno)
class AdminAsignaturaAnno(admin.ModelAdmin):
    list_display = ('id', )
    list_filter = ('id', )

@admin.register(ValoracionAsignatura)
class AdminValoracionAsignatura(admin.ModelAdmin):
    list_display = ('id', 'valoracion')
    list_filter = ('id',)


@admin.register(Tarea)
class AdminTarea(admin.ModelAdmin):
    list_display = ('id', 'titulo', 'creador')
    list_filter = ('id',)

@admin.register(MeGustaTarea)
class AdminMeGustaTarea(admin.ModelAdmin):
    list_display = ('id', 'valor', 'valorador')
    list_filter = ('id',)

@admin.register(Comentario)
class AdminAsignatura(admin.ModelAdmin):
    list_display = ('id', 'creador', 'puntuacion', 'fechaCreacion')
    list_filter = ('id', 'creador', 'puntuacion', 'fechaCreacion')

@admin.register(MeGustaComentario)
class AdminMeGustaComentario(admin.ModelAdmin):
    list_display = ('id', 'valorador', 'comentario')
    list_filter = ('id',)

@admin.register(Logs)
class AdminLogs(admin.ModelAdmin):
    list_display = ('id', 'data')
    list_filter = ('id', 'facultad')
