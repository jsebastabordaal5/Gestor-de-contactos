class Usuario:
    def __init__(self, nombre : str , contraseña : str):
        self.nombre= nombre
        self.contraseña = contraseña
        self.gestor= GestorContactos()