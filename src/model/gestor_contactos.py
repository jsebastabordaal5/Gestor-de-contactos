from src.model.contacto import Contacto
from src.model.errores import  TipoContactoError, NumeroInvalidoError, NombreInvalidoError


class GestorContactos:
    def __init__(self):
        self.contactos: list[Contacto] = []


    def ver_contactos(self):
        pass

    def registrar_contacto(self, contacto:Contacto):
        if len(contacto.nombre) < 30 and len(contacto.nombre) > 0 :
            if len(contacto.telefono) >= 10 and len(contacto.telefono) <= 12:
                if contacto.tipo == "profesional" or contacto.tipo == "personal":
                    self.contactos.append(contacto)
                    return contacto
                else:
                    raise TipoContactoError(f"El tipo: {contacto.tipo} es inválido")
            else:
                raise NumeroInvalidoError(f"El número ingresado NO es válido")
        else:
            raise NombreInvalidoError






    def editar_contacto(self, contacto: Contacto, nuevo_tipo: str = None , nuevo_nombre : str= None , nuevo_telefono: str = None ):
        pass

    def importar_contactos(self, archivo):
        pass

    def filtrar_contactos(self, criterio: str, valor: str) -> list[Contacto]:
        contactos_filtrados = []
        for contacto in self.contactos:
            if criterio == 'tipo' and contacto.tipo == valor:
                contactos_filtrados.append(contacto)
            else:
                raise TipoContactoError(f"El tipo: {contacto.tipo} es inválido")

            if criterio == 'nombre' and contacto.nombre == valor:
                contactos_filtrados.append(contacto)
            else:
                raise NombreInvalidoError(f"El nombre {contacto.nombre} no se encuentra")

            if criterio == 'teléfono' and contacto.telefono == valor:
                contactos_filtrados.append(contacto)
            else:
                raise NumeroInvalidoError(f"El número {contacto.telefono} es inexistente")

        return contactos_filtrados






    def exportar_contactos(self,nombre_archivo: str):
        pass
