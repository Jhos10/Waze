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
from PyQt5.QtGui import QPixmap
from PyQt5.QtCore import Qt

class StackedManager(QStackedWidget):
    def __init__(self, vista_principal, vista_secundaria):
        super().__init__()
        # In
        self.vista_principal = vista_principal
        self.vista_secundaria = vista_secundaria
        self.setGeometry(100,100,1000,1000)
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
        self.setWindowTitle("Configuración Waze")
        self.indice = 0
        self.w = dict()
        self.w['imagen_waze'] = QLabel()
        self.w['imagen_waze'].setPixmap(pixmap)
        self.w['title'] = QLabel('Selecciona tu Email:')
        self.w['title'].setStyleSheet('font-size : 30px; color: blue;')
        self.w["menu_usuarios"] = QComboBox()
        self.w['btn_ingresar'] = QPushButton("Ingresar")
        self.w['menu_usuarios'].addItem('Usuarios disponibles')
        self.w['menu_usuarios'].setCurrentIndex(0)
        self.w['menu_usuarios'].setEditable(False)
        self.w['menu_usuarios'].setStyleSheet('padding: 5px; width: 120px; height: 30px; border: 3px solid black; border-radius:10px;')

        self.layout_principal = QVBoxLayout()
        for key_w, w in self.w.items():
            self.layout_principal.addWidget(w, alignment=Qt.AlignCenter)
        
        self.setLayout(self.layout_principal)
    
    def llenar_menu_usuarios(self, lista_usuarios):
        self.w["menu_usuarios"].addItems([x.email for x in lista_usuarios])


    
        # self.setLayout(self.layout_principal)
    # self.w['menu_usuarios'].setPlaceholderText("Usuarios disponibles:")

class VistaSecundaria(QWidget):

    def __init__(self):
        super().__init__()

        self.setWindowTitle('pantalla secundaria')
        self.indice = 1
        self.layout = QVBoxLayout()
        etiqueta  = QLabel('Pantalla secundaria')
        self.layout.addWidget(etiqueta)
        self.setLayout(self.layout)

        