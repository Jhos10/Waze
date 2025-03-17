from db.Conexion import Conexion
from models.VO.UsuarioVO import UsuarioVO
from typing import List
from sqlite3 import Error

class UsuarioDAO:
    
    def __init__(self):
        # Se intancia el objeto conexion
        self.objeto_conexion = Conexion()

    
    def consultar(self)->List[UsuarioVO]:
        try:
            with self.objeto_conexion.crear_conexion() as conexion:
                # Se instancia el cursor a la base de datos
                cursor = conexion.cursor()
                # Se escribe la sentencia sql
                sql = "SELECT * FROM Usuario"
                # Se ejeucta la sentencia
                cursor.execute(sql)
                # Se obtiene la respuesta de la bd
                informacion_usuarios = cursor.fetchall()
                # Se mapea la respuesta de la bd a una lista de usuarios vo
                lista_usaurio_vo = [UsuarioVO(ID_usuario=x[0],fecha_registro=x[1],email=x[2],nombre=x[3],configuracion=x[4]) for x in informacion_usuarios]

                return lista_usaurio_vo
            
        except Error as e:
            # Se imprime el error de la base de datos
            print(f"Error al consultar usuarios: {e}")
        
        return lista_usaurio_vo
        