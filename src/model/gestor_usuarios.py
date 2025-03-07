from src.model.usuario import Usuario

class GestorUsuarios:

    def __init__(self):
        Usuarios: list[Usuario]

    def iniciar_sesion(self, nombre: str, contraseña: str) -> Usuario:
        pass

    def cerrar_sesion(self):
        pass

    def registrar_usuario(self, Usuario: str) -> Usuario:
        pass

    def eliminar_usuario(self, nombre: str) -> None:
        pass