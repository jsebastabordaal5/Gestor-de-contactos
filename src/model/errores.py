class ContactoNoEncontradoError(Exception):
    """Se lanza cuando un contacto no se encuentra en la lista."""
    pass

class DatosInsuficientesError(Exception):
    """Se lanza cuando no se proporcionan datos para editar un contacto."""
    pass

class NumeroInvalidoError(Exception):
    "se lanza cuando el numero de telefono tiene menos de 10 digitos o mas de 10"
    pass

class CampoVacio(Exception):
    "se lanza cuando los campos es vacio"
    pass

class NumeroLargoError(Exception):
    "se lanza cuando el teléfono excede los 10 dígitos"
    pass

class NombreDeUnCaracter(Exception):
    "se lanza cuando un nombre tiene sólo un caracter"
    pass

class TipoContactoInvalido:
    "Se lanza cuando se ingresa un tipo de contacto inválido"
    pass


class NombreLargoError(Exception):
    "Se lanza cuando el nombre supera los 15 caracteres"
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