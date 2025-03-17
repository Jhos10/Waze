from PyQt5.QtWidgets import QApplication
from views.vista import StackedManager
from models.DAO import UsuarioDAO
from views.vista import VistaPrincipal, VistaSecundaria

import sys
class Controlador:

    def __init__(self):
        # Instanciar la aplicación
        self.app = QApplication(sys.argv)

        vista_principal = VistaPrincipal()
        vista_secundaria = VistaSecundaria()
        # Instanaciar vista_stacked
        self.stacked_manager = StackedManager(vista_principal=vista_principal, vista_secundaria=vista_secundaria)

        self.usuario_dao = UsuarioDAO.UsuarioDAO()

        self.stacked_manager.vista_principal.llenar_menu_usuarios(self.usuario_dao.consultar())

    # Metodo que contiene los handlers del proyecto
    def _setup_handlers(self):

        
        # handler cambiar vista secundaria
        def handler_cambiar_vista_secundaria():
            self.stacked_manager.cambiar_vista(self.stacked_manager.vista_secundaria.indice)

        # Conectar el botón de la vista principal para cambiar de vista

        def handler_usuario_selected(x):
            print("cambiando usuario",x)


        self.stacked_manager.vista_principal.w["menu_usuarios"].activated[str].connect(handler_usuario_selected)
    def mainloop(self):
        # Configurar los handlers
        self._setup_handlers()

        # Mostrar el QStackedWidget (que contiene ambas vistas)
        self.stacked_manager.show()

        # Ejecutar la aplicación
        sys.exit(self.app.exec_())
