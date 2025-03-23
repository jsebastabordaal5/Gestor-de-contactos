from src.model.gestor_contactos import GestorContactos
from src.model.contacto import Contacto
class Usuario:
    def __init__(self, nombre : str , contraseña : str):
        self.nombre= nombre
        self.contraseña = contraseña
        self.gestor= GestorContactos()

    def __str__(self):
        return f"Nombre: {self.nombre}, Contraseña : {self.contraseña}"

    def registrar_contacto(self, tipo: str, nombre: str, telefono: str) -> Contacto:
        contacto = Contacto(tipo, nombre, telefono)
        self.gestor.registrar_contacto(contacto)

    def ver_contactos(self) -> Contacto:
        pass