from peewee import *
from db.Conexion import ConexionORM

class Icono(Model):
    id_icono = AutoField()
    tipo_icono = CharField()
    imagen = CharField()

    class Meta:
        database = ConexionORM.conexion
        
          