from src.model.usuario import Usuario
from src.model.errores import ErrorUsuarioYaExistente, ContraseñaIncorrectaError, NombreInvalidoError, ErrorUsuarioNulo, ErrorTipoInvalidoUsuario


class GestorUsuarios:

    def __init__(self):
        self.usuarios: list[Usuario] = []


    def registrar_usuario(self, usuario: Usuario):

        if usuario == None:
            raise ErrorUsuarioNulo()

        if not isinstance(usuario, Usuario):
            raise ErrorTipoInvalidoUsuario()

        for user in self.usuarios:
            if user.nombre.strip().lower() == usuario.nombre.strip().lower():
                raise ErrorUsuarioYaExistente(usuario.nombre)

        self.usuarios.append(usuario)
        return

    def iniciar_sesion(self, nombre: str, contraseña: str) -> Usuario | None:
        for usuario in self.usuarios:
            if usuario.nombre == nombre:
                if usuario.contraseña == contraseña:
                    print("Sesión iniciada exitosamente")
                    return usuario
                else:
                    raise ContraseñaIncorrectaError()
            else:
                raise NombreInvalidoError()

    def cerrar_sesion(self) -> None:
        print("sesión cerrada")

    def eliminar_usuario(self, nombre: str) -> None:
        for usuario in self.usuarios:
            if usuario.nombre == nombre:
                self.usuarios.delete(usuario)
                print(f"Usuario{usuario.nombre} eliminado correctamente")
            else:
                print("El usuario no fue encontrado")

