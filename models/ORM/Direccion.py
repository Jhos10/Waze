from peewee import *
from db.Conexion import ConexionORM

class Direcciones(Model):
    id_direcciones = AutoField()
    direccion = CharField()

    class Meta:
        database = ConexionORM.conexion
        