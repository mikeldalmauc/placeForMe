from __future__ import unicode_literals
from django.db import models
from datetime import date, datetime
from django.core.validators import RegexValidator
from django.contrib.auth.models import User
from jsonfield import JSONField

from django.conf import settings



class Facultad(models.Model):
    nombre = models.CharField(max_length=50)
    universidad = models.CharField(max_length=50)
    direccion = models.CharField(max_length=50)
    def __str__(self):
        return self.nombre

class CursoAcademico(models.Model):
    inicioCuatrimestreUno = models.DateField(default=date.today, blank=True)
    inicioCuatrimestreDos = models.DateField(default=date.today, blank=True)
    finCuatrimestreUno = models.DateField(default=date.today, blank=True)
    finCuatrimestreDos = models.DateField(default=date.today, blank=True)
    fiestas = JSONField(blank=True)
    especiales = JSONField(blank=True)
    facultad = models.ForeignKey(Facultad)
    def __str__(self):
        return self.facultad.nombre

class Asignatura(models.Model):
    CURSO = (
            ('1', 'Primero'),
            ('2', 'Segundo'),
            ('3', 'Tercero'),
            ('4', 'Cuarto'),
            ('5', 'Quinto')
    )

    IDIOMA = (
        ('eu', 'Euskera'),
        ('en', 'Ingles'),
        ('es', 'Castellano')
    )

    nombre = models.CharField(max_length=10)
    codigo = models.IntegerField()
    nombreCompleto = models.CharField(max_length=50)
    curso = models.CharField(max_length=10, choices=CURSO)
    idioma = models.CharField(choices=IDIOMA, max_length=10)
    def __str__(self):
        return self.nombre

class AsignaturaAnno(models.Model):
    CUATRI = (
        ('1', 'Primero'),
        ('2', 'Segundo')
    )

    DIAHA = (
        ('L', 'Lunes'),
        ('M', 'Martes'),
        ('X', 'Miercoles'),
        ('J', 'Jueves'),
        ('V', 'Viernes')
    )

    plazasSolicitadas = models.IntegerField(default=0)
    anno = models.IntegerField()
    creditosMinimos = models.IntegerField(default=0)
    plazasOcupadas = models.IntegerField(default=0)
    plazasMaximas = models.IntegerField(default=0)
    cuatrimestre = models.CharField(choices=CUATRI, max_length=10)
    diaHorarioAgrupado = models.CharField(choices=DIAHA, blank=True, max_length=10)
    # {
    # 'Examenes': [{''Nombre': xxx, 'Dia': xxx (Tipo DATEJS), 'HInicio': xxx, 'HFin': xxx}, {..}, {..}],
    # 'Clases': [{'Dia': xxx (Tipo DATEJS), 'HInicio': xxx, 'HFin': xxx}, {..}, {..}],
    # 'Tareas': [{'id', xxx, 'Titulo': xxx, 'Descripcion': xxx, 'HFin': xxx, 'Creador': user.id}, {..}, {..}]
    # }
    eventos = JSONField(blank=True)
    # {'Clases': [{Dia': xxx (Tipo DATEJS), 'HInicio': xxx, 'HFin': xxx}, {..}, {..}]}
    descripcion = models.CharField(max_length=1000)
    enlaceGuia = models.URLField(blank=True)
    colorEvento = models.CharField(max_length=8, blank=True)
    asignatura = models.ForeignKey(Asignatura)

    def __str__(self):
        return self.asignatura.nombre

class ValoracionAsignatura(models.Model):
    valoracion = models.IntegerField(default=0)
    argumento = models.CharField(max_length=140, blank=True)
    asignatura = models.ForeignKey(AsignaturaAnno)
    creador = models.ForeignKey(User)
    def __str__(self):
        return self.id

class Tarea(models.Model):
    descripcion = models.CharField(max_length=140)
    titulo = models.CharField(max_length=50)
    HFin = models.TimeField(auto_now=False, blank=True)
    HInicio = models.TimeField(auto_now=False, blank=True)
    puntuacion = models.IntegerField(default=0)
    creador = models.ForeignKey(User)
    def __str__(self):
        return self.titulo


class MeGustaTarea(models.Model):
    valor = models.IntegerField(default=0)
    valorador = models.ForeignKey(User)
    tarea = models.ForeignKey(Tarea)
    def __str__(self):
        return self.Tarea.titulo

class Comentario(models.Model):
    contenido = models.CharField(max_length=140)
    fechaCreacion = models.DateField(default=date.today, blank=True)
    fechaUltimaModificacion = models.DateField(default=date.today, blank=True)
    puntuacion = models.IntegerField(default=0)
    creador = models.ForeignKey(User)
    def __str__(self):
        return self.User.username

class MeGustaComentario(models.Model):
    valor = models.IntegerField(default=0)
    valorador = models.ForeignKey(User)
    comentario = models.ForeignKey(Comentario)
    def __str__(self):
        return self.comentario

class Logs(models.Model):
    data = models.CharField(max_length=255)
    facultad = models.ForeignKey(Facultad)
    usuario = models.ForeignKey(User)
    def __str__(self):
        return self.facultad.nombre
