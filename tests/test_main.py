from src.model.usuario import Usuario
from src.model.gestor_contactos import GestorContactos
from src.model.contacto import Contacto

from src.model.errores import ContactoNoEncontradoError, DatosInsuficientesError, NumeroInvalidoError, NombreCortoError, \
    NombreVacioError, ErrorSinContactos, ErrorArchivoInexistente, ErrorFormatoArchivoInvalido, NombreLargoError


import pytest

#Requisito 1

#Normales
def test_crear_contacto_1():
    usuario = Usuario("juan", "12345")
    usuario.gestor.registrar_contacto("personal", "juan sebastian", "3226130937")
    assert len(usuario.gestor.contactos) == 1

def test_crear_contacto_2():
    usuario = Usuario("juan", "12345")
    usuario.gestor.registrar_contacto("profesional", "tomas henao", "3146272068")
    assert len(usuario.gestor.contactos) == 1

def test_crear_contacto_3():
    usuario = Usuario("juan", "12345")
    usuario.gestor.registrar_contacto("profesional", "daniel olarte", "3148122296")
    assert len(usuario.gestor.contactos) == 1

#Extremos
def test_nombre_con_mas_de_15_caracteres():
    usuario = Usuario("juan", "12345")


    with pytest.raises(NombreLargoError):
        usuario.gestor.registrar_contacto("profesional", "daniel olarte perez valencia villa", "3148122296")













#Requisito 2
#Normales
def test_editar_tipo_contacto ( ):
    usuario = Usuario("juan","12345")
    usuario.gestor.registrar_contacto("personal","samuel","300222398")
    usuario.gestor.editar_contacto("samuel", nuevo_tipo="profesional")
    assert usuario.gestor.contactos[0].tipo == "profesional"

def test_editar_nombre_contacto ( ):
    usuario = Usuario("juan","12345")
    usuario.gestor.registrar_contacto("personal","samuel","300222398")
    usuario.gestor.editar_contacto("samuel", nuevo_nombre="juan")
    assert usuario.gestor.contactos[0].nombre == "juan"

def test_editar_numero_contacto ( ):
    usuario = Usuario("juan","12345")
    usuario.gestor.registrar_contacto("personal","samuel","300222398")
    usuario.gestor.editar_contacto("samuel",nuevo_telefono="3005680588")
    assert usuario.gestor.contactos[0].telefono == "3005680588"




#Extremos
def test_editar_contacto_nombre_extremadamente_corto():
    usuario = Usuario("juan", "12345")
    usuario.gestor.registrar_contacto("personal", "samuel", "3002223987")
    
    with pytest.raises(NombreCortoError):
        usuario.gestor.editar_contacto("samuel", nuevo_nombre="a")


def test_editar_contacto_numero_extremadamente_largo():
    usuario = Usuario("juan", "12345")
    numero_muy_largo = "1234567898765432123"
    usuario.gestor.registrar_contacto("personal", "samuel", "3002223987")
    
    with pytest.raises(NumeroInvalidoError):
        usuario.gestor.editar_contacto("samuel",nuevo_telefono= numero_muy_largo)

def test_editar_contacto_numero_invalido():
    usuario = Usuario("juan", "12345")
    numero_corto= "1"
    usuario.gestor.registrar_contacto("personal", "samuel", "300222398")  

    with pytest.raises(NumeroInvalidoError): 
        usuario.gestor.editar_contacto("samuel", numero_corto) 


#Error
def test_editar_contacto_no_existente():
        usuario = Usuario("juan", "12345")
        usuario.gestor.registrar_contacto("personal","samuel","300222398")

        with pytest.raises(ContactoNoEncontradoError):
            usuario.gestor.editar_contacto("desconocido", nuevo_tipo="profesional")
            

def test_editar_contacto_sin_valores():
    usuario = Usuario("juan", "12345")
    usuario.gestor.registrar_contacto("personal", "samuel", "300222398")

    with pytest.raises(DatosInsuficientesError):
        usuario.gestor.editar_contacto("samuel")  




def test_editar_contacto_nombre_vacio():
    usuario = Usuario("juan", "12345")
    usuario.gestor.registrar_contacto("personal", "samuel", "300222398")

    with pytest.raises(NombreVacioError):
        usuario.gestor.editar_contacto("samuel", nuevo_nombre= "")
       

#Requisito 4
#Normales
def test_exportar_contacto():
   usuario = Usuario("juan", "12345")
   usuario.gestor.registrar_contacto("personal", "samuel", "300222398")

   usuario.gestor.exportar_contactos("contactos.vcf")

   with open("contactos.vcf", "r") as archivo:
        contenido = archivo.read()

        esperado = """BEGIN:VCARD
                    FN:samuel
                    TEL:300222398
                    CATEGORIES:personal
                    END:VCARD"""

        assert esperado in contenido


def test_importar_contacto():
    with open("contactos.vcf", "w") as archivo:
        archivo.write("""BEGIN:VCARD
FN:samuel
TEL:300222398
CATEGORIES:personal
END:VCARD""")

    usuario = Usuario("juan", "12345")
    usuario.gestor.importar_contactos("contactos.vcf")

    assert len(usuario.gestor.contactos) == 1
    assert usuario.gestor.contactos[0].nombre == "samuel"
    assert usuario.gestor.contactos[0].telefono == "300222398"
    assert usuario.gestor.contactos[0].tipo == "personal"
    
  


def test_exportar_multiples_contactos():
    usuario = Usuario("juan", "12345")
    usuario.gestor.registrar_contacto("personal", "samuel", "300222398")
    usuario.gestor.registrar_contacto("profesional", "ana", "3104567890")

    usuario.gestor.exportar_contactos("contactos.vcf")

    with open("contactos.vcf", "r") as archivo:
        contenido = archivo.read()

    esperado = """BEGIN:VCARD
FN:samuel
TEL:300222398
CATEGORIES:personal
END:VCARD

BEGIN:VCARD
FN:ana
TEL:3104567890
CATEGORIES:profesional
END:VCARD"""

    assert esperado in contenido


#Extremos
def test_exportar_contacto_nombre_largo():
    usuario = Usuario("juan", "12345")
    nombre_largo = "a" * 200  
    usuario.gestor.registrar_contacto("personal", nombre_largo, "300222398")
    usuario.gestor.exportar_contactos("contactos.vcf")

    with open("contactos.vcf", "r") as archivo:
        contenido = archivo.read()

    assert f"FN:{nombre_largo}" in contenido

def test_importar_contacto_archivo_vacio():
    with open("contactos_vacio.vcf", "w") as archivo:
        pass  # Crear un archivo vacío

    usuario = Usuario("juan", "12345")
    usuario.gestor.importar_contactos("contactos_vacio.vcf")

    assert len(usuario.gestor.contactos) == 1

def test_exportar_importar_contacto_caracteres_especiales():
    usuario = Usuario("juan", "12345")
    nombre_especial = "José López 🎉✨"
    telefono_especial = "+57-300-555-6666"
    
    usuario.gestor.registrar_contacto("personal", nombre_especial, telefono_especial)
    usuario.gestor.exportar_contactos("contactos_especiales.vcf")

    nuevo_usuario = Usuario("carlos", "54321")
    nuevo_usuario.gestor.importar_contactos("contactos_especiales.vcf")

    contacto_encontrado = False
    for contacto in nuevo_usuario.gestor.contactos:
        if contacto.nombre == nombre_especial and contacto.telefono == telefono_especial:
            contacto_encontrado = True
            break

    assert contacto_encontrado, "El contacto con caracteres especiales no fue importado correctamente."

#Error
def test_exportar_sin_contactos():
    usuario = Usuario("juan", "12345")

    with pytest.raises(ErrorSinContactos):
        usuario.gestor.exportar_contactos("contactos.vcf")


def test_importar_archivo_no_existente():
    usuario = Usuario("juan", "12345")

    with pytest.raises(ErrorArchivoInexistente):
        usuario.gestor.importar_contactos("archivo_inexistente.vcf")

def test_importar_archivo_formato_invalido():
    with open("formato_invalido.vcf", "w") as archivo:
        archivo.write("CONTACTO: samuel, 300222398")  # 

    usuario = Usuario("juan", "12345")

    with pytest.raises(ErrorFormatoArchivoInvalido):
        usuario.gestor.importar_contactos("formato_invalido.vcf")