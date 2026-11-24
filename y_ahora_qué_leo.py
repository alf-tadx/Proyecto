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
    tiempo = int(input("¿Cuántas horas tienes para leer?"))
    return paginas_hora, tiempo

def datos_libro ():
    """
    Pregunta el titulo, las paginas del libro y el genero
    para agregarlos a cada lista
    """
    titulo_libro = input("¿Cual es el titulo del libro? ")
    titulos_libro.append(titulo_libro)
    
    pagina_libro = int(input("¿Cuantas paginas tiene el libro? "))
    paginas_libro.append(pagina_libro)
    
    genero_libro = input("¿Cual es el genero del libro?")
    generos_libro.append(genero_libro)
    
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
    print ("")
    print ("Bienvenidos a ¿Y a hora que leo?")
    print ("1. Ver si puedes leer un libro")
    print ("2. Agregar datos de un libro")
    print ("3. Cambiar velocidad y tiempo")
    print ("4. Ver tu biblioteca")
    print ("5. No tengo ni idea de que leer")
    print ("6. Salir :(")

def mostrar_biblioteca (titulos_libro, paginas_libro, generos_libro):
    """
    Muestra todos los libros que tiene la biblioteca usando listas
    """
    for i in range(len(titulos_libro)):
        print(i, titulos_libro[i], " ", paginas_libro[i], "paginas",
              " ", generos_libro[i])

def elegir_libro (titulos_libro, paginas_libro, generos_libro):
    """
    Sirve para elegir que libro quieres usar para checar
    si lo puedes acabar o no
    """
    mostrar_biblioteca (titulos_libro, paginas_libro, generos_libro)
    libro = int(input("Que numero de libro quieres usar"))
    return libro

def sumar_puntos(fila):
    """"
    Suma los puntos de cada fila de
    la matriz de puntajes para ver cual recomendar
    """
    total = 0
    for puntos in fila:
        total = total + puntos
    return total

def calcular_matriz_puntajes (paginas_libro, generos_libro,
                              genero_usuario, paginas_hora, tiempo):
    """
    Va a hacer una matriz de puntaje de cada libro donde
    haya columnas dependiendo si acabas el libro y si es
    el genero que buscas
    """
    cantidad_libros = len(paginas_libro)
    puntajes = []
    for i in range(cantidad_libros):
        puntajes.append([0,0])
        
    paginas_posibles = calcular_paginas(paginas_hora, tiempo)
    
    for i in range(cantidad_libros):
        porcentaje = calcular_porcentaje_leer(paginas_posibles,
                                              paginas_libro[i])
        puntajes[i][0] = (porcentaje * PUNTOS_TERMINAR / 100)
        
        generos_libro[i] = limpiar_texto (generos_libro[i])
        if generos_libro[i] == genero_usuario:
            puntajes[i][1] = PUNTOS_GENERO
    
    return puntajes
    
def mostrar_puntos(titulos_libro, puntajes):
    """
    Imprime los puntos de cada libro y su total
    """
    print("Puntos de cada libro en tu biblioteca")
    cantidad_libros = len(titulos_libro)
    for i in range(cantidad_libros):
        print(titulos_libro[i], "Terminas el libro?", puntajes[i][0],
              "Genero", puntajes[i][1], "Total", sumar_puntos(puntajes[i]))

def recomendar_libro(titulos_libro, paginas_libro, generos_libro,
                     paginas_hora, tiempo):
    """
    Pregunta que genero quieres leer para hacer la recomendacion de
    tu biblioteca
    """
    genero_usuario = input("¿Que genero quieres leer?")
    genero_usuario = limpiar_texto (genero_usuario)
    puntajes = calcular_matriz_puntajes (paginas_libro, generos_libro,
                              genero_usuario, paginas_hora, tiempo)
    mostrar_puntos(titulos_libro, puntajes)
    
def limpiar_texto (texto):
    """
    Hace que puedas comparar mejor los textos sin problemas
    quitando las mayusculas y los espacios
    """
    texto = texto.lower()
    texto = texto.replace(" ","")
    return texto

def cargar_libros():
    """
    Crea listas vacias y por cada linea del archivo lo separa por "," para
    poder meter la informacion en cada lista
    """
    titulos_libros = []
    paginas_libros = []
    generos_libros = []
    
    f = open("biblioteca.txt", "r")
    for linea in f:
        linea = linea.strip()
        datos = linea.split(",")
        titulos_libros.append(datos[0])
        paginas_libros.append(int(datos[1]))
        generos_libros.append(datos[2])
    f.close()
    
    return titulos_libros, paginas_libros, generos_libros

def guardar_libros(titulos_libros, paginas_libros, generos_libros):
    """
    Borra los libros que estaban guardados antes en el archivo y vuelve a
    sobreescribirlos agregando los nuevos livbros, las paginas se convierten
    en string de nuevo para guardarlas en el archivo
    """
    f = open("biblioteca.txt","w")
    for i in range(len(titulos_libros)):
        f.write(titulos_libros[i]+","+ str(paginas_libros[i]) +
                                ","+ generos_libros[i] + "\n" )
    f.close()

#Biblioteca de libros con archivos
"""
Cambie los libros para utlizar un archivo de la biblioteca en donde esten todos
y que se guarden los cambios que haga el usuario.
"""
titulos_libro, paginas_libro, generos_libro = cargar_libros()

PROMEDIO_PAGINAS_HORA = 40

#Puntaje si terminas el libro y si coincide con el genero
PUNTOS_TERMINAR = 50
PUNTOS_GENERO = 50

#Datos del usuario
paginas_hora, tiempo = datos_usuario()

#Menu principal que se repite con while hasta que el usuario elija opcion 6 
opcion = " "
while opcion != "6":
    mostrar_menu()
    opcion = input("Elige una opcion: ")

    if opcion == "1":
        libro = elegir_libro (titulos_libro, paginas_libro, generos_libro)
        calcular_acabas_libro (titulos_libro[libro] , paginas_libro[libro],
                               paginas_hora, tiempo)
    elif opcion == "2":
        datos_libro()
        guardar_libros(titulos_libro, paginas_libro, generos_libro)
    elif opcion == "3":
        paginas_hora, tiempo = datos_usuario()
    elif opcion == "4":
        mostrar_biblioteca (titulos_libro, paginas_libro, generos_libro)
    elif opcion == "5":
        recomendar_libro(titulos_libro, paginas_libro, generos_libro,
                     paginas_hora, tiempo)
    elif opcion == "6":
        print("Adios")
    else:
        print("Opcion no valida, elige 1, 2, 3, 4, 5 o 6")
