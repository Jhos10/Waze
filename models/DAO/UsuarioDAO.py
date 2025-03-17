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
        
    def consultar_por_correo(self, email):
        try:
            with self.objeto_conexion.crear_conexion() as conexion:

                cursor = conexion.cursor()

                sql = "SELECT * FROM Usuario WHERE Email = ?;"

                cursor.execute(sql, (email,))

                informacion_usuario = cursor.fetchone()

                usuario = UsuarioVO(ID_usuario=informacion_usuario[0],
                                     fecha_registro=informacion_usuario[1],
                                      email=informacion_usuario[2], 
                                      nombre=informacion_usuario[3], 
                                      configuracion=informacion_usuario[4])
                return usuario
        except Error as e:
            print(f"Error al consultar por correo {e}")
            return e
