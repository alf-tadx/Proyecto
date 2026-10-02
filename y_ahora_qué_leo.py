"""
Proyecto ¿Y ahora qué leo?
El programa va a tener una lista de libros
y con diferentes preguntas va a recomendar
cual es el mejor para el usuario
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
    if paginas_faltantes <= 0:
        paginas_faltantes = 0
    return paginas_faltantes

def calcular_porcentaje_leer(paginas_posibles, paginas_libro):
    """
    Calcular porcentaje que has leido
    """
    porcentaje = (paginas_posibles / paginas_libro) * 100
    if porcentaje >= 100:
        porcentaje = 100
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
    
def terminar_libro (porcentaje):
    """
    Usa if para determinar si el usuario
    acaba o no el libro
    """
    if porcentaje >= 100:
        return "Si puedes acabar el libro :)"
    else:
        return "Todavia no puedes acabar el libro :("

def calcular_paginas_hora ( ):
    """
    Pregunta si sabes cuantas paginas lees por hora,
    si no sabes usa el promedio de las referencias
    """
    respuesta = int(input("Sabes cuantas paginas lees \
por hora,si = 1 no = 2"))
    if respuesta == 1:
        paginas_hora = float(input("¿Cuántas páginas \
lees cada hora?"))
    elif respuesta == 2:
        paginas_hora = PROMEDIO_PAGINAS_HORA
    return paginas_hora

"""
Programa principal con datos de un libro como ejemplo
"""

TITULO_LIBRO = "The Setting Sun"
PAGINAS_LIBRO = 174
PROMEDIO_PAGINAS_HORA = 40

# Datos del usuario
paginas_hora = calcular_paginas_hora ( )
tiempo = float(input("¿Cuántas horas tienes para leer?"))

# Programa
paginas_posibles = calcular_paginas(paginas_hora, tiempo)
horas_libro = calcular_horas_necesarias(PAGINAS_LIBRO, paginas_hora)
paginas_faltantes = calcular_paginas_faltantes \
                    (PAGINAS_LIBRO, paginas_posibles)
porcentaje = calcular_porcentaje_leer(paginas_posibles, PAGINAS_LIBRO)

# Resultados
print (" ")
imprimir_resultados(TITULO_LIBRO, PAGINAS_LIBRO, paginas_posibles,
                    horas_libro, paginas_faltantes, porcentaje)
print (" ")
print (terminar_libro (porcentaje))