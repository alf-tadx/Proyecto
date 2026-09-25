"""
Proyecto ¿Y ahora qué leo?
El programa va a tener una lista de libros
y con diferentes preguntas va a recomendar
cual es el mejor para el usuario
"""

# Avance 2 Libre Uso de Funciones

"""
Para este avance cambie las operaciones por diferentes funciones
para tener un mayor orden y poder utilizarlas mas veces.
"""

def calcular_paginas(paginas_hora, tiempo):
    """
    Cantidad de paginas que puedes leer segun el tiempo
    """
    paginas_posibles = paginas_hora * tiempo
    return paginas_posibles

def calcular_horas_necesarias(paginas_libro, paginas_hora):
    """
    Cantidad de horas en las que acabas el libro
    """
    horas_libro = paginas_libro / paginas_hora
    return horas_libro

def calcular_paginas_faltantes(paginas_libro, paginas_posibles):
    """
    Paginas que faltan para acabar el libro
    """
    paginas_faltantes = paginas_libro - paginas_posibles
    return paginas_faltantes

def calcular_porcentaje_leer(paginas_posibles, paginas_libro):
    """
    Calcular porcentaje que has leido
    """
    porcentaje = (paginas_posibles / paginas_libro) * 100
    return porcentaje

def imprimir_resultados(titulo_libro, paginas_libro, paginas_posibles,
                         horas_libro, paginas_faltantes, porcentaje):
    """
    Impresion de resultados
    """
    print("Resultados finales")
    print("Libro", titulo_libro, "de", paginas_libro, "paginas")
    print("Segun tu tiempo y velocidad de lectura puedes leer",
          paginas_posibles, "paginas")
    print("En", horas_libro, "horas terminas el libro")
    print("Te faltarian", paginas_faltantes,
          "paginas para acabar el libro")
    print("Puedes leer un", porcentaje, "% del libro")

"""
Programa principal con datos de un libro como ejemplo
"""

TITULO_LIBRO = "The Setting Sun"
PAGINAS_LIBRO = 174

# Datos del usuario
paginas_hora = float(input("¿Cuántas páginas lees cada hora?"))
tiempo = float(input("¿Cuántas horas tienes para leer?"))

# Programa
paginas_posibles = calcular_paginas(paginas_hora, tiempo)
horas_libro = calcular_horas_necesarias(PAGINAS_LIBRO, paginas_hora)
paginas_faltantes = calcular_paginas_faltantes \
                    (PAGINAS_LIBRO, paginas_posibles)
porcentaje = calcular_porcentaje_leer(paginas_posibles, PAGINAS_LIBRO)

# Resultados
imprimir_resultados(TITULO_LIBRO, PAGINAS_LIBRO, paginas_posibles,
                    horas_libro, paginas_faltantes, porcentaje)