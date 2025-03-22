from src.model.usuario import Usuario, u
from src.model.errores import

class GestorUsuarios:

    def __init__(self):
        self.usuarios: list[Usuario] = []

    def iniciar_sesion(self, nombre: str, contraseña: str) -> Usuario:
        usuario = Usuario(nombre, nombre, contraseña)
        if usuario.nombre



    def cerrar_sesion(self) -> None:
        pass

    def registrar_usuario(self, Usuario: str) -> Usuario:
        pass

    def eliminar_usuario(self, nombre: str) -> None:
        pass