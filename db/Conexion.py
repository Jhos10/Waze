import sqlite3


class Conexion:
    def __init__(self):
        self.ruta = ".\db\Waze.db"
        self.conexion = None

    def crear_conexion(self):
        try:
            self.conexion = sqlite3.connect(self.ruta)
        except sqlite3.Error as e:
            print("----------------------------")
            print("Error de conexión con la BD")
            print(e)
            print("----------------------------")
        return self.conexion