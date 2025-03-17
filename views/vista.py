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
)
from models.VO.UsuarioVO import UsuarioVO
from PyQt5.QtGui import QPixmap
from PyQt5.QtCore import Qt

class StackedManager(QStackedWidget):
    def __init__(self, vista_principal, vista_secundaria):
        super().__init__()
        # In
        self.vista_principal = vista_principal
        self.vista_secundaria = vista_secundaria
        self.setGeometry(100,100,1000,1000)
        self.setWindowTitle("Configuración Waze")
        #Agregamos las vistas al QstackedWidget
        self.addWidget(self.vista_principal)
        self.addWidget(self.vista_secundaria)
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
        self.w['btn_ingresar'] = QPushButton("Ingresar")
        self.w['menu_usuarios'].addItem('Usuarios disponibles')
        self.w['menu_usuarios'].setCurrentIndex(0)
        self.w['menu_usuarios'].setEditable(False)
        self.w['menu_usuarios'].setStyleSheet('padding: 5px; width: 200px; height: 30px; border: 3px solid black; border-radius:10px;')

        self.layout_principal = QVBoxLayout()
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
        self.layout = QVBoxLayout()
        self.w = dict()
        self.w["etiqueta"] = QLabel("Configuracion waze")
        self.w["etiqueta"].setStyleSheet(
            "font-size : 30px; color: blue; font-family: serif; font-weight: bold;"
        )
        self.w["usuario_actual_nombre"] = QLabel()
        self.w["usuario_actual_email"] = QLabel()
        self.w["usuario_actual_fecha"] = QLabel()
        
        self.w["btn_cerrar_sesion"] = QPushButton("cerrar sesion")
        self.setLayout(self.layout)

        for key_w, w in self.w.items():
            self.layout.addWidget(w, alignment=Qt.AlignCenter)
        self.setLayout(self.layout)

    def set_usuario_actual(self, usuario: UsuarioVO):
        self.usuario_actual = usuario
        self.w["usuario_actual_nombre"].setText(self.usuario_actual.nombre)
        self.w["usuario_actual_email"].setText(self.usuario_actual.email)
        self.w["usuario_actual_fecha"].setText(self.usuario_actual.fecha_registro)