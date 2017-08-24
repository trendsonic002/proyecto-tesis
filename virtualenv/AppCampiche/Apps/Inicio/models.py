# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey has `on_delete` set to the desired behavior.
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from __future__ import unicode_literals

from django.db import models


class Administrador(models.Model):
    id_administrador = models.AutoField(primary_key=True)
    usuario = models.CharField(max_length=200)
    contrasenia = models.CharField(max_length=200)

    class Meta:
        managed = False
        db_table = 'administrador'
    def __unicode__(self):
        return self.usuario



class Alumno(models.Model):
    id_alumno = models.AutoField(primary_key=True)
    id_persona = models.ForeignKey('Persona', models.DO_NOTHING, db_column='id_persona')
    curso = models.CharField(max_length=100)
    huella = models.TextField(blank=True, null=True)
    estado = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'alumno'


class Asistencia(models.Model):
    id_asistencia = models.AutoField(primary_key=True)
    fecha = models.DateField(blank=True, null=True)
    tipo = models.IntegerField(blank=True, null=True)
    id_alumno = models.ForeignKey(Alumno, models.DO_NOTHING, db_column='id_alumno')

    class Meta:
        managed = False
        db_table = 'asistencia'


class AuthGroup(models.Model):
    name = models.CharField(unique=True, max_length=80)

    class Meta:
        managed = False
        db_table = 'auth_group'


class AuthGroupPermissions(models.Model):
    group_id = models.IntegerField()
    permission_id = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'auth_group_permissions'
        unique_together = (('group_id', 'permission_id'),)


class AuthPermission(models.Model):
    name = models.CharField(max_length=255)
    content_type_id = models.IntegerField()
    codename = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'auth_permission'
        unique_together = (('content_type_id', 'codename'),)


class AuthUser(models.Model):
    password = models.CharField(max_length=128)
    last_login = models.DateTimeField(blank=True, null=True)
    is_superuser = models.IntegerField()
    username = models.CharField(unique=True, max_length=150)
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    email = models.CharField(max_length=254)
    is_staff = models.IntegerField()
    is_active = models.IntegerField()
    date_joined = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'auth_user'


class AuthUserGroups(models.Model):
    user_id = models.IntegerField()
    group_id = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'auth_user_groups'
        unique_together = (('user_id', 'group_id'),)


class AuthUserUserPermissions(models.Model):
    user_id = models.IntegerField()
    permission_id = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'auth_user_user_permissions'
        unique_together = (('user_id', 'permission_id'),)


class Direccion(models.Model):
    id_direccion = models.AutoField(primary_key=True)
    region = models.IntegerField()
    comuna = models.CharField(max_length=100)
    ciudad = models.CharField(max_length=100)
    calle = models.CharField(max_length=100)
    numero = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'direccion'


class DjangoAdminLog(models.Model):
    action_time = models.DateTimeField()
    object_id = models.TextField(blank=True, null=True)
    object_repr = models.CharField(max_length=200)
    action_flag = models.SmallIntegerField()
    change_message = models.TextField()
    content_type_id = models.IntegerField(blank=True, null=True)
    user_id = models.IntegerField()

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


class Docente(models.Model):
    id_docente = models.AutoField(primary_key=True)
    id_persona = models.ForeignKey('Persona', models.DO_NOTHING, db_column='id_persona')
    cargo = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'docente'


class Historial(models.Model):
    id_historial = models.AutoField(primary_key=True)
    rut_alum = models.IntegerField()
    fecha = models.DateField()
    hora = models.CharField(max_length=100)
    estado = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'historial'


class Persona(models.Model):
    id_persona = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=200)
    apellido_pat = models.CharField(max_length=100)
    apellido_mat = models.CharField(max_length=100)
    rut = models.IntegerField()
    dverificador = models.CharField(max_length=1)
    sexo = models.CharField(max_length=1)
    telefono_f = models.IntegerField()
    telefono_m = models.IntegerField()
    fecha_nac = models.DateField()
    id_direccion = models.ForeignKey(Direccion, models.DO_NOTHING, db_column='id_direccion')
    asistencia = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'persona'