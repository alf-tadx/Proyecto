"""
Proyecto ¿Y ahora qué leo?
El programa va a tener una lista de libros
y con diferentes preguntas va a recomendar
cual es el mejor para el usuario
"""

#Avance 1 operaciones aritmeticos

"""
Para este avance hice con operaciones una forma que calcule
si puedes o no acabar un libro dependiendo de tu velocidad
de lectura que va a ser un criterio que planeo usar para
el recomendador de libros final.
"""

#Datos de un libro como ejemplo
titulo_libro = "The Setting Sun"
paginas_libro = 174

#Datos del usuario
paginas_hora = float(input("¿Cuántas páginas lees cada hora?", ))
tiempo = float(input("¿Cuántas horas tienes para leer?", ))

#Cantidad de paginas que puedes leer segun el tiempo
paginas_posibles = paginas_hora * tiempo
print ("Segun tu tiempo y velocidad de lectura  puedes leer ",
       paginas_posibles, "páginas")

#Cantidad de horas en las que acabas el libro
horas_libro = paginas_libro / paginas_hora
print("En ", horas_libro, "horas terminas el libro",titulo_libro)

#Paginas que faltan para acabar el libro
paginas_faltantes = paginas_libro - paginas_posibles
print("Te faltarían", paginas_faltantes, "páginas para acabar el libro",
      titulo_libro)
