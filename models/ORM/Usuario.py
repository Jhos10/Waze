from peewee import *
from db.Conexion import ConexionORM
# from models.ORM import
conexion_orm = ConexionORM()

class Usuario(Model):
    id_usuario = AutoField()
    fecha_registro = DateField()
    email = CharField()
    nombre = CharField()
    id_configuracion = ForeignKeyField(

    )
    

    class Meta:
        database = conexion_orm.conexion