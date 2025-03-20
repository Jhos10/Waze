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
        

    def consultar_por_id(self,icono:IconoVO)->IconoVO:
        try:
            with self.objeto_conexion.crear_conexion() as conexion:

                cursor = conexion.cursor()

                sql = "SELECT * FROM Icono WHERE ID_icono = ?;"

                cursor.execute(sql,(icono.ID_Icono,))

                info_icono= cursor.fetchone()

                print(info_icono)
                icono_vo =IconoVO(ID_Icono=info_icono[0],tipo=info_icono[1],imagen=info_icono[2])

            return icono_vo
        
        except Error as e:
            print(f"Error al consultar icono del usuario {e}")
        
            return False

    