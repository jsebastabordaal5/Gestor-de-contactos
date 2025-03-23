from src.model.usuario import Usuario
from src.model.errores import ErrorUsuarioExistente, ErrorCredencialesIncorrectas


class GestorUsuarios:

    def __init__(self):
        self.usuarios: list[Usuario] = []


    def registrar_usuario(self, usuario: Usuario)-> None:
        for u in self.usuarios:
            if u.nombre == usuario.nombre:
                raise ErrorUsuarioExistente("El usuario ya existe")
            else:
                self.usuarios.append(usuario)


    def iniciar_sesion(self, nombre: str, contraseña: str) -> Usuario | None:
        for usuario in self.usuarios:
            if usuario.nombre == nombre and usuario.contraseña == contraseña :
                print("Sesión iniciada exitosamente")
                return usuario
            else:
                raise ErrorCredencialesIncorrectas("Nombre o contraseña incorrectas")




    def cerrar_sesion(self) -> None:
        print("sesión cerrada")



    def eliminar_usuario(self, nombre: str) -> None:
        for usuario in self.usuarios:
            if usuario.nombre == nombre:
                self.usuarios.delete(usuario)
                print(f"Usuario{usuario.nombre} eliminado correctamente")
            else:
                print("El usuario no fue encontrado")

