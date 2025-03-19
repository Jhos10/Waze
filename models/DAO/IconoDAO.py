from db.Conexion import Conexion
from models.VO.IconoVO import IconoVO
from typing import List
from sqlite3 import Error

class IconoDAO:

    def __init__(self):
        self.objeto_conexion = Conexion()

    
    def consultar_iconos(self)-> List[IconoVO]:
        try:
            with self.objeto_conexion.crear_conexion() as conexion:

                cursor = conexion.cursor()

                sql = "SELECT * FROM Icono;"

                cursor.execute(sql)

                info_icono= cursor.fetchall()


                lista_iconos =[IconoVO(ID_Icono=x[0],tipo=x[1],imagen=x[2]) for x in info_icono]

            return lista_iconos
        
        except Error as e:
            print(f"Error al consultar configuracion del usuario {e}")
        
            return lista_iconos