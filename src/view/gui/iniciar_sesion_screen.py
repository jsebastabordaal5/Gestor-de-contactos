from kivy.uix.popup import Popup
from kivy.uix.screenmanager import Screen
from src.controller.app_controlador import AppControlador
from kivy.lang import Builder
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.label import Label

Builder.load_file("src/view/gui/kv/iniciar_sesion_screen.kv")

class IniciarSesionScreen(Screen):
    def __init__ (self , controlador : AppControlador, **kwargs):
        super().__init__(**kwargs)
        self.controlador: AppControlador= controlador

    def iniciar_sesion(self):
        usuario = self.ids.usuario_input.text.strip()
        contraseña = self.ids.contrasena_input.text.strip()

        if not usuario or not contraseña:
            self.mostrar_popup("Error: completar los 2 campos")
            return

        user = self.controlador.iniciar_sesion(usuario, contraseña)

        if user:
            self.manager.current = "usuario_screen"
        else:
            self.mostrar_popup("Usuario o contraseña incorrectos")

    def mostrar_popup(self, mensaje):
        layout = BoxLayout(orientation='vertical', spacing=10, padding=10)
        layout.add_widget(Label(text=mensaje))
        cerrar_btn = Button(text="Cerrar", size_hint_y=None, height=40)
        layout.add_widget(cerrar_btn)

        popup = Popup(title="Aviso",
                      content=layout,
                      size_hint=(None, None),
                      size=(400, 200),
                      auto_dismiss=False)
        cerrar_btn.bind(on_release=popup.dismiss)
        popup.open()
