from src.model.sistema import Sistema
from src.model.usuario import Usuario
from src.model.contacto import Contacto


class AppControlador:
    def __init__(self):
        self.sistema = Sistema()
        self.usuario_actual: Usuario = None

    def iniciar_sesion(self, nombre: str, contraseña: str):
        usuario = self.sistema.gestor_usuarios.iniciar_sesion(nombre, contraseña)
        self.usuario_actual = usuario
        return usuario

    def registrar_usuario(self, nombre: str, contraseña: str):
        usuario = Usuario(nombre, contraseña)
        self.sistema.gestor_usuarios.registrar_usuario(usuario)

    def crear_contacto(self, tipo: str, nombre: str, telefono: str):
        contacto = Contacto(tipo, nombre, telefono)
        self.usuario_actual.gestor.registrar_contacto(contacto)

    def obtener_contactos(self):
        return self.usuario_actual.gestor.contactos






