from kivy.uix.screenmanager import Screen
from kivy.lang import Builder
from src.controller.app_controlador import AppControlador


Builder.load_file("src/view/gui/kv/ver_contactos_screen.kv")

class VerContactosScreen(Screen):
    def __init__(self, controlador: AppControlador, **kwargs):
        super().__init__(**kwargs)
        self.controlador: AppControlador = controlador

    def on_enter(self):
        self.mostrar_contactos()

    def mostrar_contactos(self, contactos=None):
        if contactos is None:
            contactos = self.controlador.obtener_contactos()
        datos = [{"text": str(c)} for c in contactos]
        self.ids.lista_contactos.data = datos

    def filtrar_contactos(self):
        tipo = self.ids.filtro_tipo.text.lower()
        nombre = self.ids.filtro_nombre.text.lower()
        telefono = self.ids.filtro_telefono.text.lower()

        contactos = self.controlador.obtener_contactos()
        filtrados = [
            c for c in contactos
            if (tipo in c.tipo.lower() if tipo else True)
               and (nombre in c.nombre.lower() if nombre else True)
               and (telefono in c.telefono.lower() if telefono else True)
        ]
        self.mostrar_contactos(filtrados)