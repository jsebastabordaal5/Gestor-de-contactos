# GestorDeContactos
El objetivo de este proyecto es desarrollar una aplicación para la gestión de contactos personales y profesionales, permitiendo almacenar, organizar y manipular información de manera eficiente

# Requisitos:


# 1. Crear un contacto:
El sistema debe permitir al usuario crear un contacto.

## Caso de prueba 1: Caso normal:
| Tipo | Nombre | Teléfono |
|------|--------|----------|
| "Personal" | "Juan Sebastián" | "3226130937" |

## Caso de prueba 2: Caso normal:
| Tipo | Nombre | Teléfono |
|------|--------|----------|
| "Profesional" | "Tomás Henao" | "3146272068" |

## Caso de prueba 3: Caso normal:
| Tipo | Nombre | Teléfono |
|------|--------|----------|
| "Profesional" | "Daniel Olarte" | "3148122216" |


## Caso de prueba 4: Nombre con más de 12 caracteres:
| Tipo | Nombre | Teléfono |
|------|--------|----------|
| "Profesional" | "Daniel Olarte Pérez Valencia Villa Andrade" | "3148122216" |


## Caso de prueba 5: Teléfono con más de 10 dígitos:
| Tipo | Nombre | Teléfono |
|------|--------|----------|
| "Personal" | "Samuel Flórez" | "99999999999999999" |


## Caso de prueba 6: Nombre con un sólo caracter:
| Tipo | Nombre | Teléfono |
|------|--------|----------|
| "Personal" | "Y" | "331 2498 3127" |


## Caso de prueba 7: Tipo de Contacto Inválido:
| Tipo | Nombre | Teléfono | Error           |
|------|--------|----------|----------|
| "Parcero" | "Juan González" | "331 2498 3127" | Error! Tipo de contacto Inválido|



## Caso de prueba 8: Datos NO numéricos:
| Tipo | Nombre | Teléfono | Error           |
|------|--------|----------|----------|
| "Profesional" | "Juan Mecánico" | "313 812 149916" | Error! Contiene letras|



## Caso de prueba 9: Campos vacíos:
| Tipo | Nombre | Teléfono | Error           |
|------|--------|----------|----------|
| "Profesional" | "" | "313 812 149916" | Error! Campo Vacío|


| Tipo | Nombre | Teléfono | Error           |
|------|--------|----------|----------|
| "Profesional" | "Felipe Sánchez" | "" | Error! Campo vacío|


| Tipo | Nombre | Teléfono | Error           |
|------|--------|----------|----------|
| "" | "Felipe Sánchez" | "313 812 149916" | Error! Campo vacío|












# 2. Editar un contacto:
El sistema debe permitir al usuario editar la información de un
contacto.

## Caso de prueba normal 1: Editar el Tipo de Contacto.
| Tipo | Nombre | Teléfono |
|------|--------|----------|
| "Personal" | "Samuel" | "300222398" |

| Tipo | Nombre | Teléfono |
|------|--------|----------|
| "Profesional" | "Samuel" | "300222398" |


## Caso de prueba normal 2: Editar el Nombre del Contacto.
| Tipo | Nombre | Teléfono |
|------|--------|----------|
| "Personal" | "Samuel" | "300222398" |

| Tipo | Nombre | Teléfono |
|------|--------|----------|
| "Personal" | "Juan" | "300222398" |


## Caso de prueba normal 3: Editar el teléfono del contacto.
| Tipo | Nombre | Teléfono |
|------|--------|----------|
| "Personal" | "Samuel" | "300222398" |

| Tipo | Nombre | Teléfono |
|------|--------|----------|
| "Personal" | "Samuel" | "3005680588" |








# 3. Filtrar un contacto por nombre y categoría:
El sistema debe permitir al usuario filtrar la
lista de contactos por nombre y categoría.


# 4. Exportar e importar los contactos en formato vcards (.vcf): 
El sistema debe permitir al
usuario exportar los contactos a un archivo .vcf e importarlos al sistema desde un
archivo .vcf.


# 5. Crear un usuario:
El sistema debe permitir al usuario darse de alta.


# 6. Iniciar sesión:
El sistema debe permitir al usuario iniciar sesión para ver la lista de sus
contactos.
