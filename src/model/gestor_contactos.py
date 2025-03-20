from src.model.contacto import Contacto
from src.model.errores import ErrorCriterioInexistente

class GestorContactos:
    def __init__(self):
        self.contactos: list[Contacto] = []


    def ver_contactos(self):
        pass

    def registrar_contacto(self, contacto:Contacto):
        if contacto not in self.contactos:
            self.contactos.append(contacto)
            print(f"Contacto: {contacto.nombre} fue agregado exitosamente!")
        else:
            print(f"El contacto {contacto.nombre} ya es existente!")



    def editar_contacto(self, contacto: Contacto, nuevo_tipo: str = None , nuevo_nombre : str= None , nuevo_telefono: str = None ):
        pass

    def importar_contactos(self, archivo):
        pass

    def filtrar_contactos(self, criterio: str, valor: str) -> list[Contacto]:
        if criterio not in ["tipo", "nombre", "teléfono"]:
            raise ErrorCriterioInexistente(f"El criterio {criterio} es inexistente")

        contactos_filtrados = []
        for contacto in self.contactos:
            if str(getattr(contacto, criterio)) == valor:
                contactos_filtrados.append(contacto)
        return contactos_filtrados

    def exportar_contactos(self,nombre_archivo: str):
        pass
