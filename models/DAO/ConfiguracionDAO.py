from db.Conexion import Conexion
from models.VO.UsuarioVO import UsuarioVO
from models.VO.ConfiguracionVO import ConfiguracionVO
from models.VO.IdiomaVO import IdiomaVO
from models.VO.VozVO import VozVo
from models.DAO.IdiomaDAO import IdiomaDAO
from models.DAO.IconoDAO import IconoDAO
from models.DAO.VozDAO import VozDAO
from models.VO.IconoVO import IconoVO
from typing import List
from sqlite3 import Error

class ConfiguracionDAO:

    def __init__(self):
        self.objeto_conexion = Conexion()

    def configuracion_predeterminada(self)->ConfiguracionVO:
        idioma_dao = IdiomaDAO()
        voz_dao = VozDAO()
        icono_dao = IconoDAO()
        idioma_vo = idioma_dao.consultar_idioma_por_id(2)
        voz_vo = voz_dao.consultar_voz_por_id(2)
        icono_vo = icono_dao.consultar_por_id(IconoVO(ID_Icono=2))
        try:
            with self.objeto_conexion.crear_conexion() as conexion:
                
                sql = """
                    INSERT INTO Configuracion (UnidadesDistancia, Notificaciones, Modo, Placa, ID_Idioma, ID_Voz, ID_Icono)
                    VALUES 
                    ('Kilómetros', 1, 'Día', '0000', 2, 2, 2); 
                """

                cursor = conexion.cursor()
                cursor.execute(sql)
                conexion.commit()
                configuracion_vo = ConfiguracionVO(Id_configuracion=cursor.lastrowid,unidadDistancia='Kilómetros',notificaciones= 1,modo='Día', placa='0000',idioma= idioma_vo,voz=voz_vo,icono=icono_vo)

                return configuracion_vo
        except Error as e:
            print(f'Hubo un erro en la configuracion: {e}')
            return False
        
    def eliminar_configuracion(self,configuracion_eliminar: ConfiguracionVO)->ConfiguracionVO:
        try:
            with self.objeto_conexion.crear_conexion() as conexion:
                sql = "DELETE FROM Configuracion WHERE id_configuracion = ?;"
                cursor = conexion.cursor()
                cursor.execute(sql,(configuracion_eliminar.Id_configuracion,))
                conexion.commit()

            return True
                
        except Error as e:
            print(f"Hubo un error al momento de eliminar la configuraciond del usuario {e}")
            return False
            
            



    def consultar_config_usuario(self, id_configuracion ):
        try:
            with self.objeto_conexion.crear_conexion() as conexion:

                cursor = conexion.cursor()

                sql = "SELECT * FROM Configuracion WHERE id_configuracion = ?"

                cursor.execute(sql, (id_configuracion,))

                info_configuracion = cursor.fetchone()

                idioma_dao = IdiomaDAO()
                voz_dao = VozDAO()
                icono_dao = IconoDAO()
                icono_vo = IconoVO(ID_Icono=info_configuracion[7])

                notificaciones = None
                if info_configuracion[2] == 1:
                    notificaciones = True
                else:
                    notificaciones = False
                configuracion = ConfiguracionVO(Id_configuracion=info_configuracion[0],
                                                unidadDistancia=info_configuracion[1], 
                                                notificaciones=notificaciones,
                                                modo=info_configuracion[3], 
                                                placa=info_configuracion[4],
                                                idioma=idioma_dao.consultar_idioma_por_id(info_configuracion[5]),
                                                voz=voz_dao.consultar_voz_por_id(id_voz=info_configuracion[6]),
                                                icono=icono_dao.consultar_por_id(icono=icono_vo)
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

                conexion.commit()

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
    
    def cambiar_icono(self, icono: IconoVO, usuario_actual: UsuarioVO)-> bool:
        try:
            with self.objeto_conexion.crear_conexion() as conexion:
                # Se instancia el cursor a la base de datos
                cursor = conexion.cursor()
                # Se escribe la sentencia sql
                sql = "UPDATE Configuracion SET ID_Icono = ? WHERE id_configuracion = ?;"
                # Se ejeucta la sentencia
                cursor.execute(sql, (icono.ID_Icono, usuario_actual.configuracion.Id_configuracion,))

                conexion.commit()

                return True
            
        except Error as e:
            # Se imprime el error de la base de datos
            print(f"Error al actualizar Icono: {e}")
        

    
    def actualizar_notificaciones(self, usuario_actual:UsuarioVO):
        try:
            with self.objeto_conexion.crear_conexion() as conexion:
                cursor = conexion.cursor()
                sql = "UPDATE Configuracion SET Notificaciones = ? WHERE id_configuracion = ?"


                cursor.execute(sql, (not usuario_actual.configuracion.notificaciones,usuario_actual.configuracion.Id_configuracion,))

                conexion.commit()

                return True
        except Error as e:
            # Se imprime el error de la base de datos
            print(f"Error al actualizar notificaciones: {e}")  
            

    def actualizar_modo(self, usuario_actual:UsuarioVO, nuevo_estado_modo:str):
        try:
            with self.objeto_conexion.crear_conexion() as conexion:
                cursor = conexion.cursor()
                sql = "UPDATE Configuracion SET Modo = ? WHERE id_configuracion = ?"


                cursor.execute(sql, (nuevo_estado_modo,usuario_actual.configuracion.Id_configuracion,))

                conexion.commit()

                return True
        except Error as e:
            # Se imprime el error de la base de datos
            print(f"Error al actualizar modo: {e}")  

    def actualizar_placa(self, usuario_actual:UsuarioVO, nueva_placa:str):
        try:
            with self.objeto_conexion.crear_conexion() as conexion:
                cursor = conexion.cursor()
                sql = "UPDATE Configuracion SET Placa = ? WHERE id_configuracion = ?"


                cursor.execute(sql, (nueva_placa,usuario_actual.configuracion.Id_configuracion,))

                conexion.commit()

                return True
        except Error as e:
            # Se imprime el error de la base de datos
            print(f"Error al actualizar la placa: {e}")  


    def actualizar_unidades_distancia(self, usuario_actual:UsuarioVO, unidad_distancia:str):
        try:
            with self.objeto_conexion.crear_conexion() as conexion:
                cursor = conexion.cursor()
                sql = "UPDATE Configuracion SET UnidadesDistancia = ? WHERE id_configuracion = ?"


                cursor.execute(sql, (unidad_distancia,usuario_actual.configuracion.Id_configuracion,))

                conexion.commit()

                return True
        except Error as e:
            # Se imprime el error de la base de datos
            print(f"Error al actualizar las unidades de distancia: {e}")  

 