
class GestorContactos:
    def __init__(self):
        self.contactos = []


    def ver_contactos(self):
        pass

    def registrar_contacto(self, tipo: str , nombre: str , telefono: str):
        nuevo_contacto = Contacto(tipo, nombre, telefono)
        self.contactos.append(nuevo_contacto)

    def editar_contacto(self, nombre_actual:str, nuevo_tipo: str = None , nuevo_nombre : str= None , nuevo_telefono: str = None ):
        pass

    def importar_contactos (self,archivo):
        pass

    def exportar_contactos(self,nombre_archivo: str):
        pass
