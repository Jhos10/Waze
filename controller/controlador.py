from PyQt5.QtWidgets import QApplication, QTableWidgetItem
from PyQt5.QtGui import QIcon,QPixmap
from PyQt5.QtCore import Qt
from views.vista import StackedManager
from models.DAO import UsuarioDAO,DireccionDAO, ConfiguracionDAO, Configuracion_direcciones_DAO, IdiomaDAO, VozDAO,IconoDAO
from models.VO import DireccionVO,VozVO, IdiomaVO,IconoVO, UsuarioVO
from views.vista import VistaPrincipal, VistaSecundaria,VistaDirecciones, VistaIdiomaVoz,VistaIcono,VistaCrearUsuario, VistaModificarCuenta,VistaEliminarUsuario
import sys
class Controlador:

    def __init__(self):
        # Instanciar la aplicación
        self.app = QApplication(sys.argv)

        vista_principal = VistaPrincipal()
        vista_secundaria = VistaSecundaria()
        vista_direccion = VistaDirecciones()
        vista_idioma_voz = VistaIdiomaVoz()
        vista_icono = VistaIcono()
        vista_nuevo_usuario = VistaCrearUsuario()
        vista_modificar_cuenta = VistaModificarCuenta()
        self.vista_eliminar_usuario = VistaEliminarUsuario()
        # Instanaciar vista_stacked
        self.stacked_manager = StackedManager(vista_principal=vista_principal, vista_secundaria=vista_secundaria,vista_direccion=vista_direccion,vista_idioma_voz=vista_idioma_voz,vista_icono=vista_icono,vista_crear_usuario=vista_nuevo_usuario, vista_modificar_cuenta=vista_modificar_cuenta)

        # Instanciar cada dao
        # Instanciar usuario data acces
        self.usuario_dao = UsuarioDAO.UsuarioDAO()

        # Instanciar direccion data acces
        self.direccion_dao = DireccionDAO.DireccionDAO()
        #Instancia configuracion data acces 
        self.configuracion = ConfiguracionDAO.ConfiguracionDAO()
        #Instancuar configuracion_direcciones 
        self.config_direcciones = Configuracion_direcciones_DAO.ConfiguracionDireccionesDAO()
        #instanciar idioma data acces 
        self.idioma_dao = IdiomaDAO.IdiomaDAO()

        # Instanciar voz data acces
        self.voz_dao = VozDAO.VozDAO()
        
        self.icono_dao = IconoDAO.IconoDAO()

        self.stacked_manager.vista_principal.llenar_menu_usuarios(self.usuario_dao.consultar())

        

    # Metodo que contiene los handlers del proyecto
    def _setup_handlers(self):

        
        #handler cambiar vista principal
        def handler_cambiar_vista_principal():
            self.stacked_manager.vista_principal.w['menu_usuarios'].clear()
            self.stacked_manager.vista_principal.llenar_menu_usuarios(self.usuario_dao.consultar())
            self.stacked_manager.cambiar_vista(self.stacked_manager.vista_principal.indice)

        # handler cambiar vista nuevo usuairo
        def hanler_cambiar_vista_nuevo_usuario():
            self.stacked_manager.cambiar_vista(self.stacked_manager.vista_crear_usuario.indice)

        def handler_agregar_usuario():
            if len(self.stacked_manager.vista_crear_usuario.w['input_nuevo_nombre'].text()) > 3:
                usuario_vo = UsuarioVO.UsuarioVO(email=self.stacked_manager.vista_crear_usuario.w['input_nuevo_email'].text(),nombre=self.stacked_manager.vista_crear_usuario.w['input_nuevo_nombre'].text())
                self.usuario_dao.nuevo_usuario(usuario_vo)
                handler_cambiar_vista_principal()
            

        # handler cambiar vista secundaria
        def handler_cambiar_vista_secundaria():
            # print(self.usuario_dao.usuario_actual)
            self.stacked_manager.cambiar_vista(self.stacked_manager.vista_secundaria.indice)
        
        # handler cambiar vista direccion
        def handler_cambiar_vista_direccion():
            self.stacked_manager.cambiar_vista(self.stacked_manager.vista_direccion.indice)
            print(self.stacked_manager.vista_secundaria.usuario_actual)
            configuracion_usuario = self.stacked_manager.vista_secundaria.usuario_actual.configuracion
            
            lista_direcciones_ids = self.config_direcciones.consultar(configuracion_usuario.Id_configuracion)
            lista_todas_direcciones = self.direccion_dao.consultar()

            lista_direcciones = list(filter(lambda x: True if x.id_direccion in lista_direcciones_ids else False,lista_todas_direcciones))
  
            self.stacked_manager.vista_direccion.w['lista_direcciones'].setColumnCount(1)
            self.stacked_manager.vista_direccion.w['lista_direcciones'].setHorizontalHeaderLabels(
                ['direccion']
            )
            self.stacked_manager.vista_direccion.w['lista_direcciones'].setRowCount(len(lista_direcciones))
            for indice,direccion in enumerate(lista_direcciones):
                self.stacked_manager.vista_direccion.w['lista_direcciones'].setItem(indice,0,QTableWidgetItem(direccion.direccion))

            for direccion in lista_todas_direcciones:
                self.stacked_manager.vista_direccion.w['menu_direcciones'].addItem(direccion.direccion)
            
        def handler_cambiar_vista_idioma_voz():
            self.stacked_manager.cambiar_vista(self.stacked_manager.vista_idioma_voz.indice)
            self.stacked_manager.vista_idioma_voz.w['lista_idiomas'].clear()
            self.stacked_manager.vista_idioma_voz.w['menu_de_voz'].clear()
            
            lista_idiomas = self.idioma_dao.consultar()
            print('imprimiendo lista idiomas ')
            print('-'*50)
            print(lista_idiomas)
            print('-'*50)
            for idioma in lista_idiomas:
                self.stacked_manager.vista_idioma_voz.w['lista_idiomas'].addItem(idioma.nombre_idioma)
            

            lista_voces = self.voz_dao.consultarVoces()
            print("Lista de voces: ")
            print(lista_voces)
            print("----------------")
            for voz in lista_voces:
                self.stacked_manager.vista_idioma_voz.w['menu_de_voz'].addItem(voz.Tipo_voz)

        def handler_cambiar_vista_icono():
            self.stacked_manager.vista_icono.agregarImagen(self.stacked_manager.vista_secundaria.usuario_actual.configuracion.icono.imagen)
            self.stacked_manager.cambiar_vista(self.stacked_manager.vista_icono.indice)

            lista_iconos = self.icono_dao.consultar_iconos()
            self.stacked_manager.vista_icono.w['tabla_iconos'].setColumnCount(3)
            self.stacked_manager.vista_icono.w['tabla_iconos'].setHorizontalHeaderLabels(['id','Tipo icono', 'icono'])
            self.stacked_manager.vista_icono.w['tabla_iconos'].setRowCount(len(lista_iconos))
            print(lista_iconos)
            for indice, icono in enumerate(lista_iconos):
                item = QTableWidgetItem()  # Crear el item correctamente
                imagen = QIcon(icono.imagen)  # Cargar el icono
                item.setIcon(imagen)  # Asignar el icono al item
                self.stacked_manager.vista_icono.w['tabla_iconos'].setItem(indice, 0,QTableWidgetItem(str(icono.ID_Icono)))
                self.stacked_manager.vista_icono.w['tabla_iconos'].setItem(indice, 1,QTableWidgetItem(icono.tipo))
                self.stacked_manager.vista_icono.w['tabla_iconos'].setItem(indice, 2, item)  # Insertar en la tabla

        def hanlder_actualizar_icono():
            icono_seleccionado = self.stacked_manager.vista_icono.w['tabla_iconos'].selectedItems()
            icono_vo = IconoVO.IconoVO(ID_Icono=icono_seleccionado[0].text(),tipo=icono_seleccionado[1].text())
            icono_obtenido = self.icono_dao.consultar_por_id(icono_vo)
            self.configuracion.cambiar_icono(icono=icono_obtenido,usuario_actual=self.stacked_manager.vista_secundaria.usuario_actual)
            self.stacked_manager.vista_secundaria.usuario_actual.configuracion.icono = icono_obtenido
            handler_cambiar_vista_icono()



        def handler_agregar_direccion():
            direccion = self.stacked_manager.vista_direccion.w['menu_direcciones'].currentText()
                
            direccion_vo = self.direccion_dao.consultar_id_direccion(direccion)

        
            self.config_direcciones.nueva_config_direccion(usuario=self.stacked_manager.vista_secundaria.usuario_actual,
                                                            direccion=direccion_vo)

            handler_cambiar_vista_direccion()


         
            
        def handler_guardar_voz():
            voz_seleccionada = self.stacked_manager.vista_idioma_voz.w['menu_de_voz'].currentText()
            if voz_seleccionada != "Selecciona la voz":
                # print(voz_seleccionada)
                voz_vo_seleccionada = VozVO.VozVo(Tipo_voz=voz_seleccionada)
                # print(voz_vo_seleccionada)
                voz_vo = self.voz_dao.consultar_voz_tipo_voz(voz_vo=voz_vo_seleccionada)
                self.configuracion.actualizarVoz(usuario_actual=self.stacked_manager.vista_secundaria.usuario_actual,voz=voz_vo)
                self.stacked_manager.vista_secundaria.usuario_actual.configuracion.voz = voz_vo
                self.stacked_manager.vista_secundaria.set_usuario_actual(self.stacked_manager.vista_secundaria.usuario_actual)
                handler_cambiar_vista_secundaria()
        
        #Handler para actualizar el idioma
        def handler_actualizar_idioma():
            idioma_seleccionado = self.stacked_manager.vista_idioma_voz.w['lista_idiomas'].currentText()
            if idioma_seleccionado != "Idiomas Disponibles":
                idioma_vo = self.idioma_dao.consultar_idioma_por_nombre(idioma=idioma_seleccionado)
                self.configuracion.actualizar_idioma(idioma=idioma_vo, usuario_actual=self.stacked_manager.vista_secundaria.usuario_actual)
                self.stacked_manager.vista_secundaria.usuario_actual.configuracion.idioma = idioma_vo
                self.stacked_manager.vista_secundaria.set_usuario_actual(self.stacked_manager.vista_secundaria.usuario_actual)
                handler_cambiar_vista_secundaria()
 
                
            
        # Conectar el botón de la vista principal para cambiar de vista
        def handler_usuario_selected(x):
            if x != "Usuarios disponibles":
                usuario_vo = self.usuario_dao.consultar_por_correo(x)
                usuario_vo.configuracion = self.configuracion.consultar_config_usuario(usuario_vo.configuracion.Id_configuracion)
                print(usuario_vo.configuracion)
                self.stacked_manager.vista_secundaria.set_usuario_actual(usuario_vo)
                handler_cambiar_vista_secundaria()
        
        def handler_eliminar_direccion():
            direccion = self.stacked_manager.vista_direccion.w['lista_direcciones'].selectedItems()
            direccion_vo = self.direccion_dao.consultar_id_direccion(direccion[0].text())
            self.config_direcciones.eliminar_direcion(direccion=direccion_vo,usuario=self.stacked_manager.vista_secundaria.usuario_actual)
            handler_cambiar_vista_direccion()

        #En construccion!
        def handler_mostrar_eliminar_cuenta():
            self.vista_eliminar_usuario.show()

        def handler_eliminar_cuenta():
            self.usuario_dao.eliminarUsuario(self.stacked_manager.vista_secundaria.usuario_actual)
            handler_cambiar_vista_principal()

        def handler_cancelar_eliminar_cuenta():
            handler_cambiar_vista_secundaria()
            

        def handler_cambiar_vista_modificar_cuenta():
            self.stacked_manager.vista_modificar_cuenta.w["menu_unidades_distancia"].clear()
            self.stacked_manager.vista_modificar_cuenta.w['menu_modo'].clear()


            self.stacked_manager.cambiar_vista(self.stacked_manager.vista_modificar_cuenta.indice)
            self.stacked_manager.vista_modificar_cuenta.w["menu_unidades_distancia"].addItem("Kilómetros")
            self.stacked_manager.vista_modificar_cuenta.w["menu_unidades_distancia"].addItem("Millas")
            self.stacked_manager.vista_modificar_cuenta.w['menu_modo'].addItem('Día')
            self.stacked_manager.vista_modificar_cuenta.w['menu_modo'].addItem('Noche')
            self.stacked_manager.vista_modificar_cuenta.set_config_actual(self.stacked_manager.vista_secundaria.usuario_actual)
        

        def handler_modificar_unidades_de_distancia():
            nueva_unidad_distancia = self.stacked_manager.vista_modificar_cuenta.w['menu_unidades_distancia'].currentText()
            if len(nueva_unidad_distancia) > 0:
                self.configuracion.actualizar_unidades_distancia(usuario_actual=self.stacked_manager.vista_secundaria.usuario_actual, unidad_distancia=nueva_unidad_distancia)
                handler_cambiar_vista_principal()

            

        def handler_modificar_notificaciones():
            self.configuracion.actualizar_notificaciones(usuario_actual=self.stacked_manager.vista_secundaria.usuario_actual)
            handler_cambiar_vista_principal()


        def handler_modificar_modo():
            nuevo_modo = self.stacked_manager.vista_modificar_cuenta.w['menu_modo'].currentText()
            if nuevo_modo != "Modos Disponibles":
                self.configuracion.actualizar_modo(usuario_actual=self.stacked_manager.vista_secundaria.usuario_actual, nuevo_estado_modo=nuevo_modo)
                handler_cambiar_vista_principal()
            
        def handler_modificar_placa():
            nueva_placa = self.stacked_manager.vista_modificar_cuenta.w['input_placa'].text()
            if len(nueva_placa) >= 6:
                self.configuracion.actualizar_placa(usuario_actual=self.stacked_manager.vista_secundaria.usuario_actual, nueva_placa=nueva_placa)
                handler_cambiar_vista_principal()
        
        def handler_modificar_email():
            nuevo_email = self.stacked_manager.vista_modificar_cuenta.w["input_email_usuario"].text()
            if len(nuevo_email) > 5:
                self.usuario_dao.actualizar_email(nuevo_email=nuevo_email,usuario_actual=self.stacked_manager.vista_secundaria.usuario_actual)
                handler_cambiar_vista_principal()
                


        def handler_modificar_nombre():
            nuevo_nombre = self.stacked_manager.vista_modificar_cuenta.w["input_nombre_usuario"].text()
            print(nuevo_nombre)
            if len(nuevo_nombre) > 2:
                print("Ingreso ")
                self.stacked_manager.vista_secundaria.usuario_actual = self.usuario_dao.actualizar_nombre(nuevo_nombre=nuevo_nombre,usuario_actual=self.stacked_manager.vista_secundaria.usuario_actual)
                print(self.stacked_manager.vista_secundaria.usuario_actual)
                self.stacked_manager.vista_secundaria.set_usuario_actual(self.stacked_manager.vista_secundaria.usuario_actual)
                handler_cambiar_vista_secundaria()
                

            



        
            

        #Asignar los botones de la vista principal
        self.stacked_manager.vista_principal.w["menu_usuarios"].activated[str].connect(handler_usuario_selected)
        self.stacked_manager.vista_principal.w["btn_nuevo_usuario"].clicked.connect(hanler_cambiar_vista_nuevo_usuario)
        #Asignar los botones de la vista secundaria
        self.stacked_manager.vista_secundaria.w["btn_cerrar_sesion"].clicked.connect(handler_cambiar_vista_principal)
        self.stacked_manager.vista_secundaria.w['btn_direccion'].clicked.connect(handler_cambiar_vista_direccion)
        self.stacked_manager.vista_secundaria.w['btn_icono'].clicked.connect(handler_cambiar_vista_icono)
        self.stacked_manager.vista_secundaria.w['btn_idioma'].clicked.connect(handler_cambiar_vista_idioma_voz)
        self.stacked_manager.vista_secundaria.w["btn_eliminar_usuario"].clicked.connect(handler_mostrar_eliminar_cuenta)
        self.stacked_manager.vista_secundaria.w["btn_modificar_cuenta"].clicked.connect(handler_cambiar_vista_modificar_cuenta)

        #Asignar botones de la vista direccion
        self.stacked_manager.vista_direccion.w['btn_nueva'].clicked.connect(handler_agregar_direccion) 
        self.stacked_manager.vista_direccion.w['bt_regresar_vista_sec'].clicked.connect(handler_cambiar_vista_secundaria)
        self.stacked_manager.vista_direccion.w['btn_eliminar_direccion'].clicked.connect(handler_eliminar_direccion)

        # Asignar botones de la vista idioma_voz
        self.stacked_manager.vista_idioma_voz.w['btn_guardar_idioma'].clicked.connect(handler_actualizar_idioma)
        self.stacked_manager.vista_idioma_voz.w['btn_guardar_voz'].clicked.connect(handler_guardar_voz)
        self.stacked_manager.vista_idioma_voz.w['btn_regresar_vista_sec'].clicked.connect(handler_cambiar_vista_secundaria)


        #Asignar botones de la vista Icono 
        self.stacked_manager.vista_icono.w['btn_regresar_vista_sec'].clicked.connect(handler_cambiar_vista_secundaria)
        self.stacked_manager.vista_icono.w['btn_cambiar'].clicked.connect(hanlder_actualizar_icono)

        # Asignar señales de los botones de la vista de crear nuevo usuario
        self.stacked_manager.vista_crear_usuario.w['btn_nuevo_usuario'].clicked.connect(handler_agregar_usuario)
        self.stacked_manager.vista_crear_usuario.w['regresar'].clicked.connect(handler_cambiar_vista_principal)

        #Asignar señales de los botones de la vista modificar cuenta 
        # self.stacked_manager.vista_modificar_cuenta.w[""]
        self.stacked_manager.vista_modificar_cuenta.w['btn_togle_notificaciones'].clicked.connect(handler_modificar_notificaciones)
        self.stacked_manager.vista_modificar_cuenta.w['menu_modo'].activated[str].connect(handler_modificar_modo)
        self.stacked_manager.vista_modificar_cuenta.w['menu_unidades_distancia'].activated[str].connect(handler_modificar_unidades_de_distancia)
        self.stacked_manager.vista_modificar_cuenta.w['btn_cambiar_placa'].clicked.connect(handler_modificar_placa)
        self.stacked_manager.vista_modificar_cuenta.w["btn_cambiar_nombre"].clicked.connect(handler_modificar_nombre)
        self.stacked_manager.vista_modificar_cuenta.w["btn_cambiar_email"].clicked.connect(handler_modificar_email)
        self.stacked_manager.vista_modificar_cuenta.w["btn_regresar"].clicked.connect(handler_cambiar_vista_secundaria)

        # Asignar señales de los eventos de la ventana eliminar usuario
        self.vista_eliminar_usuario.w['btn_elminar'].clicked.connect(handler_eliminar_cuenta)
        self.vista_eliminar_usuario.w['btn_cancelar'].clicked.connect(handler_cancelar_eliminar_cuenta)


    
    def mainloop(self):
        # Configurar los handlers
        self._setup_handlers()

        # Mostrar el QStackedWidget (que contiene ambas vistas)
        self.stacked_manager.show()

        # Ejecutar la aplicación
        sys.exit(self.app.exec_())
