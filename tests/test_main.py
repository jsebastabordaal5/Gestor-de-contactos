from src.model.usuario import Usuario
from src.model.gestor_contactos import GestorContactos
from src.model.contacto import Contacto

from src.model.errores import ContactoNoEncontradoError, DatosInsuficientesError, NumeroInvalidoError, NombreCortoError, \
    CampoVacio, ErrorSinContactos, ErrorArchivoInexistente, ErrorFormatoArchivoInvalido, NombreLargoError, NumeroLargoError, NombreDeUnCaracter, TipoContactoInvalidoError, \
    ErrorDatosNoNumericos, ErrorCriterioInexistente, ErrorNombreCaracterInvalido



import pytest

#Requisito 1

#Normales
def test_crear_contacto_1():
    usuario = Usuario("juan", "12345")
    contacto= Contacto("personal", "juan sebastian", "3226130937")
    usuario.gestor.registrar_contacto(contacto)
    assert len(usuario.gestor.contactos) == 1

def test_crear_contacto_2():
    usuario = Usuario("juan", "12345")
    contacto = Contacto("profesional", "tomas henao", "3148122236")
    usuario.gestor.registrar_contacto(contacto)
    assert len(usuario.gestor.contactos) == 1

def test_crear_contacto_3():
    usuario = Usuario("juan", "12345")
    contacto = Contacto("profesional", "daniel olarte", "3148122216")
    usuario.gestor.registrar_contacto(contacto)
    assert len(usuario.gestor.contactos) == 1

#Extremos
def test_nombre_con_mas_de_15_caracteres():
    usuario = Usuario("juan", "12345")
    with pytest.raises(NombreLargoError):
        contacto = Contacto("personal", "Daniel Olarte Pérez Valencia Villa Andrade", "3148122216")


def test_telefono_mas_de_10_digitos():
    usuario = Usuario("juan", "12345")
    with pytest.raises(NumeroLargoError):
        contacto = Contacto("personal", "Samuel Flórez", "99999999999999999" )

def test_nombre_con_solo_1_caracter():
    usuario = Usuario("juan", "12345")
    with pytest.raises(NombreDeUnCaracter):
        contacto = Contacto("personal", "y", "331 2498 3127" )



def test_tipo_contacto_invalido():
    usuario = Usuario("juan", "12345")
    with pytest.raises(TipoContactoInvalidoError):
        contacto = Contacto("parcero", "juan gonzalez", "331 2498 3127")


def datos_no_numericos():
    usuario = Usuario("juan", "12345")
    with pytest.raises(ErrorDatosNoNumericos):
        contacto = Contacto("profesional", "juan gonzalez", "3abc 233 447")

def campos_vacios():
    usuario = Usuario("juan", "12345")
    with pytest.raises(CampoVacio):
        contacto1 = Contacto(" ", "juan gonzalez", "331 2498 3127")
        contacto2 = Contacto("profesional ", " ", "331 2498 3127")
        contacto3 = Contacto("profesional", "juan gonzalez", " ")



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
    with pytest.raises(CampoVacio):
        usuario.gestor.editar_contacto("samuel", nuevo_nombre= "")


# Requisito 3

# Normales

def test_filtrar_contactos_por_nombre():
    usuario = Usuario("juan", "12345")
    usuario.gestor.contactos = [
        Contacto("personal", "Carlos Pérez", "555123456"),
        Contacto("profesional", "Ana López", "555654321"),
        Contacto("personal", "Carlos Gómez", "555987654"),
    ]
    resultado = usuario.gestor.filtrar_contactos('nombre', 'carlos')

    esperado = [
        Contacto("personal", "Carlos Pérez", "555123456"),
        Contacto("personal", "Carlos Gómez", "555987654")
    ]
    assert resultado == esperado


def test_filtrar_contactos_por_telefono():
    usuario = Usuario("juan", "12345")
    usuario.gestor.contactos = [
        Contacto("personal", "Juan Rodríguez", "3146272068"),
        Contacto("profesional", "Ana López", "555654321"),
        Contacto("profesional", "Carlos Gómez", "309482213"),
    ]
    resultado = usuario.gestor.filtrar_contactos('telefono', '314')

    esperado = [
        Contacto("personal", "Juan Rodríguez", "3146272068")
    ]
    assert resultado == esperado



def test_filtrar_contactos_por_tipo():
    usuario = Usuario("juan", "12345")
    usuario.gestor.contactos = [
        Contacto("personal", "Juan Rodríguez", "3146272068"),
        Contacto("profesional", "Ana López", "555654321"),
        Contacto("profesional", "Carlos Gómez", "309482213")
    ]
    resultado = usuario.gestor.filtrar_contactos('tipo', 'profesional')

    esperado = [
        Contacto("profesional", "Ana López", "555654321"),
        Contacto("profesional", "Carlos Gómez", "309482213")
    ]
    assert resultado == esperado


# Extremos

def test_filtrar_lista_vacia():
    usuario = Usuario("juan", "12345")
    usuario.gestor.contactos = []
    resultado = usuario.gestor.filtrar_contactos("nombre", "Carlos")
    assert resultado == []


# Errores
def test_filtrar_criterio_inexistente():
    usuario = Usuario("juan", "12345")
    usuario.gestor.contactos = [
        Contacto("personal", "mateo lópez", "329050614"),
        Contacto("profesional", "carlos manuel", "399888765"),
        Contacto("profesional", "juan mecanico", "315665432"),
    ]

    with pytest.raises(ErrorCriterioInexistente):
        usuario.gestor.filtrar_contactos("edad", "37")


def test_filtrar_nombre_caracter_invalido():
    usuario = Usuario("juan", "12345")
    usuario.gestor.contactos = [
        Contacto("personal", "mateo lópez", "329050614"),
        Contacto("profesional", "carlos manuel", "399888765"),
        Contacto("profesional", "juan mecanico", "315665432"),
    ]

    with pytest.raises(ErrorNombreCaracterInvalido):
        usuario.gestor.filtrar_contactos("nombre", "C@rlos")



       

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