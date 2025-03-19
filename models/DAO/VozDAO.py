from models.VO import VozVO
from db.Conexion import Conexion
from sqlite3 import Error
from typing import List

class VozDAO:
    def __init__(self):
        self.objeto_conexion = Conexion()
    
    def consultarVoces(self)->List[VozVO.VozVo]:
        try:
            with self.objeto_conexion.crear_conexion() as conexion:

                sql = """
                    SELECT * FROM Voz;
                """
                cursor = conexion.cursor()
                cursor.execute(sql)
                informacion_voces = cursor.fetchall()
                lista_voces_vo = [VozVO.VozVo(ID_voz=x[0],Tipo_voz=x[1]) for x in informacion_voces]

                return lista_voces_vo
        except Error as e:
            print(f"Hubo un error al momento de obtener la lista de voces: {e}")
            return e

    def consultar_voz_tipo_voz(self,voz_vo:VozVO.VozVo)->VozVO.VozVo:
        try:
            with self.objeto_conexion.crear_conexion() as conexion:
                sql = "SELECT * FROM Idioma WHERE Tipo_voz = ?"
                cursor = conexion.cursor()
                cursor.execute(sql,(voz_vo.ID_voz,))
                informacion_voz = cursor.fetchone()
                voz_vo  = VozVO.VozVo(ID_voz=informacion_voz[0],Tipo_voz=informacion_voz[1])

                return voz_vo
        except Error as e:
            print(f"Hubo un error en la consulta para encontra lazo por el tipo de voz {e}")
            return None
