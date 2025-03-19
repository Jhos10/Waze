from db.Conexion import Conexion
from models.VO.UsuarioVO import UsuarioVO
from models.VO.ConfiguracionVO import ConfiguracionVO
from models.VO.IdiomaVO import IdiomaVO
from models.VO.VozVO import VozVo
from typing import List
from sqlite3 import Error

class ConfiguracionDAO:

    def __init__(self):
        self.objeto_conexion = Conexion()

    
    def consultar_config_usuario(self, id_configuracion ):
        try:
            with self.objeto_conexion.crear_conexion() as conexion:

                cursor = conexion.cursor()

                sql = "SELECT * FROM Configuracion WHERE id_configuracion = ?"

                cursor.execute(sql, (id_configuracion,))

                info_configuracion = cursor.fetchone()


                configuracion = ConfiguracionVO(Id_configuracion=info_configuracion[0],
                                                unidadDistancia=info_configuracion[1], 
                                                notificaciones=info_configuracion[2],
                                                modo=info_configuracion[3], 
                                                placa=info_configuracion[4],
                                                )
                
                
            return configuracion
        
        except Error as e:
            print(f"Error al consultar configuracion del usuario {e}")
        
            return configuracion
        
    def actualizar_idioma(self, idioma:IdiomaVO, usuario_actual: UsuarioVO)-> bool:
        try:
            with self.objeto_conexion.crear_conexion() as conexion:
                # Se instancia el cursor a la base de datos
                cursor = conexion.cursor()
                # Se escribe la sentencia sql
                sql = "UPDATE Configuracion SET ID_idioma = ? WHERE id_configuracion = ?;"
                # Se ejeucta la sentencia
                cursor.execute(sql, (idioma.id_idioma, usuario_actual.configuracion.Id_configuracion,))

                cursor.commit()

                return True
            
        except Error as e:
            # Se imprime el error de la base de datos
            print(f"Error al actualizar idioma en la configuracion: {e}")
         
    def actualizarVoz(self,usuario_actual:UsuarioVO,voz:VozVo):
        try:
            with self.objeto_conexion.crear_conexion() as conexion:
                sql = """
                    UPDATE Configuracion
                    SET ID_voz = ? WHERE id_configuracion = ?;
                """

                cursor = conexion.cursor()
                cursor.execute(sql,(voz.ID_voz,usuario_actual.configuracion.Id_configuracion,))
                conexion.commit()
        except Error as e:
            print(f"Hubo un error al momento de actualizar la voz en la configuracion {e}")
        
    # def cambiar_icono(self, icono: IconoVO, usuario_actual: UsuarioVO)-> bool:
    #     try:
    #         with self.objeto_conexion.crear_conexion() as conexion:
    #             # Se instancia el cursor a la base de datos
    #             cursor = conexion.cursor()
    #             # Se escribe la sentencia sql
    #             sql = "UPDATE Configuracion SET ID_Icono = ? WHERE id_configuracion = ?;"
    #             # Se ejeucta la sentencia
    #             cursor.execute(sql, (icono.tipo_icono, usuario_actual.configuracion.Id_configuracion,))

    #             cursor.commit()

    #             return True
            
    #     except Error as e:
    #         # Se imprime el error de la base de datos
    #         print(f"Error al actualizar Icono: {e}")

 