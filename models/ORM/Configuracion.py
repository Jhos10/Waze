from db.Conexion import ConexionORM
from peewee import *

class Configuracion:
    id_configuracion = AutoField()
    unidadesdistancia = CharField()
    notificaciones = BooleanField()
    placa = CharField()
    id_idioma = ForeignKeyField()
    id_voz = ForeignKeyField()
    id_icono = ForeignKeyField()
    
    class Meta:
        database = ConexionORM.conexion
        