from PyQt5.QtWidgets import QApplication, QTableWidgetItem
from views.vista import StackedManager
from models.DAO import UsuarioDAO,DireccionDAO, ConfiguracionDAO, Configuracion_direcciones_DAO, IdiomaDAO, VozDAO,IconoDAO
from models.VO import DireccionVO,VozVO, IdiomaVO,IconoVO
from views.vista import VistaPrincipal, VistaSecundaria,VistaDirecciones, VistaIdiomaVoz,VistaIcono

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
        # Instanaciar vista_stacked
        self.stacked_manager = StackedManager(vista_principal=vista_principal, vista_secundaria=vista_secundaria,vista_direccion=vista_direccion,vista_idioma_voz=vista_idioma_voz,vista_icono=vista_icono)

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
            self.stacked_manager.cambiar_vista(self.stacked_manager.vista_principal.indice)

        # handler cambiar vista secundaria
        def handler_cambiar_vista_secundaria():
            self.stacked_manager.cambiar_vista(self.stacked_manager.vista_secundaria.indice)
        
        # handler cambiar vista direccion
        def handler_cambiar_vista_direccion():
            self.stacked_manager.cambiar_vista(self.stacked_manager.vista_direccion.indice)
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
            self.stacked_manager.cambiar_vista(self.stacked_manager.vista_icono.indice)
            lista_iconos = self.icono_dao.consultar_iconos()
            
            self.stacked_manager.vista_icono.w['tabla_iconos'].setColumnCount(1)
            self.stacked_manager.vista_icono.w['tabla_iconos'].setHorizontalHeaderLabels(['Icono'])
            self.stacked_manager.vista_icono.w['tabla_iconos'].setRowCount(len(lista_iconos))
            for indice, icono in enumerate(lista_iconos):
                self.stacked_manager.vista_icono.w['tabla_iconos'].setItem(indice,0,QTableWidgetItem(icono.tipo))

        def handler_agregar_direccion():
            direccion = self.stacked_manager.vista_direccion.w['menu_direcciones'].currentText()
                
            direccion_vo = self.direccion_dao.consultar_id_direccion(direccion)

                
            self.config_direcciones.nueva_config_direccion(usuario=self.stacked_manager.vista_secundaria.usuario_actual,
                                                            direccion=direccion_vo)

            handler_cambiar_vista_direccion()


            
            
        def handler_guardar_voz():
            voz_seleccionada = self.stacked_manager.vista_idioma_voz.w['menu_de_voz'].currentText()
            
            voz_vo_seleccionada = VozVO.VozVo(Tipo_voz=voz_seleccionada)

            voz_vo = self.voz_dao.consultar_voz_tipo_voz(voz_vo=voz_vo_seleccionada)

            self.configuracion.actualizarVoz(usuario_actual=self.stacked_manager.vista_secundaria.usuario_actual,voz=voz_vo)

            handler_cambiar_vista_idioma_voz()

        
        #Handler para actualizar el idioma
        def handler_actualizar_idioma():
            idioma_seleccionado = self.stacked_manager.vista_idioma_voz.w['lista_idiomas'].currentText()
            idioma_vo = self.idioma_dao.consultar_idioma_por_nombre(idioma=idioma_seleccionado)
            
            self.configuracion.actualizar_idioma(idioma=idioma_vo, usuario_actual=self.stacked_manager.vista_secundaria.usuario_actual)
            handler_cambiar_vista_idioma_voz()
 
                
            
        # Conectar el botón de la vista principal para cambiar de vista
        def handler_usuario_selected(x):
            usuario_vo = self.usuario_dao.consultar_por_correo(x)
            self.stacked_manager.vista_secundaria.set_usuario_actual(usuario_vo)
            handler_cambiar_vista_secundaria()

            # self.stacked_manager.vista_secundaria.usuario_actual = usuario_vo

        #Asignar los botones de la vista principal
        self.stacked_manager.vista_principal.w["menu_usuarios"].activated[str].connect(handler_usuario_selected)
        #Asignar los botones de la vista secundaria
        self.stacked_manager.vista_secundaria.w["btn_cerrar_sesion"].clicked.connect(handler_cambiar_vista_principal)
        self.stacked_manager.vista_secundaria.w['btn_direccion'].clicked.connect(handler_cambiar_vista_direccion)
        self.stacked_manager.vista_secundaria.w['btn_icono'].clicked.connect(handler_cambiar_vista_icono)

        #Asignar botones de la vista direccion
        self.stacked_manager.vista_direccion.w['btn_nueva'].clicked.connect(handler_agregar_direccion) 
        self.stacked_manager.vista_direccion.w['bt_regresar_vista_sec'].clicked.connect(handler_cambiar_vista_secundaria)
        self.stacked_manager.vista_secundaria.w['btn_idioma'].clicked.connect(handler_cambiar_vista_idioma_voz)

        # Asignar botones de la vista idioma
        self.stacked_manager.vista_idioma_voz.w['btn_guardar_idioma'].clicked.connect(handler_actualizar_idioma)
        self.stacked_manager.vista_idioma_voz.w['btn_guardar_voz'].clicked.connect(handler_guardar_voz)
    def mainloop(self):
        # Configurar los handlers
        self._setup_handlers()

        # Mostrar el QStackedWidget (que contiene ambas vistas)
        self.stacked_manager.show()

        # Ejecutar la aplicación
        sys.exit(self.app.exec_())
