from kivy.uix.screenmanager import Screen
from kivy.app import App
from kivy.uix.popup import Popup
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.button import Button
from src.model.contacto import Contacto
from kivy.lang import Builder


Builder.load_file("src/view/gui/kv/editar_contacto_screen.kv")

class EditarContactoScreen(Screen):
    def __init__(self, contacto: Contacto, **kwargs):
        super().__init__(**kwargs)
        self.contacto_original = contacto

    def on_kv_post(self, base_widget):
        """
        Se ejecuta una vez que el archivo .kv ya fue cargado y los ids están disponibles.
        Cargamos aquí los datos del contacto.
        """
        if self.contacto_original:
            self.ids.nombre_input.text = self.contacto_original.nombre
            self.ids.telefono_input.text = self.contacto_original.telefono
            tipo = self.contacto_original.tipo.lower()
            self.ids.tipo_spinner.text = tipo if tipo in ['personal', 'profesional'] else "Seleccionar tipo"

    def guardar_contacto(self):
        nombre = self.ids.nombre_input.text.strip()
        telefono = self.ids.telefono_input.text.strip()
        tipo = self.ids.tipo_spinner.text.strip().lower()

        if not nombre or not telefono or tipo not in ["personal", "profesional"]:
            self.mostrar_error("Todos los campos son obligatorios y deben ser válidos.")
            return

        app = App.get_running_app()
        app.controlador.actualizar_contacto(self.contacto_original, {
            "nombre": nombre,
            "telefono": telefono,
            "tipo": tipo
        })

        self.manager.current = "usuario_screen"

    def mostrar_error(self, mensaje):
        layout = BoxLayout(orientation='vertical', spacing=10, padding=10)
        layout.add_widget(Label(text=mensaje))
        cerrar_btn = Button(text="Cerrar", size_hint_y=None, height=40)
        layout.add_widget(cerrar_btn)

        popup = Popup(title="Error",
                      content=layout,
                      size_hint=(None, None),
                      size=(400, 200),
                      auto_dismiss=False)
        cerrar_btn.bind(on_release=popup.dismiss)
        popup.open()
