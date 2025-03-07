from src.model.contacto import Contacto

class GestorContactos:
    def __init__(self):
        self.contactos = []


    def ver_contactos(self):
        pass

    def registrar_contacto(self,contacto:Contacto):
        pass



    def editar_contacto(self, contacto: Contacto, nuevo_tipo: str = None , nuevo_nombre : str= None , nuevo_telefono: str = None ):
        pass

    def importar_contactos (self, archivo):
        pass

    def filtrar_contactos(self, criterio: str, valor: str) -> list[Contacto]:
        pass

    def exportar_contactos(self,nombre_archivo: str):
        pass
