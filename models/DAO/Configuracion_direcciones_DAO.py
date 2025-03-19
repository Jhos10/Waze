from db.Conexion import Conexion
from models.VO.UsuarioVO import UsuarioVO
from models.VO.ConfiguracionVO import ConfiguracionVO
from models.VO.DireccionVO import DireccionVO
from typing import List
from sqlite3 import Error

class ConfiguracionDireccionesDAO:

    def __init__(self):
        self.objeto_conexion = Conexion()

    
    def consultar(self, id_configuracion ):
        try:
            with self.objeto_conexion.crear_conexion() as conexion:

                cursor = conexion.cursor()

                sql = "SELECT ID_direccion FROM Configuracion_Direcciones WHERE ID_configuracion = ?"

                cursor.execute(sql, (id_configuracion,))
                informacion_config = cursor.fetchall()
                lista_ids_direcciones = [x[0] for x in informacion_config]

                return lista_ids_direcciones
        except Error as e:
            print(f"Error en la consulta: {e}")
            return None
                

    def nueva_config_direccion(self,usuario:UsuarioVO, direccion:DireccionVO):
        try:
            with self.objeto_conexion.crear_conexion() as conexion:
                sql = """
                    INSERT INTO Configuracion_Direcciones (
                        ID_direccion, 
                        ID_configuracion
                    )
                    VALUES (
                        ?,
                        ?
                    )
                """
                cursor = conexion.cursor()
                cursor.execute(sql,(direccion.id_direccion,usuario.configuracion.Id_configuracion,))
                
                conexion.commit()

                return cursor.lastrowid
        except Error as e:
            print(f"Hubo un error al momento de agregar configuracion: {e}")
            