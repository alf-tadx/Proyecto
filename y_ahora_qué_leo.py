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
    print("Resultados")
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

def datos_usuario ():
    """
    Pregunta la velocidad de lectura y las horas que
    tiene para poder leer
    """
    paginas_hora = calcular_paginas_hora ( )
    tiempo = float(input("¿Cuántas horas tienes para leer?"))
    return paginas_hora, tiempo

def datos_libro ():
    """
    Pregunta el titulo y las paginas del libro
    """
    titulo_libro = input("¿Cual es el titulo del libro? ")
    paginas_libro = int(input("¿Cuantas paginas tiene el libro? "))
    return titulo_libro, paginas_libro

def calcular_acabas_libro (titulo_libro, paginas_libro, paginas_hora, tiempo):
    """
    Programa que muestra si puedes acabar el libro
    segun la informacion que tiene el programa
    """
    paginas_posibles = calcular_paginas(paginas_hora, tiempo)
    horas_libro = calcular_horas_necesarias(paginas_libro, paginas_hora)
    paginas_faltantes = calcular_paginas_faltantes \
                    (paginas_libro, paginas_posibles)
    porcentaje = calcular_porcentaje_leer(paginas_posibles, paginas_libro)

    print (" ")
    imprimir_resultados(titulo_libro, paginas_libro, paginas_posibles,
                    horas_libro, paginas_faltantes, porcentaje)
    print (" ")
    print (terminar_libro (porcentaje))
    
def mostrar_menu ():
    """"
    Muestra las opciones que tiene el menu del programa
    """
    print ("Bienvenidos a Y a hora que leo?")
    print ("1. Ver si puedes leer el libro")
    print ("2. Cambiar los datos del libro")
    print ("3. Cambiar velocidad y tiempo")
    print ("4. Salir :(")
    

#Programa principal con datos de un libro como ejemplo

TITULO_LIBRO = "The Setting Sun"
PAGINAS_LIBRO = 174
PROMEDIO_PAGINAS_HORA = 40

paginas_hora, tiempo = datos_usuario()

#Menu principal que se repite con while hasta que el usuario elija opcion 4 
opcion = " "
while opcion != "4":
    mostrar_menu()
    opcion = input("Elige una opcion: ")

    if opcion == "1":
        calcular_acabas_libro (TITULO_LIBRO, PAGINAS_LIBRO,
                               paginas_hora, tiempo)
    elif opcion == "2":
        TITULO_LIBRO, PAGINAS_LIBRO = datos_libro()
    elif opcion == "3":
        paginas_hora, tiempo = datos_usuario()
    elif opcion == "4":
        print("Adios")
    else:
        print("Opcion no valida, elige 1, 2, 3 o 4")
