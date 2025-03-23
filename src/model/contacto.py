
class Contacto:
    def __init__(self, tipo: str ,nombre: str , telefono : str):
        self.tipo = tipo
        self.nombre = nombre
        self.telefono = telefono


    def __eq__(self, other):
        if isinstance(other, Contacto):
            return self.nombre == other.nombre and self.telefono == other.telefono and self.tipo == other.tipo
        return False


    def __hash__(self):
        return hash((self.nombre, self.telefono, self.tipo))

