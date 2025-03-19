from db.Conexion import Conexion
from models.VO.IdiomaVO import IdiomaVO
from models.VO.UsuarioVO import UsuarioVO
from typing import List
from sqlite3 import Error
from models.DAO import ConfiguracionDAO

class IdiomaDAO:
    
    def __init__(self):
        # Se intancia el objeto conexion
        self.objeto_conexion = Conexion()

    def consultar(self) -> List[IdiomaVO]:
        try:
            with self.objeto_conexion.crear_conexion() as conexion:
                # Se instancia el cursor a la base de datos
                cursor = conexion.cursor()
                # Se escribe la sentencia sql
                sql = "SELECT * FROM Idioma;"
                # Se ejeucta la sentencia
                cursor.execute(sql)
                # Se obtiene la respuesta de la bd
                informacion_idiomas = cursor.fetchall()
                # Se mapea la respuesta de la bd a una lista de usuarios vo
                lista_idiomas_vo = [IdiomaVO(id_idioma=x[0], nombre_idioma=x[1]) for x  in informacion_idiomas]

                return lista_idiomas_vo
            
        except Error as e:
            # Se imprime el error de la base de datos
            print(f"Error al consultar idiomas: {e}")


    def consultar_idioma_por_nombre(self, idioma:str):
        try:
            with self.objeto_conexion.crear_conexion() as conexion:
                # Se instancia el cursor a la base de datos
                cursor = conexion.cursor()
                # Se escribe la sentencia sql
                sql = "SELECT * FROM Idioma WHERE nombre_idioma = ?"
                # Se ejeucta la sentencia
                cursor.execute(sql, (idioma))
                # Se obtiene la respuesta de la bd
                informacion_idiomas = cursor.fetchone()
                # Se mapea la respuesta de la bd a una lista de usuarios vo
                idioma_vo = IdiomaVO(id_idioma=informacion_idiomas[0], nombre_idioma=informacion_idiomas[1])

                return idioma_vo
            
        except Error as e:
            # Se imprime el error de la base de datos
            print(f"Error al consultar idiomas: {e}")


