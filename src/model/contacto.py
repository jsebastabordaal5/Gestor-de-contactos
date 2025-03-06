
class Contacto:
    def __init__ (self,tipo: str ,nombre: str , telefono : str ):
        self.tipo = tipo
        self.nombre= nombre
        self.telefono = telefono

    def registrar_contacto(self, tipo: str , nombre: str , telefono: str):
        nuevo_contacto = Contacto(tipo, nombre, telefono)
