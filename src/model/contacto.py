
class Contacto:
    def __init__(self, tipo: str ,nombre: str , telefono : str):
        self.tipo = tipo
        self.nombre = nombre
        self.telefono = telefono

    def __str__(self):
        return f"{self.tipo} ({self.nombre}) - {self.telefono}"

