# GestorDeContactos
El objetivo de este proyecto es desarrollar una aplicación para la gestión de contactos personales y profesionales, permitiendo almacenar, organizar y manipular información de manera eficiente




![image](https://github.com/user-attachments/assets/8fa9f15b-096e-41f3-ae8b-4964b2bee244)



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
El sistema debe permitir al usuario editar la informacion de un contacto

## Caso de prueba 1: Caso normal-Editar tipo de contacto:
Contacto:
| Tipo | Nombre | Teléfono|
|------|--------|---------|
| "personal" | "samuel" | "300222398" |

Al editar: 
|Valor a cambiar| Nuevo valor|
|---------------|------------|
| "tipo" | "profesional"| 

Resultado:
| Tipo | Nombre | Teléfono|
|------|--------|---------|
| "profesional" | "samuel" | "300222398" |


## Caso de prueba 2: Caso normal- Editar nombre de contacto :
Contacto:
| Tipo | Nombre | Teléfono|
|------|--------|---------|
| "personal" | "samuel" | "300222398" |

Al editar: 
|Valor a cambiar| Nuevo valor|
|---------------|------------|
| "nombre" | "juan"| 

Resultado:
| Tipo | Nombre | Teléfono|
|------|--------|---------|
| "personal" | "juan" | "300222398" |

## Caso de prueba 3: Caso normal-Editar numero de contacto:
Contacto:
| Tipo | Nombre | Teléfono|
|------|--------|---------|
| "personal" | "samuel" | "300222398" |

Al editar: 
|Valor a cambiar| Nuevo valor|
|---------------|------------|
| "telefono" | "3005680588"| 

Resultado:
| Tipo | Nombre | Teléfono|
|------|--------|---------|
| "personal" | "samuel" | "3005680588" |

## Caso de prueba 4: Caso Extremo-Editar contacto con nombre muy corto:
Contacto:
| Tipo | Nombre | Teléfono|
|------|--------|---------|
| "personal" | "samuel" | "300222398" |

Al editar: 
|Valor a cambiar| Nuevo valor|
|---------------|------------|
| "nombre" | "a"| 

Resultado:
| Eror|
|------|
| "Error: El nombre es demasiado corto. Debe tener al menos 3 caracteres" |

## Caso de prueba 5: Caso Extremo-Editar contacto con telefono muy largo:

Contacto:
| Tipo | Nombre | Teléfono|
|------|--------|---------|
| "personal" | "samuel" | "300222398" |

Al editar: 
|Valor a cambiar| Nuevo valor|
|---------------|------------|
| "telefono" | "1234567898765432123"| 

Resultado:
| Error|
|------|
| "Error: El número de teléfono debe tener exactamente 10 dígitos |


## Caso de prueba 6: Caso Extremo-Editar contacto con telefono ivalido:
Contacto:
| Tipo | Nombre | Teléfono|
|------|--------|---------|
| "personal" | "samuel" | "300222398" |

Al editar: 
|Valor a cambiar| Nuevo valor|
|---------------|------------|
| "telefono" | "1"| 

Resultado:
| Error|
|------|
| "Error: El número de teléfono debe tener exactamente 10 dígitos |


## Caso de prueba 7: Caso Error-Editar contacto no existente:
Contacto:
| Tipo | Nombre | Teléfono|
|------|--------|---------|
|      |       |        |

Al editar:
| Error|
|------|
| "Error: El contacto no fue encontrado"|


## Caso de prueba 8: Caso Error-Editar contacto sin valores:
Contacto:
| Tipo | Nombre | Teléfono|
|------|--------|---------|
| "personal" | "samuel" | "300222398" |

Al editar: 
| nuevo tipo |nuevo Nombre | nuevo Teléfono|
|------|--------|---------|
|      |       |        |

Resultado:
| Error|
|------|
| "Error: Debe proporcionar al menos un dato para modificar el contacto|


## Caso de prueba 9 : Caso Error-Editar contacto nombre vacio:
Contacto:
| Tipo | Nombre | Teléfono|
|------|--------|---------|
| "personal" | "samuel" | "300222398" |

Al editar: 
| nuevo tipo |nuevo Nombre | nuevo Teléfono|
|------|--------|---------|
|      |    " "   |        |

Resultado:
| Error|
|------|
| "Error: El nombre no puede ser un campo vacio|









# 3. Filtrar un contacto por nombre y categoría:
El sistema debe permitir al usuario filtrar la
lista de contactos por nombre y categoría.


## Caso de prueba Normal 1: Filtrar contactos por nombre:
| Tipo | Nombre | Teléfono|
|------|--------|---------|
| "personal" | "Carlos Pérez" | "555123456" |
| "profesional" | "Ana López" | "555654321" |
| "personal" | "Carlos Gómez" | "555987654" |
|------|--------|---------|


| Nombre: | Carlos |
|------|--------|

| "personal" | "Carlos Pérez" | "555123456" |
| "personal" | "Carlos Gómez" | "555987654" |
|------|--------|---------|


## Caso de prueba Normal 2: Filtrar contactos por teléfono:
| Tipo | Nombre | Teléfono|
|------|--------|---------|
| "personal" | "Carlos Pérez" | "555123456" |
| "profesional" | "Ana López" | "555654321" |
| "profesional" | "Carlos Gómez" | "555987654" |
|------|--------|---------|




# 4. Exportar e importar los contactos en formato vcards (.vcf): 
El sistema debe permitir al
usuario exportar los contactos a un archivo .vcf e importarlos al sistema desde un
archivo .vcf.


# 5. Crear un usuario:
El sistema debe permitir al usuario darse de alta.


# 6. Iniciar sesión:
El sistema debe permitir al usuario iniciar sesión para ver la lista de sus
contactos.
