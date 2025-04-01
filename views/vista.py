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
    def __init__(self, vista_principal, vista_secundaria, vista_direccion, vista_idioma_voz, vista_icono, vista_crear_usuario, vista_modificar_cuenta):
        super().__init__()
        # In
        self.vista_principal = vista_principal
        self.vista_secundaria = vista_secundaria
        self.vista_direccion = vista_direccion
        self.vista_idioma_voz = vista_idioma_voz
        self.vista_icono = vista_icono
        self.vista_crear_usuario = vista_crear_usuario
        self.vista_modificar_cuenta = vista_modificar_cuenta
        self.setGeometry(100,100,1000,1000)
        self.setWindowTitle("Configuración Waze")
        #Agregamos las vistas al QstackedWidget
        self.addWidget(self.vista_principal)
        self.addWidget(self.vista_secundaria)
        self.addWidget(self.vista_direccion)
        self.addWidget(self.vista_idioma_voz)
        self.addWidget(self.vista_icono)
        self.addWidget(self.vista_crear_usuario)
        self.addWidget(self.vista_modificar_cuenta)
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
        self.w['btn_nuevo_usuario'] = QPushButton("Crear nuevo usuario")


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
        self.w1["usuario_actual_idioma"] = QLabel()
        self.w1["usuario_actual_voz"] = QLabel()
        self.w['btn_direccion'] = QPushButton("Direcciones")
        self.w['btn_idioma'] = QPushButton("Idioma y Voz")
        self.w['btn_icono'] = QPushButton('Iconos')
        self.w["btn_cerrar_sesion"] = QPushButton("cerrar sesion")
        self.w["btn_modificar_cuenta"] = QPushButton("Modificar Cuenta")
        self.w["btn_eliminar_usuario"] = QPushButton("Eliminar mi cuenta")
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
        self.w1["usuario_actual_idioma"].setText(self.usuario_actual.configuracion.idioma.nombre_idioma)
        self.w1["usuario_actual_voz"].setText(self.usuario_actual.configuracion.voz.Tipo_voz)
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
        self.w['btn_eliminar_direccion'] = QPushButton('Eliminar Direccion')
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
        self.w['btn_regresar_vista_sec'] = QPushButton("Regresar")

        self.layout_principal = QVBoxLayout()
        
        for key_w,w in self.w.items():
            self.layout_principal.addWidget(w)
        
        self.setLayout(self.layout_principal)


class VistaIcono(QWidget):
    def __init__(self):
        super().__init__()
        self.indice = 4
        self.w = dict()
        self.w['label_icono'] = QLabel("Icono selecionado:")
        self.w['label_imagen_icono'] = QLabel()
        self.w['menu_iconos'] = QLabel('Menu Iconos')
        self.w['tabla_iconos'] = QTableWidget()
        self.w['btn_cambiar'] = QPushButton('Cambiar imagen')
        self.w['btn_regresar_vista_sec'] = QPushButton('Regresar')
        self.layout_principal = QVBoxLayout()

        for key_w, w in self.w.items():
            self.layout_principal.addWidget(w)

        self.w['tabla_iconos'].setSelectionBehavior(QTableWidget.SelectRows)
        self.setLayout(self.layout_principal)

    def agregarImagen(self,imagen):
        pixmap =QPixmap(imagen)
        self.w['label_imagen_icono'].setPixmap(pixmap)
        

class VistaCrearUsuario(QWidget):
    def __init__(self):
        super().__init__()
        self.indice = 5
        self.w = dict()
        self.w['label_nuevo_nombre'] = QLabel('Ingrese el nombre: ')
        self.w['input_nuevo_nombre'] = QLineEdit()
        self.w['label_nuevo_direcciones'] = QLabel('Ingrese el email: ')
        self.w['input_nuevo_email'] = QLineEdit()
        self.w['btn_nuevo_usuario'] = QPushButton('Guardar nuevo usuario')
        self.w['regresar'] = QPushButton('Regresar')

        self.layout_principal = QVBoxLayout()
        for key, w in self.w.items():
            self.layout_principal.addWidget(w)
        
        self.setLayout(self.layout_principal)
    
class VistaEliminarUsuario(QDialog):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Eliminar usuario")
        self.setGeometry(100,100,500,500)
        self.w = dict()
        self.w['label_eliminar'] = QLabel("Esta seguro de eliminar el usuario")
        self.w['btn_elminar'] = QPushButton("Aceptar")
        self.w['btn_cancelar'] = QPushButton("Cancelar")

        self.layout_principal = QVBoxLayout()
        for key,w in self.w.items():
            self.layout_principal.addWidget(w)
        
        self.setLayout(self.layout_principal)
        self.w['btn_elminar'].clicked.connect(self.accept)
        self.w['btn_cancelar'].clicked.connect(self.accept)

class VistaModificarCuenta(QWidget):
    def __init__(self):
        super().__init__()
        self.indice = 6
        self.w = dict()
        self.w["label_nombre"] = QLabel("Ingresa el nombre nuevo")
        self.w["input_nombre_usuario"] = QLineEdit()
        self.w["btn_cambiar_nombre"] = QPushButton("Cambiar Nombre")
        self.w["label_email"] = QLabel("Ingresa el nuevo email")
        self.w["input_email_usuario"] = QLineEdit()
        self.w["btn_cambiar_email"] = QPushButton("Cambiar Email")
        self.w['estado_unidades'] = QLabel()
        self.w["menu_unidades_distancia"] = QComboBox()
        self.w['menu_unidades_distancia'] = QComboBox()
        self.w['menu_unidades_distancia'].addItem('Selecciona unidad de ditancia')
        self.w['menu_unidades_distancia'].setCurrentIndex(0)
        self.w['menu_unidades_distancia'].setEditable(False)
        self.w['estado_notificaciones'] = QLabel()
        self.w['btn_togle_notificaciones'] = QPushButton("Activar/Desactivar")
        self.w['estado_modo'] = QLabel()
        self.w['menu_modo'] = QComboBox()
        self.w['menu_modo'].addItem('Modos Disponibles')
        self.w['menu_modo'].setCurrentIndex(0)
        self.w['menu_modo'].setEditable(False)
        self.w['label_placa'] = QLabel('Ingresa la placa')
        self.w['input_placa'] = QLineEdit()
        self.w['btn_cambiar_placa'] = QPushButton('Cambiar Placa')
        self.w['btn_regresar'] = QPushButton("Regresar")

        self.layout_principal = QVBoxLayout()

        for key, w in self.w.items():
            self.layout_principal.addWidget(w)

        self.setLayout(self.layout_principal)

    def set_config_actual(self, usuario_actual:UsuarioVO):
        if usuario_actual.configuracion.notificaciones:
            self.w['estado_notificaciones'].setText("Activado")
        else:
            self.w['estado_notificaciones'].setText("Desactivado")
        self.w['estado_modo'].setText(usuario_actual.configuracion.modo)
        self.w['label_placa'].setText(usuario_actual.configuracion.placa)
        self.w['estado_unidades'].setText(usuario_actual.configuracion.unidadDistancia)
    


