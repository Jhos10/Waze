from db.Conexion import Conexion
from models.VO.DireccionVO import DireccionVO
from typing import List
from sqlite3 import Error

class DireccionDAO:
    
    def __init__(self):
        # Se intancia el objeto conexion
        self.objeto_conexion = Conexion()

    def consultar(self)-> List[DireccionVO]:

        try:
            with self.objeto_conexion.crear_conexion() as conexion:

                cursor = conexion.cursor()

                sql = "SELECT * FROM Direcciones;"

                cursor.execute(sql)

                informacion_direcciones = cursor.fetchall()

                lista_direcciones_vo = [DireccionVO(id_direccion=x[0], direccion=x[1]) for x in informacion_direcciones]


                return lista_direcciones_vo

        except Error as e:
            print(f"Error al consultar direcciones {e}")
        
        return lista_direcciones_vo
    
    def consultar_id_direccion(self, nombre_direccion)->DireccionVO:
        try:
            with self.objeto_conexion.crear_conexion() as conexion:

                cursor = conexion.cursor()

                sql = "SELECT * FROM Direcciones WHERE Direccion = ?;"

                cursor.execute(sql, (nombre_direccion,))

                info_direccion = cursor.fetchone()

                direccion = DireccionVO(id_direccion=info_direccion[0], direccion=info_direccion[1])

                return direccion
            
        except Error as e:
            print(f"Error al consultar id direccion {e}")

        return direccion

