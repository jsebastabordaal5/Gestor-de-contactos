from kivy.app import App
from kivy.uix.screenmanager import ScreenManager
from src.controller.app_controlador import AppControlador
from src.view.gui.main_screen import MainScreen
from src.view.gui.iniciar_sesion_screen import IniciarSesionScreen
from src.view.gui.registrar_usuario import RegistrarUsuarioScreen
from src.view.gui.usuario_screen import UsuarioScreen

class ContactosApp(App):
    def __init__(self, controlador: AppControlador, **kwargs):
        super().__init__(**kwargs)
        self.controlador: AppControlador = controlador

    def build(self):
        screen_manager= ScreenManager()
        screen_manager.add_widget(MainScreen(name="MainScreen", controlador= self.controlador))
        screen_manager.add_widget(IniciarSesionScreen(name="iniciar_sesion_screen", controlador= self.controlador))
        screen_manager.add_widget(RegistrarUsuarioScreen(name="registrar_usuario_screen", controlador= self.controlador))
        screen_manager.add_widget(UsuarioScreen(name="usuario_screen", controlador= self.controlador))

        return screen_manager

