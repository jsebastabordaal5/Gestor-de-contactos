from src.model.gestor_contactos import GestorContactos
from src.model.contacto import Contacto
class Usuario:
    def __init__(self, nombre : str , contraseña : str):
        self.nombre= nombre.strip()
        self.contraseña = contraseña.strip()
        self.gestor= GestorContactos()

    def __str__(self):
        return f"Nombre: {self.nombre}, Contraseña : {self.contraseña}"

