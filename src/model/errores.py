class ContactoNoEncontradoError(Exception):
    """Se lanza cuando un contacto no se encuentra en la lista."""
    pass

class DatosInsuficientesError(Exception):
    """Se lanza cuando no se proporcionan datos para editar un contacto."""
    pass

class NumeroInvalidoError(Exception):
    "se lanza cuando el numero de telefono tiene menos de 10 digitos o mas de 10"
    pass

class NombreVacioError(Exception):
    "se lanza cuando el campo de nuevo nombre es vacio"
    pass

class NombreCortoError(Exception):
    "se lanza cuando el campo de nuevo nombre es muy corto"
    pass

class ErrorSinContactos(Exception):
    "Se lanza cuando no hay contactos para exportar"
    pass

class ErrorArchivoInexistente(Exception):
    "Se lanza cuando el archivo no existe"
    pass

class ErrorFormatoArchivoInvalido(Exception):
    "Se lanza cuando el archivo tiene un formato diferente al .vcf"
    pass