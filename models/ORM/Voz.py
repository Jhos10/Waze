from peewee import *
from db.Conexion import ConexionORM

class Voz(Model):
    id_voz = AutoField()
    tipo_voz = CharField()

    class Meta:
        database = ConexionORM.conexion
        