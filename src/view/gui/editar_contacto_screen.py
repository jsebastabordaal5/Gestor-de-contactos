from kivy.uix.screenmanager import Screen
from kivy.properties import ObjectProperty
from kivy.app import App
from kivy.uix.popup import Popup
from kivy.uix.label import Label
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.lang import Builder

Builder.load_file("src/view/gui/kv/editar_contacto_screen.kv")

class EditarContactoScreen(Screen):
    contacto_original = ObjectProperty(None)

    def on_pre_enter(self):
        if not self.contacto_original:
            self.ids.nombre_input.text = ""
            self.ids.telefono_input.text = ""
            self.ids.tipo_spinner.text = "Seleccionar tipo"

    def cargar_contacto(self, contacto):
        """
        Recibe un diccionario con los datos del contacto original
        y los coloca en los campos del formulario.
        """
        self.contacto_original = contacto

        self.ids.nombre_input.text = contacto.get('nombre', '')
        self.ids.telefono_input.text = contacto.get('telefono', '')
        tipo = contacto.get('tipo', '').lower()
        self.ids.tipo_spinner.text = tipo if tipo in ['personal', 'profesional'] else "Seleccionar tipo"

    def guardar_contacto(self):
        """
        Valida y guarda los cambios realizados al contacto.
        """
        nombre = self.ids.nombre_input.text.strip()
        telefono = self.ids.telefono_input.text.strip()
        tipo = self.ids.tipo_spinner.text.lower()

        if not nombre or not telefono or tipo not in ['personal', 'profesional']:
            self.mostrar_error("Todos los campos son obligatorios y deben ser válidos.")
            return

        contacto_actualizado = {
            'nombre': nombre,
            'telefono': telefono,
            'tipo': tipo
        }

        app = App.get_running_app()
        app.controlador.actualizar_contacto(self.contacto_original, contacto_actualizado)

        # Limpieza y regreso
        self.contacto_original = None
        self.ids.nombre_input.text = ""
        self.ids.telefono_input.text = ""
        self.ids.tipo_spinner.text = "Seleccionar tipo"
        app.root.current = "usuario_screen"

    def mostrar_error(self, mensaje):
        content = BoxLayout(orientation='vertical', spacing=10, padding=10)
        content.add_widget(Label(text=mensaje))

        cerrar_btn = Button(text='Cerrar', size_hint_y=None, height=40)
        content.add_widget(cerrar_btn)

        popup = Popup(title='Error',
                      content=content,
                      size_hint=(None, None),
                      size=(400, 200),
                      auto_dismiss=False)
        cerrar_btn.bind(on_release=popup.dismiss)
        popup.open()
