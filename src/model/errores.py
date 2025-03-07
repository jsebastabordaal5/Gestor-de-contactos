class ContactoNoEncontradoError(Exception):
    def __init__(self, contacto):
        super().__init__(f"El contacto '{contacto}' no fue encontrado")


class DatosInsuficientesError(Exception):
    # Se lanza cuando no se proporciona al menos un dato para editar un contacto
    def __init__(self):
        super().__init__("Debe proporcionar al menos un dato para modificar el contacto.")


class NumeroInvalidoError(Exception):
    # Se lanza cuando el número de teléfono tiene menos o más de 10 dígitos
    def __init__(self, mensaje="El número de teléfono debe tener exactamente 10 dígitos"):
        super().__init__(mensaje)


class NombreVacioError(Exception):
    # Se lanza cuando el campo de nuevo nombre está vacío
    def __init__(self, mensaje="El nombre no puede estar vacío"):
        super().__init__(mensaje)


class NombreCortoError(Exception):
    # Se lanza cuando el campo de nuevo nombre es demasiado corto
    def __init__(self, mensaje="El nombre es demasiado corto. Debe tener al menos 2 caracteres."):
        """Inicializa la excepción con un mensaje opcional."""
        super().__init__(mensaje)

class ContraseñaVaciaError(Exception):
    def __init__(self, mensaje="Contraseña Vacía"):
        super().__init__(mensaje)




class ErrorSinContactos(Exception):
    def __init__(self, mensaje="No hay contactos para exportar."):
        super().__init__(mensaje)


class ErrorArchivoInexistente(Exception):
    def __init__(self, archivo: str):
        super().__init__(f"El archivo '{archivo}' no existe. Verifique la ruta y el nombre del archivo.")


class ErrorFormatoArchivoInvalido(Exception):
    # Se lanza cuando el archivo tiene un formato diferente al .vcf
    def __init__(self, archivo: str):
        super().__init__(
            f"El archivo '{archivo}' no tiene un formato VCF válido. Verifique el contenido y la estructura.")


class ErrorUsuarioNulo(Exception):
    # se lanza cuando se trata de crear un usuario nulo
    def __init__(self):
        super().__init__("No se puede registrar un usuario nulo. Verifique los datos de entrada.")


class ErrorUsuarioYaExistente(Exception):
    # se lanza cuando se trata de crear un usuario ya existente
    def __init__(self, nombre_usuario):
        super().__init__(f"El usuario '{nombre_usuario}' ya está registrado. Elija un nombre diferente.")

class ErrorUsuarioInexistente(Exception):
    def __init__(self):
        super().__init__(f"Usuario Inexistente")





class NombreLargoError(Exception):
    def __init__(self, nombre):
        super().__init__(f"El nombre'{nombre}' excede los 15 caracteres")


class NombreCortoError(Exception):
    def __init__(self, nombre):
        super().__init__(f"El nombre'{nombre}' es demasiado corto")


class ErrorSinContactos(Exception):
    def __init__(self):
        super().__init__(f"No hay contactos para exportar")


class ErrorArchivoInexistente(Exception):
    def __init__(self):
        super().__init__(f"Formato archivo inexistente")


class ErrorFormatoArchivoInvalido(Exception):
      def __init__(self):
        super().__init__(f"Formato archivo inválido")

class ErrorNombreCaracterInvalido(Exception):
    def __init__(self, nombre):
        super().__init__(f"nombre: {nombre} es inválido")


class ErrorUsuarioExistente(Exception):
    def __init__(self):
        super().__init__(f"El usuario es existente!")


#  pass

class TipoContactoError(Exception):
    def __init__(self, tipo):
        super().__init__(f"El tipo de contacto: {tipo} es inválido")



class DatosNoNumericosError(Exception):
    def __init__(self, telefono):
        super().__init__(f"El telefono: {telefono} no es válido")

class ErrorCriterioInexistente(Exception):
    def __init__(self, criterio):
        super().__init__(f"El criterio: {criterio} es inexistente")








