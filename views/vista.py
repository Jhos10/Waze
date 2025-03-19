from PyQt5.QtWidgets import (
    QPushButton,
    QVBoxLayout,
    QTableWidget,
    QTableWidgetItem,
    QSlider,
    QLabel,
    QWidget,
    QDialog,
    QLineEdit,
    QComboBox,
    QStackedWidget,
    QHBoxLayout,
)
from models.VO.UsuarioVO import UsuarioVO
from PyQt5.QtGui import QPixmap
from PyQt5.QtCore import Qt

class StackedManager(QStackedWidget):
    def __init__(self, vista_principal, vista_secundaria, vista_direccion, vista_idioma_voz, vista_icono):
        super().__init__()
        # In
        self.vista_principal = vista_principal
        self.vista_secundaria = vista_secundaria
        self.vista_direccion = vista_direccion
        self.vista_idioma_voz = vista_idioma_voz
        self.vista_icono = vista_icono
        self.setGeometry(100,100,1000,1000)
        self.setWindowTitle("Configuración Waze")
        #Agregamos las vistas al QstackedWidget
        self.addWidget(self.vista_principal)
        self.addWidget(self.vista_secundaria)
        self.addWidget(self.vista_direccion)
        self.addWidget(self.vista_idioma_voz)
        self.addWidget(self.vista_icono)
        self.setCurrentIndex(self.vista_principal.indice)

    def cambiar_vista(self, indice):
        self.setCurrentIndex(indice)
    

class VistaPrincipal(QWidget):

    def __init__(self):
        super().__init__()
        
        pixmap = QPixmap('.\\images\\waze-icon.svg')
        self.indice = 0
        self.w = dict()
        self.w['imagen_waze'] = QLabel()
        self.w['imagen_waze'].setPixmap(pixmap)
        self.w['title'] = QLabel('Selecciona tu Email:')
        self.w["title"].setStyleSheet(
            "font-size : 30px; color: blue; font-family: serif; font-weight: bold;"
        )
        self.w["menu_usuarios"] = QComboBox()
        self.w['menu_usuarios'].addItem('Usuarios disponibles')
        self.w['menu_usuarios'].setCurrentIndex(0)
        self.w['menu_usuarios'].setEditable(False)
        self.w['menu_usuarios'].setStyleSheet('padding: 5px; width: 200px; height: 30px; border: 3px solid black; border-radius:10px;')

        self.layout_principal = QHBoxLayout()
        for key_w, w in self.w.items():
            self.layout_principal.addWidget(w, alignment=Qt.AlignCenter)
        
        self.setLayout(self.layout_principal)
    
    def llenar_menu_usuarios(self, lista_usuarios):
        self.w["menu_usuarios"].addItems([x.email for x in lista_usuarios])


    
        # self.setLayout(self.layout_principal)
    # self.w['menu_usuarios'].setPlaceholderText("Usuarios disponibles:")

class VistaSecundaria(QWidget):

    def __init__(self, usuario_actual : UsuarioVO = None):
        super().__init__()

        self.usuario_actual = usuario_actual
        self.indice = 1
        self.layout_principal = QVBoxLayout()
        self.layout_1 = QHBoxLayout()
        self.layout_2 = QHBoxLayout()
        self.layout_principal.addLayout(self.layout_1)
        self.layout_principal.addLayout(self.layout_2)
        self.w = dict()
        self.w1 = dict()
        self.w1["etiqueta"] = QLabel("Configuracion waze")
        self.w1["etiqueta"].setStyleSheet(
            "font-size : 30px; color: blue; font-family: serif; font-weight: bold;"
        )
        self.w1["usuario_actual_nombre"] = QLabel()
        self.w1["usuario_actual_email"] = QLabel()
        self.w1["usuario_actual_fecha"] = QLabel()
        self.w['btn_direccion'] = QPushButton("Direcciones")
        self.w['btn_idioma'] = QPushButton("Idioma y Voz")
        self.w['btn_icono'] = QPushButton('Iconos')
        self.w["btn_cerrar_sesion"] = QPushButton("cerrar sesion")
        self.setLayout(self.layout_principal)
        
        for key_w1, w1 in self.w1.items():
            self.layout_1.addWidget(w1)


        for key_w, w in self.w.items():
            self.layout_principal.addWidget(w, alignment=Qt.AlignCenter)
        self.setLayout(self.layout_principal)
        
        

    def set_usuario_actual(self, usuario: UsuarioVO):
        self.usuario_actual = usuario
        self.w1["usuario_actual_nombre"].setText(self.usuario_actual.nombre)
        self.w1["usuario_actual_email"].setText(self.usuario_actual.email)
        self.w1["usuario_actual_fecha"].setText(self.usuario_actual.fecha_registro)

class VistaDirecciones(QWidget):
    def __init__(self):
        super().__init__()
        # Indice para identificarlo en el stack
        self.indice = 2
        self.w = dict()
        self.w['label_direcciones'] = QLabel('Direcciones guardadas: ')
        self.w['lista_direcciones'] = QTableWidget()
        self.w['label_agregar'] = QLabel('Agregar una nueva direccion: ')
        self.w['menu_direcciones'] = QComboBox()
        self.w['menu_direcciones'].addItem('Agreagr direcciones')
        self.w['menu_direcciones'].setCurrentIndex(0)
        self.w['menu_direcciones'].setEditable(False)
        self.w['btn_nueva'] = QPushButton('Agregar nueva direccion')
        self.w['bt_regresar_vista_sec'] = QPushButton('Regresar 🔙')

        self.layout_principal = QVBoxLayout()

        for key_w,w in self.w.items():
            self.layout_principal.addWidget(w)
        
        self.setLayout(self.layout_principal)

        
class VistaIdiomaVoz(QWidget):
    def __init__(self):
        super().__init__()

        self.indice = 3
        self.w = dict()
        self.w['label_idioma'] = QLabel('Idiomas Disponibles')
        self.w['lista_idiomas'] = QComboBox()
        self.w['lista_idiomas'].setCurrentIndex(0)
        self.w['lista_idiomas'].setEditable(False)
        self.w['btn_guardar_idioma'] = QPushButton('Guardar idioma')
        self.w['label_elige_voz'] = QLabel("Selecciona la voz")
        self.w['menu_de_voz'] = QComboBox()
        self.w['menu_de_voz'].addItem('Seleccion la voz')
        self.w['menu_de_voz'].setCurrentIndex(0)
        self.w['menu_de_voz'].setEditable(False)
        self.w['btn_guardar_voz'] = QPushButton("Guardar voz")

        self.layout_principal = QVBoxLayout()
        
        for key_w,w in self.w.items():
            self.layout_principal.addWidget(w)
        
        self.setLayout(self.layout_principal)


class VistaIcono(QWidget):
    def __init__(self):
        super().__init__()
        self.indice = 4
        self.w = dict()
        self.w['menu_iconos'] = QLabel('Menu Iconos')
        self.w['tabla_iconos'] = QTableWidget()

        self.layout_principal = QVBoxLayout()

        for key_w, w in self.w.items():
            self.layout_principal.addWidget(w)

        self.setLayout(self.layout_principal)        
        