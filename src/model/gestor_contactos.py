import re
import os
from src.model.contacto import Contacto
from src.model.errores import (NombreCortoError , NombreVacioError , NumeroInvalidoError , ContactoNoEncontradoError
                     , DatosInsuficientesError , ErrorNombreCaracterInvalido, ErrorCriterioInexistente, ErrorSinContactos, ErrorArchivoInexistente,ErrorFormatoArchivoInvalido,
                     TipoContactoError, NumeroInvalidoError, NombreInvalidoError, DatosNoNumericosError, CampoVacioError
                    )


class GestorContactos:
    def __init__(self):
        self.contactos: list[Contacto] = []


    def ver_contactos(self):
        if not self.contactos:
            print("No hay contactos guardados.")
            return

        lista_aux = []

        print("\nLista de Contactos:")

        for i, contacto in enumerate(self.contactos, start=1):
            print(f"{i}. {contacto.tipo} - {contacto.nombre} ({contacto.telefono})")
            lista_aux.append(contacto)

        return lista_aux

    def registrar_contacto(self, contacto:Contacto):

        if contacto.nombre.strip() == "" or contacto.tipo.strip() == "" or contacto.telefono.strip() == "":
            raise CampoVacioError()

        if not contacto.telefono.isdigit():
            raise DatosNoNumericosError(contacto.telefono)


        if len(contacto.nombre) < 30 and len(contacto.nombre) > 0 :
            if len(contacto.telefono) >= 10 and len(contacto.telefono) <= 12:
                if contacto.tipo == "profesional" or contacto.tipo == "personal":
                    self.contactos.append(contacto)
                    return contacto
                else:
                    raise TipoContactoError(contacto.tipo)
            else:
                raise NumeroInvalidoError()
        else:
            raise NombreInvalidoError()




    def editar_contacto(self, contacto: Contacto, nuevo_tipo: str = None , nuevo_nombre : str= None , nuevo_telefono: str = None ):
        if nuevo_nombre == "":
            raise NombreVacioError()

        if not nuevo_nombre and not nuevo_tipo and not nuevo_telefono:
            raise DatosInsuficientesError()

        if contacto not in self.contactos:
            raise ContactoNoEncontradoError(contacto)

        if nuevo_nombre:
            if len(nuevo_nombre.strip()) < 3:
                raise NombreCortoError()

            contacto.nombre = nuevo_nombre.strip()

        if nuevo_telefono:
            if len(nuevo_telefono.strip()) != 10:
                raise NumeroInvalidoError()

            contacto.telefono = nuevo_telefono.strip()

        if nuevo_tipo:
            if nuevo_tipo.strip().lower() != "profesional" and nuevo_tipo.strip().lower() != "personal":
                print("el tipo debe ser profesional o personal ")

            contacto.tipo = nuevo_tipo.strip()

        return contacto



    def importar_contactos(self, archivo):
        if not os.path.isabs(archivo):  # Verifica si la ruta es absoluta
            archivo = os.path.abspath(archivo)  # Convierte a ruta absoluta

        if not os.path.exists(archivo):
            raise ErrorArchivoInexistente(archivo)

        with open(archivo, "r", encoding="utf-8") as file:
            contenido = file.read().strip()

        if not contenido:
            return

            # Verificamos si el contenido sigue el formato VCF esperado
        if "FN:" not in contenido or "TEL:" not in contenido or "CATEGORIES:" not in contenido:
            raise ErrorFormatoArchivoInvalido(archivo)

        with open(archivo, "r", encoding="utf-8") as file:
            contactos_temporales = []
            nombre = telefono = tipo = None

            for linea in file:
                linea = linea.strip()  # Eliminamos espacios innecesarios
                if linea.startswith("BEGIN:VCARD"):
                    nombre = telefono = tipo = None
                elif linea.startswith("FN:"):
                    nombre = linea[3:]  # Tomamos el texto después de "FN:"
                elif linea.startswith("TEL:"):
                    telefono = linea[4:]  # Tomamos el texto después de "TEL:"
                elif linea.startswith("CATEGORIES:"):
                    tipo = linea[11:]  # Tomamos el texto después de "CATEGORIES:"
                elif linea.startswith("END:VCARD"):
                    if nombre and telefono and tipo:
                        contacto = Contacto(tipo, nombre, telefono)
                        contactos_temporales.append(contacto)

            for contacto in contactos_temporales:
                if contacto not in self.contactos:
                    self.contactos.append(contacto)

            print(f"Se importaron {len(self.contactos)} contactos correctamente.")





    def exportar_contactos(self,nombre_archivo: str):
        if not self.contactos:  # Verifica si la lista de contactos está vacía
            raise ErrorSinContactos()

        with open(nombre_archivo, "w", encoding="utf-8") as archivo:
            for contacto in self.contactos:
                vcard = (
                    f"BEGIN:VCARD\n"
                    f"FN:{contacto.nombre}\n"
                    f"TEL:{contacto.telefono}\n"
                    f"CATEGORIES:{contacto.tipo}\n"
                    f"END:VCARD\n"
                )
                archivo.write(vcard)


    def filtrar_contactos(self, criterio: str, valor: str) -> list[Contacto]:
        criterios_validos = ["nombre", "telefono", "tipo"]
        if criterio not in criterios_validos:
            raise ErrorCriterioInexistente(
                f"El criterio '{criterio}' no es válido. Debe ser 'nombre', 'telefono' o 'tipo'.")

        # Validar caracteres en el nombre
        if criterio == "nombre" and not re.match(r"^[a-zA-ZáéíóúÁÉÍÓÚñÑ\s]+$", valor):
            raise ErrorNombreCaracterInvalido(f"El nombre '{valor}' contiene caracteres no permitidos.")

        # Validar que el teléfono contenga solo dígitos
        if criterio == "telefono" and not valor.isdigit():
            raise DatosNoNumericosError(f"El teléfono '{valor}' contiene caracteres no numéricos.")

        # Filtrar contactos
        contactos_filtrados = []

        for contacto in self.contactos:
            if criterio == "tipo" and contacto.tipo.lower() == valor.lower():
                contactos_filtrados.append(contacto)
            elif criterio == "nombre" and valor.lower() in contacto.nombre.lower():
                contactos_filtrados.append(contacto)
            elif criterio == "telefono" and valor in contacto.telefono:  # Permite búsqueda parcial de teléfono
                contactos_filtrados.append(contacto)

        return contactos_filtrados