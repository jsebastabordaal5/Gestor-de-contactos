from kivy.uix.screenmanager import Screen
from src.controller.app_controlador import AppControlador
from kivy.lang import Builder
from kivy.clock import Clock
from kivy.uix.label import Label
from kivy.uix.popup import Popup



Builder.load_file("src/view/gui/kv/crear_contacto_screen.kv")
class CrearContactoScreen(Screen):

    def __init__(self, controlador: AppControlador, **kwargs):
        super().__init__(**kwargs)
        self.controlador: AppControlador = controlador

    def crear_contacto(self):
        tipo = self.ids.tipo_input.text
        nombre = self.ids.nombre_input.text
        telefono = self.telefono_input.text

        try:
            self.controlador.crear_contacto(tipo, nombre, telefono)
            self.mostrar_popup("¡Contacto creado con éxito!")

            # Esperar 2 segundos antes de cambiar de pantalla
            Clock.schedule_once(lambda dt: self.volver_a_main(), 2)

        except Exception as e:
            self.mostrar_popup(f"Error: {str(e)}")



    def mostrar_popup(self, mensaje):
        popup = Popup(title='Mensaje',
                      content=Label(text=mensaje),
                      size_hint=(None, None), size=(400, 200))
        popup.open()

    def volver_a_main(self):
        self.manager.current = "MainScreen"