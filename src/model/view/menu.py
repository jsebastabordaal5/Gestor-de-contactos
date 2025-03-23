from src.model import Contacto, Usuario, GestorContactos, GestorUsuarios


class Sistema:
    def __init__(self):
        self.gestor_usuarios = GestorUsuarios()

    def mostrar_menu(self):
        while True:
            print("\n📌 MENÚ PRINCIPAL")
            print("1️⃣  Registrar usuario")
            print("2️⃣  Iniciar sesión")
            print("3️⃣  Cerrar Sesión")
            opcion = input("Seleccione una opción: ")

            if opcion == "1":
                self.registrar_usuario()
            elif opcion == "2":
                self.iniciar_sesion()
            elif opcion == "3":
                print("👋 Saliendo del sistema...\n")
                break
            else:
                print("⚠️ Opción no válida. Intente de nuevo.")

    def registrar_usuario(self):
        nombre = input("Ingrese nombre de usuario: ")
        contrasena = input("Ingrese contraseña: ")
        usuario = Usuario(nombre, contrasena)
        self.gestor_usuarios.registrar_usuario(usuario)
        print("✅ Usuario registrado correctamente.")

    def iniciar_sesion(self):
        nombre = input("Ingrese nombre de usuario: ")
        contrasena = input("Ingrese contraseña: ")
        usuario = self.gestor_usuarios.iniciar_sesion(nombre, contrasena)
        if usuario:
            self.opciones_usuario(usuario)

    def opciones_usuario(self, usuario):
        while True:
            print(f"\n👤 MENÚ DE USUARIO ({usuario.nombre})")
            print("1️⃣  Crear contacto")
            print("2️⃣  Ver contactos")
            print("3️⃣  Cerrar sesión")
            opcion = input("Seleccione una opción: ")

            if opcion == "1":
                self.crear_contacto(usuario)
            elif opcion == "2":
                usuario.gestor_contactos.ver_contactos()
            elif opcion == "3":
                self.gestor_usuarios.cerrar_sesion()
                print("🚪 Sesión cerrada.")
                break
            else:
                print("⚠️ Opción no válida. Intente de nuevo.")

    def crear_contacto(self, usuario):
        tipo = int(input("Ingrese tipo de contacto (1: Personal, 2: Trabajo): "))
        nombre = input("Ingrese nombre del contacto: ")
        telefono = input("Ingrese teléfono del contacto: ")
        contacto = Contacto(tipo, nombre, telefono)
        usuario.gestor_contactos.registrar_contacto(contacto)


# Inicializar y ejecutar el menú del sistema
sistema = Sistema()
sistema.mostrar_menu()

