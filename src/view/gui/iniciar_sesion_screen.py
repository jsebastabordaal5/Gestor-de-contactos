
from kivy.uix.screenmanager import Screen
from src.controller.app_controlador import AppControlador
from kivy.lang import Builder

Builder.load_file("src/view/gui/kv/iniciar_sesion_screen.kv")

class IniciarSesionScreen(Screen):
    def __init__ (self , controlador : AppControlador, **kwargs):
        super().__init__(**kwargs)
        self.controlador: AppControlador= controlador

    def iniciar_sesion(self):
        usuario= self.ids.usuario_input.text
        contraseña= self.ids.contrasena_input.text
        user= self.controlador.iniciar_sesion(usuario,contraseña)

        if user:
            self.manager.current = "usuario_screen"

