from peewee import *
from db.Conexion import ConexionORM


class Idioma(Model):
    id_idioma = AutoField()
    nombre_idioma = CharField()

    class Meta:
        database = ConexionORM.conexion