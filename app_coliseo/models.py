# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
#
# Also note: You'll have to insert the output of 'django-admin sqlcustom [app_label]'
# into your database.
from __future__ import unicode_literals

from django.db import models

class AuthGroup(models.Model):
    name = models.CharField(unique=True, max_length=80)

    class Meta:
        managed = False
        db_table = 'auth_group'


class AuthGroupPermissions(models.Model):
    group = models.ForeignKey(AuthGroup)
    permission = models.ForeignKey('AuthPermission')

    class Meta:
        managed = False
        db_table = 'auth_group_permissions'
        unique_together = (('group_id', 'permission_id'),)


class AuthPermission(models.Model):
    name = models.CharField(max_length=255)
    content_type = models.ForeignKey('DjangoContentType')
    codename = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'auth_permission'
        unique_together = (('content_type_id', 'codename'),)


class AuthUser(models.Model):
    password = models.CharField(max_length=128)
    last_login = models.DateTimeField(blank=True, null=True)
    is_superuser = models.BooleanField()
    username = models.CharField(unique=True, max_length=30)
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    email = models.CharField(max_length=254)
    is_staff = models.BooleanField()
    is_active = models.BooleanField()
    date_joined = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'auth_user'


class AuthUserGroups(models.Model):
    user = models.ForeignKey(AuthUser)
    group = models.ForeignKey(AuthGroup)

    class Meta:
        managed = False
        db_table = 'auth_user_groups'
        unique_together = (('user_id', 'group_id'),)


class AuthUserUserPermissions(models.Model):
    user = models.ForeignKey(AuthUser)
    permission = models.ForeignKey(AuthPermission)

    class Meta:
        managed = False
        db_table = 'auth_user_user_permissions'
        unique_together = (('user_id', 'permission_id'),)


class Campeonato(models.Model):
    id_campeonato = models.IntegerField(primary_key=True)
    nombre_campeonato = models.CharField(max_length=50, blank=True, null=True)
    fecha_inicio = models.DateField()
    fecha_final = models.DateField()
    id_disciplina = models.ForeignKey('Disciplina', db_column='id_disciplina')

    def __str__(self):
        return self.nombre_campeonato

    class Meta:
        managed = False
        db_table = 'campeonato'


class Disciplina(models.Model):
    id_disciplina = models.IntegerField(primary_key=True)
    nombre_diciplina = models.CharField(max_length=50, blank=True, null=True)
   
    def __str__(self):
        return str(self.nombre_diciplina)

    class Meta:
        managed = False
        db_table = 'disciplina'


class DjangoAdminLog(models.Model):
    action_time = models.DateTimeField()
    object_id = models.TextField(blank=True, null=True)
    object_repr = models.CharField(max_length=200)
    action_flag = models.SmallIntegerField()
    change_message = models.TextField()
    content_type = models.ForeignKey('DjangoContentType', blank=True, null=True)
    user = models.ForeignKey(AuthUser)

    class Meta:
        managed = False
        db_table = 'django_admin_log'


class DjangoContentType(models.Model):
    app_label = models.CharField(max_length=100)
    model = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'django_content_type'
        unique_together = (('app_label', 'model'),)


class DjangoMigrations(models.Model):
    app = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    applied = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_migrations'


class DjangoSession(models.Model):
    session_key = models.CharField(primary_key=True, max_length=40)
    session_data = models.TextField()
    expire_date = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_session'


class Equipo(models.Model):
    id_equipo = models.IntegerField(primary_key=True)
    nombre_equipo = models.CharField(max_length=50)
    id_campeonato = models.ForeignKey(Campeonato, db_column='id_campeonato')
    id_representante = models.ForeignKey('Persona', db_column='id_representante')
   
    def __str__(self):
        return self.nombre_equipo

    class Meta:
        managed = False
        db_table = 'equipo'


class Jugador(models.Model):
    id_jugador = models.IntegerField(primary_key=True)
    id_equipo = models.ForeignKey(Equipo, db_column='id_equipo')
    id_persona = models.ForeignKey('Persona', db_column='id_persona')

    def __str__(self):
        return str(self.id_persona)

    class Meta:
        managed = False
        db_table = 'jugador'


class Lugar(models.Model):
    id_lugar = models.IntegerField(primary_key=True)
    nombre_lugar = models.CharField(max_length=50, blank=True, null=True)
    direccion = models.CharField(max_length=100, blank=True, null=True)
    observacion = models.CharField(max_length=200, blank=True, null=True)

    def __str__(self):
        return self.nombre_lugar

    class Meta:
        managed = False
        db_table = 'lugar'


class Partido(models.Model):
    id_partido = models.IntegerField(primary_key=True)
    id_equipo_local = models.ForeignKey(Equipo, db_column='id_equipo_local')
    id_equipo_visitante = models.ForeignKey(Equipo, db_column='id_equipo_visitante')
    fecha_partido = models.DateField(blank=True, null=True)
    id_lugar = models.ForeignKey(Lugar, db_column='id_lugar')
    planilla = models.CharField(max_length=200, blank=True, null=True)
    observacion = models.CharField(max_length=200, blank=True, null=True)

    def __str__(self):
        return str(str(self.id_partido)+" - "+str(self.id_equipo_local)+" - "+str(self.id_equipo_visitante)+" - "+str(self.fecha_partido))

    class Meta:
        managed = False
        db_table = 'partido'


class PartidoAnotacion(models.Model):
    id_partido_anotacion = models.IntegerField(primary_key=True)
    id_partido = models.ForeignKey(Partido, db_column='id_partido')
    id_jugador = models.ForeignKey(Jugador, db_column='id_jugador')
    cantidad = models.IntegerField(blank=True, null=True)
    observacion = models.CharField(max_length=200, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'partido_anotacion'


class PartidoArbitro(models.Model):
    id_partido = models.ForeignKey(Partido, db_column='id_partido')
    id_persona = models.ForeignKey('Persona', db_column='id_persona')
    id_rol = models.ForeignKey('Rol', db_column='id_rol')

    class Meta:
        managed = False
        db_table = 'partido_arbitro'
        unique_together = (('id_partido', 'id_persona', 'id_rol'),)


class Persona(models.Model):
    id = models.IntegerField(primary_key=True)
    p_nombre = models.CharField(max_length=50, blank=True, null=True)
    o_nombre = models.CharField(max_length=50, blank=True, null=True)
    p_apellido = models.CharField(max_length=50, blank=True, null=True)
    s_apellido = models.CharField(max_length=50, blank=True, null=True)
    id_tipo_identificacion = models.ForeignKey('TipoIdentificacion', db_column='id_tipo_identificacion')
    identificacion = models.CharField(max_length=20)
    fecha_nacimiento = models.DateField(blank=True, null=True)
    genero = models.CharField(max_length=1, blank=True, null=True)
    es_arbitro = models.CharField(max_length=1, blank=True, null=True)
    fotografia = models.CharField(max_length=100, blank=True, null=True)

    def __str__(self):
        return str(self.p_nombre+" "+self.o_nombre+" "+self.p_apellido+" "+self.s_apellido)

    class Meta:
        managed = False
        db_table = 'persona'



class Rol(models.Model):
    id_rol = models.IntegerField(primary_key=True)
    nombre_rol = models.CharField(max_length=50, blank=True, null=True)

    def __str__(self):
        return self.nombre_rol

    class Meta:
        managed = False
        db_table = 'rol'


class TipoIdentificacion(models.Model):
    id_tipo_identificacion = models.IntegerField(primary_key=True)
    nombre_ti = models.CharField(max_length=50, blank=True, null=True)
    def __str__(self):
        return self.nombre_ti
    class Meta:
        managed = False
        db_table = 'tipo_identificacion'


class MyModel(models.Model):

    title = models.CharField(max_length=100)
    timestamp = models.DateTimeField()