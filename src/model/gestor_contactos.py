from src.model.contacto import Contacto
from src.model.errores import ErrorCriterioInexistente, ErrorLimiteDigitosTelefono

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




        self.contactos.append(contacto)



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
