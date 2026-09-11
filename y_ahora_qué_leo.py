"""
Proyecto ¿Y ahora qué leo?
El programa va a tener una lista de libros
y con diferentes preguntas va a recomendar
cual es el mejor para el usuario
"""

#Avance 2 Libre Uso de Funciones

"""
Para este avance cambie las operaciones por diferentes funciones 
para tener un mayor orden y poder utilizarlas mas veces.
"""


#Cantidad de paginas que puedes leer segun el tiempo
def calcular_paginas(paginas_hora,tiempo):
       paginas_posibles = paginas_hora * tiempo
       return paginas_posibles

#Cantidad de horas en las que acabas el libro
def calcular_horas_necesarias (paginas_libro, paginas_hora):
       horas_libro = paginas_libro / paginas_hora
       return horas_libro

#Paginas que faltan para acabar el libro
def calcular_paginas_faltantes(paginas_libro, paginas_posibles):
       paginas_faltantes = paginas_libro - paginas_posibles
       return paginas_faltantes

#Calcular porcentaje que has ledio
def calcular_porcentaje_leer (paginas_posibles, paginas_libro):
       porcentaje = (paginas_posibles / paginas_libro) *100
       return porcentaje
       
#Impresion de resultados
def imprimir_resultados (titulo_libro, paginas_libro, paginas_posibles,
                         horas_libro, paginas_faltantes, porcentaje):
       print ("Resultados finales")
       print ("Libro", titulo_libro, "de", paginas_libro, "paginas")
       print ("Segun tu tiempo y velocilad de lectura puedes leer", paginas_posibles, "paginas")
       print ("En", horas_libro, "horas terminas el libro")
       print ("Te faltarian", paginas_faltantes, "paginas para acabar el libro")
       print ("Puedes leer un", porcentaje, "% del libro")

"""
Programa principal
"""

#Datos de un libro como ejemplo
titulo_libro = "The Setting Sun"
paginas_libro = 174

#Datos del usuario
paginas_hora = float(input("¿Cuántas páginas lees cada hora?", ))
tiempo = float(input("¿Cuántas horas tienes para leer?", ))

#Programa
paginas_posibles =  calcular_paginas(paginas_hora,tiempo)
horas_libro = calcular_horas_necesarias (paginas_libro, paginas_hora)
paginas_faltantes = calcular_paginas_faltantes(paginas_libro, paginas_posibles)
porcentaje = calcular_porcentaje_leer (paginas_posibles, paginas_libro)

#Resultados
imprimir_resultados (titulo_libro, paginas_libro, paginas_posibles,
                         horas_libro, paginas_faltantes, porcentaje)
