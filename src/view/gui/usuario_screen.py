from kivy.uix.screenmanager import Screen
from src.controller.app_controlador import AppControlador
from kivy.lang import Builder

Builder.load_file("src/view/gui/kv/usuario_screen.kv")


class UsuarioScreen(Screen):
    def __init__(self, controlador: AppControlador, **kwargs):
        super().__init__(**kwargs)
        self.controlador: AppControlador = controlador

    def ver_contactos(self):
        pass

    def crear_contacto(self):
        pass

    def editar_contacto(self):
        pass

    def importar_contactos(self):
        pass

    def exportar_contactos(self):
        pass


