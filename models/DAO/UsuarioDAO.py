from db.Conexion import Conexion
from models.VO.UsuarioVO import UsuarioVO
from models.VO.ConfiguracionVO import ConfiguracionVO
from typing import List
from sqlite3 import Error
from models.DAO import ConfiguracionDAO
from peewee import *

class UsuarioDAO:
    
    def __init__(self):
        # Se intancia el objeto conexion
        self.objeto_conexion = Conexion()
        # Usuario actual
        self.usuario_actual = None

    def nuevo_usuario(self,nuevo_usuario:UsuarioVO)->int:
        try:
            with self.objeto_conexion.crear_conexion() as conexion:

                configuracion_dao = ConfiguracionDAO.ConfiguracionDAO()
                configuracion_vo = configuracion_dao.configuracion_predeterminada()
                print(configuracion_vo)
                sql = """
                    INSERT INTO Usuario(
                        Fecha_registro,
                        Email,
                        Nombre,
                        ID_Config
                    )
                    VALUES (
                    datetime('now'),
                    ?,
                    ?,
                    ?
                    );
                """

                cursor = conexion.cursor()
                cursor.execute(sql, (nuevo_usuario.email,nuevo_usuario.nombre,configuracion_vo.Id_configuracion))
                conexion.commit()
        except Error as e:
            print(f"Hubo un error al general el usuario: {e}")

    def eliminarUsuario(self,usuario_vo:UsuarioVO):
        try:
            configuracion_dao = ConfiguracionDAO.ConfiguracionDAO()
            configuracion_dao.eliminar_configuracion(usuario_vo.configuracion)
            with self.objeto_conexion.crear_conexion() as conexion:
                sql = "DELETE FROM Usuario WHERE ID_Usuario = ?;"
                cursor = conexion.cursor()
                cursor.execute(sql,(usuario_vo.ID_usuario,))
                conexion.commit()
            return cursor.lastrowid
        except Error as e:
            print(f"Hubo un error en eliminar usuario: {e}")
            return False
            

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

                sql = "SELECT * FROM Usuario WHERE Email = ?"

                cursor.execute(sql, (email,))

                informacion_usuario = cursor.fetchone()

                configuracion_dao = ConfiguracionDAO.ConfiguracionDAO()
                configuracion = configuracion_dao.consultar_config_usuario(informacion_usuario[4])

                usuario = UsuarioVO(ID_usuario=informacion_usuario[0],
                                     fecha_registro=informacion_usuario[1],
                                      email=informacion_usuario[2], 
                                      nombre=informacion_usuario[3], 
                                      configuracion=configuracion)
                # conexion.close()
            return usuario
        except Error as e:
            print(f"Error al consultar por correo {e}")
            return e
        
    def completar_informacion_Usuario(self,usuario_vo:UsuarioVO):
        configuracion_dao = ConfiguracionDAO.ConfiguracionDAO()
        self.usuario_actual = usuario_vo
        # self.usuario_actual


    def actualizar_nombre(self, nuevo_nombre:str, usuario_actual: UsuarioVO):
        try:
            with self.objeto_conexion.crear_conexion() as conexion:

                cursor = conexion.cursor()

                sql = "UPDATE Usuario SET Nombre = ? WHERE ID_Usuario = ?"

                cursor.execute(sql, (nuevo_nombre,usuario_actual.ID_usuario))
                usuario_actual.nombre = nuevo_nombre
                return usuario_actual
        except Error as e:
            print(f"Error al actualizar el nombre {e}")
            return e

    def actualizar_email(self, nuevo_email:str, usuario_actual: UsuarioVO):
        try:
            with self.objeto_conexion.crear_conexion() as conexion:

                cursor = conexion.cursor()

                sql = "UPDATE Usuario SET Email = ? WHERE ID_Usuario = ?"

                cursor.execute(sql, (nuevo_email,usuario_actual.ID_usuario))

                return True
        except Error as e:
            print(f"Error al actualizar el nombre {e}")
            return e